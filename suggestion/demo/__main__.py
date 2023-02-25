import tkinter as tk
from viewable import Viewable
from suggestion import Suggestion, DefaultEngine
from suggestion.engine import optimize_dataset, load_dataset


WORDS = ["hi", "house", "boat", "ship", "you", "he", "she", "we", "they",
         "week-end", "people", "happy"]

FONT = ("DejaVu Sans Mono", 11)


class View(Viewable):
    def __init__(self):
        super().__init__()
        self._dataset = list()
        self._field1 = self._field2 = self._field3 = None
        self._suggestion1 = self._suggestion2 = None

    def _build(self):
        # Words
        frame = tk.LabelFrame(self.body, text="WORDS")
        frame.pack(padx=5, pady=(5, 20), fill=tk.X)
        self._field1 = tk.Text(frame, width=60, height=12, font=FONT, wrap="word")
        self._field1.pack(padx=5, pady=5, fill=tk.X)
        self._field1.insert("1.0", " ".join(WORDS))
        button = tk.Button(frame, text="Update",
                           command=self._on_click_update)
        button.pack(padx=5, pady=(0, 5))

        # TextField
        frame = tk.LabelFrame(self.body, text="TEXT FIELD")
        frame.pack(padx=5, pady=5, fill=tk.X)
        self._field2 = tk.Text(frame, width=60, height=12, font=FONT, wrap="word")
        self._field2.pack(padx=5, pady=5, fill=tk.X)

        # EntryField
        frame = tk.LabelFrame(self.body, text="ENTRY FIELD")
        frame.pack(padx=5, pady=5, fill=tk.X)
        self._field3 = tk.Entry(frame, width=60, font=FONT)
        self._field3.pack(padx=5, pady=5, fill=tk.X)

    def _on_map(self):
        self._suggestion1 = Suggestion(self._field2)
        self._suggestion1.activate()
        self._suggestion2 = Suggestion(self._field3)
        self._suggestion2.activate()
        self._update_dataset()

    def _on_click_update(self):
        self._update_dataset()

    def _update_dataset(self):
        dataset = self._field1.get("1.0", tk.END)
        default_engine = DefaultEngine()    
        default_engine.set_dataset(dataset)
        self._suggestion1.set_engine(default_engine)
        self._suggestion2.set_engine(default_engine)


root = tk.Tk()
root.title("Pyrustic Suggestion")

view = View()
view.build(root)

root.mainloop()
