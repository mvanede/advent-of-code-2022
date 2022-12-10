import os
from abc import ABC

from utils import Parser
from utils.lib import get_timer, answer, pruntime
from utils.base_solution import BaseSolution
_ST = get_timer()

class Day03Solution(BaseSolution, ABC):
    _input = "2022/day_03/day_03.input.txt"
    _test_input = "2022/day_03/day_03_test.input.txt"
    rucksacks = []

    def parse_input(self):
        self.rucksacks = Parser.split_by(self.read_input(), "\n", "", conv_func=None)  # lambda x:int(x)

    @staticmethod
    def get_prio(item):
        return ord(item) - 38 if item.isupper() else ord(item) - 96

    def solve1(self):
        prio_sum = 0
        for r in self.rucksacks:
            halfway = len(r)//2
            c1 = r[:halfway]
            c2 = r[halfway:]
            intersection = list(set(c1) & set(c2))
            item = intersection.pop()
            prio_sum += self.get_prio(item)
        return prio_sum

    def solve2(self):
        prio_sum = 0
        for i in range(0, len(self.rucksacks), 3):
            c1 = self.rucksacks[i]
            c2 = self.rucksacks[i + 1]
            c3 = self.rucksacks[i + 2]
            intersection = list(set(c1) & set(c2) & set(c3))
            item = intersection.pop()
            prio_sum += self.get_prio(item)

        return prio_sum


if __name__ == '__main__':
    s = Day03Solution(use_test_input=False)
    answer(s.solve1())
    answer(s.solve2())

    pruntime(_ST)

# Your puzzle answer was 7850.
# Your puzzle answer was 2581.


