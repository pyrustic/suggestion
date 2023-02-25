import tkinter as tk
from viewable import Viewable
from suggestion import error


class Dropdown(Viewable):
    """ This is the 'interface' that your Dropdown must respects """

    @property
    def selected(self):
        """ Returns the selected word (string)"""
        return None

    def populate(self, data):
        """ Called by Suggestion after the engine sent results """
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
        if not self.body or not data:
            self._data = None
            self._selected_index = None
            return
        self._data = data
        self._selected_index = 0
        self._listbox.delete(0, tk.END)
        self._listbox.insert(0, *data)
        self._select_line(0)

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

    def _create_body(self, parent):
        return tk.Toplevel(parent)

    def _build(self):  # TODO add a vertical scrollbar if entries > 5
        self.body.overrideredirect(True)
        self._listbox = tk.Listbox(self.body, height=5,
                                   borderwidth=0)
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
