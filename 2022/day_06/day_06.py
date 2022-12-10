from abc import ABC
from utils.lib import get_timer, answer, pruntime
from utils.base_solution import BaseSolution
_ST = get_timer()


# CODE HERE
class Day06Solution(BaseSolution, ABC):
    _input = "2022/day_06/day_06.input.txt"
    _test_input = "2022/day_06/day_06_test.input.txt"
    stream = None
    
    def parse_input(self):
        self.stream = self.read_input()
    
    def find_marker(self, length):
        for x in range(length, len(self.stream) - 1):
            all_unique = set(self.stream[x - length:x])
            if len(all_unique) == length:
                return x

    def solve1(self):
        return self.find_marker(length=4)

    def solve2(self):
        return self.find_marker(length=14)


if __name__ == '__main__':
    s = Day06Solution(use_test_input=False)
    answer(s.solve1())
    answer(s.solve2())
    pruntime(_ST)


#  Your puzzle answer was 1987.
# Your puzzle answer was 3059.

