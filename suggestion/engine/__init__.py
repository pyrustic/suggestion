import os
import os.path
from pathlib import Path
from suggestion import error


class Engine:

    def set_dataset(self, val):
        pass

    def extend_dataset(self, val):
        pass

    def read_dataset(self):
        pass

    def search(self, info, callback):
        pass


class DefaultEngine(Engine):

    def __init__(self):
        super().__init__()
        self._dataset = dict()

    def set_dataset(self, val):
        if isinstance(val, dict):
            self._dataset = val
            return
        dataset = list()
        if isinstance(val, str):
            dataset = val.split()
        elif isinstance(val, Path):
            dataset = load_dataset(str(val.resolve()))
        elif isinstance(val, dict):
            pass
        else:
            dataset = val
        self._dataset = optimize_dataset(dataset)

    def read_dataset(self):
        if not self._dataset:
            yield from ()
            return
        for key, val in self._dataset.items():
            for item in val:
                yield item

    def search(self, info, callback):
        # return if word is a whitespace
        # whitespace: " ", "\t", "\n"
        self._search(info.word, callback)

    def _setup(self):
        if isinstance(self._dataset, str):
            # load words if dataset is a filename
            if not os.path.exists(self._dataset):
                raise error.Error("The dataset filename doesn't exist !")
            # now _dataset is a sequence of words
            with open(self._dataset, "r") as file:
                self._dataset = file.read().split()
        self._optimized_dataset = optimize_dataset(self._dataset)

    def _search(self, word, callback):
        result = []
        for key, val in self._dataset.items():
            if key.startswith(word) or word.startswith(key):
                for item in val:
                    if item.startswith(word):
                        result.append(item)
        callback(result)


def load_dataset(filename):
    dataset = list()
    if not os.path.exists(filename):
        raise error.Error("The dataset filename doesn't exist !")
    with open(filename, "r") as file:
        while True:
            line = file.readline()
            if not line:
                break
            items = line.split()
            dataset.extend(items)
    return dataset


def optimize_dataset(dataset):
    optimized_dataset = {}
    for word in dataset:
        prefix = word[0:3]
        if prefix not in optimized_dataset:
            optimized_dataset[prefix] = []
        optimized_dataset[prefix].append(word)
    return optimized_dataset
