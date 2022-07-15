class HashTable:
    def __init__(self, capacity):
        self.values = capacity * [None]
        self.__capacity = capacity

    def __len__(self):
        return self.__capacity

    def __my_index(self, key):
        return hash(key) % len(self)

    def __setitem__(self, key, value):
        index = self.__my_index(key)
        self.values[index] = value

    def __getitem__(self, key):
        index = self.__my_index(key)
        value = self.values[index]
        if value is None:
            raise KeyError(key)
        return value

    def __delitem__(self, key):
        index = self.__my_index(key)
        self.values[index] = None

    def __contains__(self, key):
        index = self.__my_index(key)
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True