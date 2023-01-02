import re
from abc import ABC
from copy import copy
from utils import Parser, Grid
from utils.grid import Coord
from utils.lib import answer, ftimer
from utils.base_solution import BaseSolution
from utils.location import Direction


class Map(Grid):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = Coord(self.get_row(0).index('.'), 0)
        self.facing = Direction.EAST

    def turn(self, d):
        if d == 'L':
            self.facing = self.facing.ccw()
        elif d == 'R':
            self.facing = self.facing.cw()

    def move(self, steps):
        # print('Move ', steps, ' steps into ', self.facing, ' starting ', self.position)
        while (steps):
            nxt = self.next()
            if self.get(nxt) != '#':
                self.position = self.next()
                self.set(self.position.x, self.position.y, str(self.facing))
                steps -= 1
            else:
                break

    def next(self):
        p = copy(self.position)
        match self.facing:
            case Direction.SOUTH:
                diff = (0, 1)
            case Direction.NORTH:
                diff = (0, -1)
            case Direction.WEST:
                diff = (-1, 0)
            case Direction.EAST:
                diff = (1, 0)

        # If out of bounds, or white space, wrap!
        p = Coord((p.x + diff[0]) % self.width, (p.y + diff[1]) % self.height)
        while self.get(p) == ' ':
            p = Coord((p.x + diff[0]) % self.width, (p.y + diff[1]) % self.height)

        return p


class Day22Solution(BaseSolution, ABC):
    _input = "2022/day_22/day_22.input.txt"
    _test_input = "2022/day_22/day_22_test.input.txt"

    def parse_input(self):
        map, path = Parser.split_by(self.read_input(), "\n\n", conv_func=None)  # lambda x:int(x)
        max_row_len = max([len(l) for l in map.split('\n')])

        # Pad all rows
        map = [l.ljust(max_row_len) for l in map.split('\n')]
        self.map = Map(Parser.split_by(map, ""))
        self.path = re.findall('\d*\D+', path + 'X')  # adding extra character ugly hack

    @ftimer
    def solve1(self):
        for step in self.path:
            move = int(step[:-1])
            turn = step[-1]
            self.map.move(move)
            self.map.turn(turn)
        return 1000 * (self.map.position.y + 1) + 4 * (self.map.position.x + 1) + int(self.map.facing)

    @ftimer
    def solve2(self):
        pass


if __name__ == '__main__':
    s = Day22Solution(use_test_input=False)
    answer(s.solve1())
    # answer(s.solve2())

#  Your puzzle answer was 88268.