import tkinter as tk
from suggestion import error
from suggestion import dto
from suggestion.constant import WHITESPACE
from suggestion.engine import DefaultEngine
from suggestion.dropdown import DefaultDropdown


class Suggestion:
    def __init__(self, widget, dataset=None,
                 engine=DefaultEngine, dropdown=DefaultDropdown):
        self._widget = widget
        self._dataset = dataset
        self._engine = engine
        self._dropdown = dropdown
        self._dropdown_visible = False
        self._multiline_field = None
        self._word = None
        self._cache = None
        self._previous_word = None
        self._is_whitespace = None
        self._word_index = None
        self._word_context = None
        self._active = False
        self._count = 0
        self._should_relocate = False
        self._setup()

    @property
    def widget(self):
        return self._widget

    @property
    def engine(self):
        return self._engine

    @property
    def dropdown(self):
        return self._dropdown

    @property
    def multiline_field(self):
        return self._multiline_field

    @property
    def active(self):
        return self._active

    def suggest(self, data):
        if not self._active:
            return False
        self._clear()
        self._word = ""
        self._word_index = self._widget.index(tk.INSERT)
        self._report_results(data)
        return True

    def activate(self):
        self._active = True

    def deactivate(self):
        self._active = False

    def set_dataset(self, dataset):
        if not self._engine:
            return
        self._clear(focus_set=False)
        self._engine.set_dataset(dataset)

    def extend_dataset(self, val):
        if not self._engine:
            return
        self._clear(focus_set=False)
        self._engine.extend_dataset(val)

    def read_dataset(self):
        if not self._engine:
            yield from ()
            return
        for x in self._engine.read_dataset():
            yield x

    def set_engine(self, engine, dataset=None):
        self._clear(focus_set=False)
        if isinstance(engine, type):
            self._engine = engine()
        else:
            self._engine = engine
        if dataset:
            self._engine.set_dataset(dataset)

    def _setup(self):
        # field
        if isinstance(self._widget, tk.Entry):
            self._multiline_field = False
        elif isinstance(self._widget, tk.Text):
            self._multiline_field = True
        else:
            msg = "Suggestion supports these Tkinter widgets: tk.Entry and tk.Text"
            raise error.IllegalWidgetError(msg)
        #
        if isinstance(self._engine, type):
            self._engine = self._engine()
        if isinstance(self._dropdown, type):
            self._dropdown = self._dropdown()
        # engine
        if self._dataset:
            self._engine.set_dataset(self._dataset)
            self._dataset = None
        # build dropdown
        self._dropdown.build(self._widget)
        self._hide_dropdown(focus_set=False)
        # binding
        self._widget.bind("<Return>", self._on_key_press, True)
        self._widget.bind("<KeyPress>", self._on_key_press, True)
        self._widget.bind("<KeyRelease>", self._on_key_release, True)
        command = lambda e, self=self: self._clear()
        self._widget.bind("<Button-1>", command, True)
        self._widget.bind("<Button-2>", command, True)
        self._widget.bind("<Button-3>", command, True)
        self._dropdown.body.bind("<Button-1>", command, True)
        self._dropdown.body.bind("<Button-2>", command, True)
        self._dropdown.body.bind("<Button-3>", command, True)
        # close dropdown on focusOut
        command = lambda e, self=self: self._clear(focus_set=False)
        self._widget.bind("<FocusOut>", command)

    def _on_key_press(self, event):
        if not self._active:
            return
        keysym = event.keysym
        # Press 'space' will close the dropdown
        if keysym == "space":
            if self._dropdown_visible:
                self._clear()
        # Press 'Tab' will fill the text field with the selected string
        elif keysym == "Tab":
            if self._dropdown_visible:
                self._edit_field()
                return "break"
        # Press 'Escape' to hide the dropdown
        elif keysym == "Escape":
            self._clear()
        # Press 'Return' will replace the current word in the text field
        elif keysym == "Return":
            if self._dropdown_visible:
                self._edit_field()
                return "break"
        elif keysym == "Up":
            if self._dropdown_visible:
                self._dropdown.select_up()
                return "break"
        elif keysym == "Down":
            if self._dropdown_visible:
                self._dropdown.select_down()
                return "break"
        elif keysym == "BackSpace":
            if not self._dropdown_visible:
                self._clear()

    def _on_key_release(self, event):
        if not self._active:
            return
        keysym = event.keysym
        if keysym in ("Escape", "Up", "Down", "Caps_Lock", "??",
                      "Control_L", "Control_R", "Shift_L", "Shift_R"):
            return
        if keysym == "BackSpace" and not self._dropdown_visible:
            return
        if keysym in ("Left", "Right") and not self._dropdown_visible:
            return
        self._process_word(event)

    def _process_word(self, event):
        word = whitespace = None
        if event.keysym in WHITESPACE:
            is_whitespace = True
            whitespace = WHITESPACE[event.keysym]
            self._word_index = self._widget.index(tk.INSERT)
            self._count = 0
            self._previous_word = self._cache
        else:
            is_whitespace = False
            word, self._word_index = self._get_word()
            self._count += 1
        if not word:
            self._clear()
            return
        if self._is_whitespace or self._multiline_field == "entry" or not self._word:
            self._should_relocate = True
        else:
            self._should_relocate = False
        self._cache_word(word)
        self._word = word
        self._is_whitespace = is_whitespace
        if whitespace:
            return
        # Info dataclass
        self._word_context = dto.WordContext(event=event,
                                             word_index=self._word_index,
                                             word=self._word,
                                             previous_word=self._previous_word)
        command = lambda: self._engine.search(self._word_context,
                                              self._report_results)
        self._widget.after(0, command)

    def _report_results(self, data=None):
        if self._count > 0:
            self._count -= 1
        if not data:
            self._clear()
            return
        if self._count == 0:
            self._dropdown.populate(data)
            if self._should_relocate:
                self._relocate_dropdown()
                #self._dropdown.relocate(self._word_context)
            self._unhide_dropdown()

    def _edit_field(self):
        if not self._dropdown_visible:
            return
        selected = self._dropdown.selected
        #if not selected or not self._word:
        #    return
        if not selected:
            return
        cache = selected.lstrip(" ")
        cache = cache.rstrip(" ")
        self._cache_word(cache)
        # let's separate 'selected' into left and right parts
        word_size = len(self._word)
        left_part = selected[0:word_size]
        right_part = selected[len(self._word):]
        if left_part == self._word:
            self._widget.insert(tk.INSERT, right_part)
        else:
            if self._multiline_field:
                line, col = self._word_index.split(".")
                cache = ".".join((line, str(int(col) + word_size)))
            else:
                cache = self._word_index + word_size
            self._widget.delete(self._word_index, cache)
            self._widget.insert(tk.INSERT, selected)
        self._clear()

    def _clear(self, focus_set=True):
        self._hide_dropdown(focus_set)
        self._word = None
        self._word_index = None
        self._should_relocate = True
        self._count = 0

    def _get_word(self):
        cursor_index = self._widget.index(tk.INSERT)
        if self._multiline_field:
            line, i = cursor_index.split(".")
            data = self._widget.get(".".join((line, "0")), tk.END)
            word, word_index = self._extract_word(int(i), data)
            return word, ".".join((line, str(word_index)))
        else:
            data = self._widget.get()
            return self._extract_word(cursor_index, data)

    def _extract_word(self, cursor_index, line):
        left = []
        # left
        for i in reversed(range(0, cursor_index)):
            char = line[i]
            if char in (" ", "\t", "\n"):
                break
            left.insert(0, char)
        word_index = cursor_index - len(left)
        word = "".join(left)
        return word, word_index

    def _hide_dropdown(self, focus_set=True):
        if self._dropdown:
            self._dropdown.body.withdraw()
            if focus_set:
                self._widget.focus_set()
        self._dropdown_visible = False

    def _unhide_dropdown(self):
        if self._dropdown:
            self._dropdown.body.deiconify()
        self._dropdown_visible = True

    def _cache_word(self, word):
        if word and word not in WHITESPACE.values():
            self._cache = word

    def _relocate_dropdown(self):
        word_index = self._word_index if self._word_index else self._widget.index(tk.INSERT)
        dropdown_body = self._dropdown.body
        if self._multiline_field:
            x, y, width, height = self._widget.bbox(word_index)
        else:
            x, y, width, height = self._widget._getints(self._widget.tk.call((self._widget, "bbox", word_index)))
        x = x + self._widget.winfo_rootx()
        y = y + self._widget.winfo_rooty()
        dropdown_height = dropdown_body.winfo_height()
        margin_y = 3
        if dropdown_height + y + height > self._widget.winfo_screenheight():
            y = y - dropdown_height - margin_y
        else:
            y = y + height + margin_y
        dropdown_body.withdraw()
        dropdown_body.update_idletasks()
        dropdown_body.geometry("+{}+{}".format(x, y))
        dropdown_body.deiconify()
