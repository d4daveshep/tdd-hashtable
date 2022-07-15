class HashTable:
    def __init__(self, capacity):
        self.values = capacity * [None]
        self.__capacity = capacity

    def __len__(self):
        return self.__capacity

    def _index(self, key):
        return hash(key) % len(self)

    def __setitem__(self, key, value):
        index = self._index(key)
        self.values[index] = value

    def __getitem__(self, key):
        index = self._index(key)
        value = self.values[index]
        if value is None:
            raise KeyError(key)
        return value

    def __delitem__(self, key):
        if key in self:
            self[key] = None
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
