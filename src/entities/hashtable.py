class HashTable:
    def __init__(self, capacity):
        self.values = capacity * [None]
        self.__capacity = capacity

    def __len__(self):
        return self.__capacity
