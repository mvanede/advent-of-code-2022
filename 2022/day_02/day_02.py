import os
import sys
from abc import ABC

from utils import Parser
from utils.lib import get_timer, answer, pruntime
from utils.base_solution import BaseSolution
_ST = get_timer()


# CODE HERE
class Day02Solution(BaseSolution, ABC):
    _input = "day_02_input.txt"
    _test_input = "day_02_test_input.txt"
    use_test_input = True

    def __init__(self, use_test_input):
        self.grid = None
        self.use_test_input = use_test_input
        self.parse_input()

    def path_to_input(*args, **kwargs):
        return os.path.dirname(__file__)

    def parse_input(self):
        self.grid = Parser.get_int_grid(self.read_input())
        self.grid.pprint(sep=' ')

    def solve1(self):
        pass

    def solve2(self):
        pass


if __name__ == '__main__':
    s = Day02Solution(use_test_input=True)
    answer(s.solve1())
    answer(s.solve2())
    pruntime(_ST)
