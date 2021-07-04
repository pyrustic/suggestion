import os
import os.path
import tkinter as tk
from viewable import Viewable


class Suggestion:
    def __init__(self, widget, dataset=None):
        self._widget = widget
        self._dataset = dataset
        self._engine = None
        self._dropdown = None
        self._dropdown_visible = False
        self._field = None
        self._word = None
        self._word_index = None
        self._info = None
        self._activated = True
        self._count = 0
        self._should_relocate = False
        self._setup()

    @property
    def widget(self):
        return self._widget

    @property
    def dataset(self):
        return self._dataset

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, val):
        self._clear()
        self._engine = val

    @property
    def dropdown(self):
        return self._dropdown

    @dropdown.setter
    def dropdown(self, val):
        self._clear()
        self._dropdown = val

    @property
    def activated(self):
        return self._activated

    def activate(self):
        self._activated = True

    def deactivate(self):
        self._activated = False

    def _setup(self):
        # field
        if isinstance(self._widget, tk.Entry):
            self._field = "entry"
        elif isinstance(self._widget, tk.Text):
            self._field = "text"
        else:
            raise IllegalWidgetError("Suggestion supports these Tkinter widgets: tk.Entry and tk.Text")
        # default dataset
        if not self._dataset:
            self._dataset = tuple()
        # default engine
        self._engine = DefaultEngine(self._dataset)
        # default dropdown
        self._dropdown = DefaultDropdown()
        self._dropdown.build()
        self._hide_dropdown(focus_set=False)
        # binding
        self._widget.bind("<KeyPress>", self._on_key_press, "+")
        self._widget.bind("<KeyRelease>", self._on_key_release, "+")
        cache = lambda e, self=self: self._clear()
        self._widget.bind("<Button-1>", cache, "+")
        self._widget.bind("<Button-2>", cache, "+")
        self._widget.bind("<Button-3>", cache, "+")
        self._dropdown.body.bind("<Button-1>", cache, "+")
        self._dropdown.body.bind("<Button-2>", cache, "+")
        self._dropdown.body.bind("<Button-3>", cache, "+")
        #self._widget.bind("<Escape>", lambda e: self._hide_dropdown)
        # close dropdown on focusOut
        self._widget.bind("<FocusOut>",
                          lambda e,
                                 self=self: self._clear(focus_set=False))

    def _on_key_press(self, event):
        if not self._activated:
            return
        keysym = event.keysym
        # Press 'space' or 'Return' will close the dropdown
        if keysym == "space":
            self._clear()
        # Press 'Tab' will fill the text field with the selected string
        elif keysym == "Tab":
            if self._dropdown_visible:
                self._edit_field()
                return "break"
        # Press 'Escape' to hide the dropdown
        elif keysym == "Escape":
            #self._hide_dropdown()
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
            self._clear()

    def _on_key_release(self, event):
        if not self._activated:
            return
        keysym = event.keysym
        if keysym in ("space", "Tab", "Escape", "Return",
                      "Up", "Down", "BackSpace", "Caps_Lock", "??",
                      "Control_L", "Shift_L", "Control_R", "Shift_R"):
            return
        if keysym in ("Left", "Right") and not self._dropdown_visible:
            return
        self._process_word(event)

    def _process_word(self, event):
        word, self._word_index = self._get_word()
        if not word:
            self._clear()
            return
        if self._word is None:
            self._should_relocate = True
        else:
            self._should_relocate = False
        self._word = word
        # Info dataclass
        self._info = Info(event=event, word=self._word,
                          word_index=self._word_index,
                          widget=self._widget,
                          field=self._field)
        self._count += 1
        command = (lambda self=self:
                   self._engine.process(self._info,
                                        self._report_results))
        self._widget.after(0, command)

    def _report_results(self, data):
        self._count -= 1
        if not data:
            self._clear()
            return
        if self._count == 0:
            self._dropdown.populate(data)
            if self._should_relocate:
                self._dropdown.relocate(self._info)
            self._unhide_dropdown()

    def _edit_field(self):
        if not self._dropdown_visible:
            return
        selected = self._dropdown.selected
        if not selected or not self._word:
            return
        # let's separate 'selected' into left and right parts
        word_size = len(self._word)
        left_part = selected[0:word_size]
        right_part = selected[len(self._word):]
        if left_part == self._word:
            self._widget.insert(tk.INSERT, right_part)
        else:
            line, col = self._word_index.split(".")
            cache = ".".join((line, str(int(col) + word_size)))
            self._widget.delete(self._word_index, cache)
            self._widget.insert(tk.INSERT, selected)
        # close
        self._clear()

    def _clear(self, focus_set=True):
        self._hide_dropdown(focus_set)
        self._word = None
        self._word_index = None

    def _get_word(self):
        cursor_index = self._widget.index(tk.INSERT)
        if self._field == "entry":
            data = self._widget.get()
            return self._extract_word(cursor_index, data)
        elif self._field == "text":
            line, i = cursor_index.split(".")
            data = self._widget.get(".".join((line, "0")), tk.END)
            word, word_index = self._extract_word(int(i), data)
            return word, ".".join((line, str(word_index)))
        else:
            raise Error("Unknown field type")

    def _extract_word(self, cursor_index, line):
        left = []
        right = []
        # left
        for i in reversed(range(0, cursor_index)):
            char = line[i]
            if char in (" ", "\t", "\n"):
                break
            left.insert(0, char)
        word_index = cursor_index - len(left)
        word = "".join(left)
        # right
        #for i in range(index, len(line)):
        #    char = line[i]
        #    if char in (" ", "\t", "\n"):
        #        break
        #left.extend(right)
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
            #self._dropdown.body.focus_set()
            #self._dropdown.body.grab_set()
        self._dropdown_visible = True


