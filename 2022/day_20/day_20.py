import copy
from abc import ABC
from utils import Parser
from utils.lib import answer, ftimer
from utils.base_solution import BaseSolution


# CODE HERE
class Day20Solution(BaseSolution, ABC):
    _input = "2022/day_20/day_20.input.txt"
    _test_input = "2022/day_20/day_20_test.input.txt"

    def parse_input(self):
        lines = Parser.split_by(self.read_input(), "\n", conv_func=lambda x:int(x))
        self.instructions = [(idx, i) for idx, i in enumerate(lines)]

    @staticmethod
    def calc_score(line):
        flat = [b for a, b in line]
        zero_idx = flat.index(0)
        l = len(line)
        return sum([flat[(n + zero_idx) % l] for n in [1000, 2000, 3000]])
    
    @staticmethod
    def mix(new_line, instructions):
        length = len(new_line)

        for idx, k in enumerate(instructions):
            _, val = k
            old_pos = new_line.index(k)
            new_pos = (old_pos + val) % (length - 1)
            new_line.insert(new_pos, new_line.pop(old_pos))
        return new_line
    
    @ftimer
    def solve1(self):
        new_line = self.mix(copy.copy(self.instructions), self.instructions)
        return self.calc_score(new_line)
        
    
    @ftimer
    def solve2(self):
        instructions = [(a, b * 811589153) for a, b in self.instructions]
        new_line = copy.copy(instructions)
        
        for _ in range (10):
            new_line = self.mix(new_line, instructions)
            
        return self.calc_score(new_line)


if __name__ == '__main__':
    s = Day20Solution(use_test_input=False)
    answer(s.solve1())
    answer(s.solve2())

# Your puzzle answer was 9866.
# Your puzzle answer was 12374299815791.