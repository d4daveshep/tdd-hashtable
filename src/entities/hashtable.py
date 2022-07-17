from typing import NamedTuple, Any


class Pair(NamedTuple):
    key: Any
    value: Any


class HashTable:
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError("Capacity must be greater than zero")
        self.__pairs = capacity * [None]
        self.__capacity = capacity

    @property
    def pairs(self):
        return {pair for pair in self.__pairs if pair}
        # return list of non-None pairs

    @property
    def values(self):
        return [pair.value for pair in self.pairs]

    @property
    def keys(self):
        return {pair.key for pair in self.pairs}

    @property
    def capacity(self):
        return(len(self.__pairs))
    
    def __len__(self):
        return len(self.pairs)

    def _index(self, key):
        return hash(key) % self.capacity

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
