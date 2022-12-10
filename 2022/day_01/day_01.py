import os
import sys
from abc import ABC

from utils import Parser
from utils.lib import get_timer, answer, pruntime
from utils.base_solution import BaseSolution
_ST = get_timer()


# CODE HERE
class Day01Solution(BaseSolution, ABC):
    _input = "2022/day_01/day_01.input.txt"
    _test_input = "2022/day_01/day_01_test.input.txt"
    food = None

    def parse_input(self):
        self.food = Parser.group_by_double_newline(self.read_input(), conv_func=lambda x: int(x))  # lambda x:int(x)

    def solve1(self):
        return max([sum(f) for f in self.food])

    def solve2(self):
        all_cal = [sum(f) for f in self.food]
        all_cal.sort(reverse=True)
        return sum(all_cal[:3])


if __name__ == '__main__':
    s = Day01Solution(use_test_input=False)
    answer(s.solve1())
    answer(s.solve2())
    pruntime(_ST)

# Your puzzle answer was 71471.
# Your puzzle answer was 211189.

