class HashTable:
    def __init__(self, capacity):
        self.pairs = capacity * [None]
        self.__capacity = capacity

    def __len__(self):
        return self.__capacity

    def _index(self, key):
        return hash(key) % len(self)

    def __setitem__(self, key, value):
        self.pairs[self._index(key)] = (key, value)

    def __getitem__(self, key):
        pair = self.pairs[self._index(key)]
        if pair is None:
            raise KeyError(key)
        return pair[1]

    def __delitem__(self, key):
        if key in self:
            self.pairs[self._index(key)] = None
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
