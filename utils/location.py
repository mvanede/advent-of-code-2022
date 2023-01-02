from enum import IntEnum
from typing import NamedTuple

Coord = NamedTuple('Coord', [('x', int), ('y', int)])


class Direction(IntEnum):
    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3

    def __str__(self):
        _str_map = {0: '>', 1: 'v', 2: '<', 3: '^'}
        return _str_map[self.value]

    def cw(self):
        return Direction((self.value + 1) % 4)

    def ccw(self):
        return Direction((self.value - 1) % 4)

    def t180(self):
        return Direction((self.value + 2) % 4)
