from collections import UserList
from functools import reduce


class MapReduceList(UserList):
    def reduce(self, func):
        return reduce(func, self.data)

    def map(self, func):
        self.data = list(map(func, self.data))
        return self

    def filter(self, func):
        self.data = list(filter(func, self.data))
        return self
