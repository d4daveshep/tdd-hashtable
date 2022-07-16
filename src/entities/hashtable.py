from typing import NamedTuple, Any


class Pair(NamedTuple):
    key: Any
    value: Any


class HashTable:
    def __init__(self, capacity):
        self.__pairs = capacity * [None]
        self.__capacity = capacity

    @property
    def pairs(self):
        return self.__pairs.copy()

    def __len__(self):
        return self.__capacity

    def _index(self, key):
        return hash(key) % len(self)

    def __setitem__(self, key, value):
        self.__pairs[self._index(key)] = Pair(key, value)

    def __getitem__(self, key):
        pair = self.__pairs[self._index(key)]
        if pair is None:
            raise KeyError(key)
        return pair.value

    def __delitem__(self, key):
        if key in self:
            self.__pairs[self._index(key)] = None
        else:
            raise KeyError(key)

    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default