class Dropdown(Viewable):
    """ This is the 'interface' that your Dropdown must respects """

    @property
    def selected(self):
        """ Returns the selected word (string)"""
        return None

    def populate(self, data):
        """ Called by Suggestion after the engine sent results """
        pass

    def relocate(self, info):
        """ Called by Suggestion to indicate the Dropdown to change its coords """
        pass

    def select_up(self):
        """ User pressed the up arrow key """
        pass

    def select_down(self):
        """ User pressed the down arrow key """
        pass


class DefaultDropdown(Dropdown):
    def __init__(self):
        super().__init__()
        self._data = None
        self._selected_index = None
        self._info = None
        self._listbox = None

    @property
    def selected(self):
        if self._selected_index is None:
            return ""
        return self._data[self._selected_index]

    def populate(self, data):
        if not self._body or not data:
            self._data = None
            self._selected_index = None
            return
        self._data = data
        self._selected_index = 0
        self._listbox.delete(0, tk.END)
        self._listbox.insert(0, *data)
        #listbox_height = 5
        data_size = len(data)
        #if data_size < 5:
        #    listbox_height = data_size
        #self._listbox.config(height=listbox_height)
        self._select_line(0)

    def relocate(self, info):
        field = info.field
        widget = info.event.widget
        word_index = info.word_index
        if field == "text":
            x, y, width, height = widget.bbox(word_index)
        elif field == "entry":
            x, y, width, height = widget._getints(widget.tk.call((widget, "bbox", word_index)))
        else:
            raise IllegalWidgetError
        x = x + widget.winfo_rootx()
        y = y + widget.winfo_rooty()
        dropdown_height = self._body.winfo_height()
        if dropdown_height + y + height > widget.winfo_screenheight():
            y = y - dropdown_height
        else:
            y = y + height
        self._body.withdraw()
        self._body.update_idletasks()
        self._body.geometry("+{}+{}".format(x, y))
        self._body.deiconify()

    def select_up(self):
        if not self._data or self._selected_index is None:
            return
        self._selected_index -= 1
        if self._selected_index == -1:
            self._selected_index = len(self._data) - 1
        self._select_line(self._selected_index)

    def select_down(self):
        if not self._data or self._selected_index is None:
            return
        self._selected_index += 1
        if self._selected_index == len(self._data):
            self._selected_index = 0
        self._select_line(self._selected_index)

    def _build(self):
        self._body = tk.Toplevel()
        self._body.overrideredirect(1)
        self._listbox = tk.Listbox(self._body, height=5)
        self._listbox.pack()

    def _on_map(self):
        pass

    def _on_destroy(self):
        pass

    def _select_line(self, index):
        self._listbox.selection_clear(0, tk.END)
        self._listbox.selection_set(index)
        self._listbox.see(index)
        self._listbox.activate(index)
        self._listbox.selection_anchor(index)


class Engine:
    def process(self, info, callback):
        pass


class DefaultEngine(Engine):

    def __init__(self, dataset):
        self._dataset = dataset
        self._setup()

    def process(self, info, callback):
        word = info.word
        self._search(word, callback)

    def _setup(self):
        if isinstance(self._dataset, str):
            # load words if dataset is a filename
            if not os.path.exists(self._dataset):
                raise Error("The dataset filename doesn't exist !")
            # now _dataset is a sequence of words
            with open(self._dataset, "r") as file:
                self._dataset = file.read().split()
        self._prepare_dataset()

    def _prepare_dataset(self):
        cache = {}
        for word in self._dataset:
            prefix = word[0:3]
            if prefix not in cache:
                cache[prefix] = []
            cache[prefix].append(word)
        self._dataset = cache

    def _search(self, word, callback):
        result = []
        for key, val in self._dataset.items():
            if key.startswith(word) or word.startswith(key):
                for item in val:
                    if item.startswith(word):
                        result.append(item)
        callback(result)


class Info:
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)


class Error(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else ""
        super().__init__(self.message)

    def __str__(self):
        return self.message


class IllegalWidgetError(Error):
    pass