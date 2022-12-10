from abc import ABC
from pprint import pprint

from utils import Parser
from utils.lib import get_timer, answer, pruntime
from utils.base_solution import BaseSolution

_ST = get_timer()


# CODE HERE
class Day10Solution(BaseSolution, ABC):
    _input = "2022/day_10/day_10.input.txt"
    _test_input = "2022/day_10/day_10_test.input.txt"

    def __init__(self, use_test_input):
        self.use_test_input = use_test_input
        self.instructions = None
        self.parse_input()
        self.values = self.exec()

    def parse_input(self):
        self.instructions = [(x[0], int(x[1]) if len(x) > 1 else None) for x in
                             Parser.split_by(self.read_input(), "\n", " ", conv_func=None)]

    def exec(self):
        values = {}
        cycle = 0
        x = 1

        for instr, val in self.instructions:
            if instr == 'addx':
                values[cycle] = x
                values[cycle + 1] = x
                cycle += 2
                x += val
            elif instr == 'noop':
                values[cycle] = x
                cycle += 1
        values[cycle] = x
        return values

    def solve1(self):
        # Calculate sum
        total = 0
        for y in range(20, len(self.values), 40):
            total += y * self.values[y - 1]

        return total

    def solve2(self):
        screen = ['.' for _ in range(40 * 6)]
        for cycle, val in self.values.items():
            sprite_position = [(cycle % 40), (cycle % 40) + 1, (cycle % 40) + 2]

            # Val+1 because our list index is zero-based and val is 1-based
            if val + 1 in sprite_position:
                screen[cycle] = '#'

        line_width = 40
        for i in range(0, len(screen), line_width):
            print(''.join(screen[i:i + line_width]))

        return ''.join(screen)


if __name__ == '__main__':
    s = Day10Solution(use_test_input=False)
    answer(s.solve1())
    s.solve2()
    pruntime(_ST)

# Your puzzle answer was 14820.
# Your puzzle answer was RZEKEFHA.
