from abc import ABC

from utils import Parser
from utils.lib import get_timer, answer, pruntime
from utils.base_solution import BaseSolution
_ST = get_timer()


class Day04Solution(BaseSolution, ABC):
    _input = "2022/day_04/day_04_input.txt"
    _test_input = "2022/day_04/day_04_test_input.txt"
    assignments = None

    def parse_input(self):
        self.assignments = Parser.split_by(self.read_input(), "\n", ",", "-", conv_func=lambda x:int(x))

    @staticmethod
    def get_list(_range):
        return [*range(_range[0], _range[1] + 1)]

    def solve1(self):
        s = 0
        for pair in self.assignments:
            elf1 = self.get_list(pair[0])
            elf2 = self.get_list(pair[1])
            overlap = list(set(elf1) & set(elf2))

            if len(overlap) == len(elf1) or len(overlap) == len(elf2):
                s += 1
        return s

    def solve2(self):
        s = 0
        for pair in self.assignments:
            elf1 = self.get_list(pair[0])
            elf2 = self.get_list(pair[1])
            overlap = list(set(elf1) & set(elf2))
            if len(overlap):
                s += 1
        return s

    # Afterthought: Solution with O(1)
    def solve2a(self):
        s = 0
        for pair in self.assignments:
            p0 = pair[0]
            p1 = pair[1]

            start_overlap = max(p0[0], p1[0])
            end_overlap = min(p0[1], p1[1]) + 1
            overlap_size = end_overlap - start_overlap
            if overlap_size > 0:
                s += 1

        return s


if __name__ == '__main__':
    s = Day04Solution(use_test_input=False)
    answer(s.solve1())
    answer(s.solve2())
    answer(s.solve2a())
    pruntime(_ST)

# Your puzzle answer was 518.
# Your puzzle answer was 909.
