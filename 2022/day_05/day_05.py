import copy
import textwrap
from abc import ABC

from utils import Parser
from utils.base_solution import BaseSolution
from utils.lib import get_timer, pruntime, answer

_ST = get_timer()


# CODE HERE
class Day05Solution(BaseSolution, ABC):
    _input = "2022/day_05/day_05.input.txt"
    _test_input = "2022/day_05/day_05_test.input.txt"
    stacks = None
    _stacks = None
    moves = []

    def parse_input(self):
        stack_lines, move_lines = Parser.split_by(self.read_input(), "\n\n", "\n", conv_func=None)  # lambda x:int(x)
        _stack_labels = stack_lines.pop()
        _crates = stack_lines

        # Columns have a fixed with of 4 (3, plus space between). We need use this line
        # since we can't be sure every stack is filled (though in practice they are ;)
        stack_labels = textwrap.wrap(_stack_labels, 4, drop_whitespace=True)
        nr_of_stacks = len(stack_labels)
        self.stacks = [[] for _ in range(nr_of_stacks)]

        for crate_row in _crates:
            # Each stack has width of 4 characters in the input.
            for idx, crate in  enumerate(textwrap.wrap(crate_row, 4, drop_whitespace=False)):
                if crate[1] != ' ':
                    # Add each to bottom of stack as we read input from the top, a space symbolizes void on the stack, so skip
                    self.stacks[idx].insert(0, crate[1])

        # make a backup
        self._stacks = copy.deepcopy(self.stacks)

        for m in move_lines:
            self.moves.append([int(s) for s in m.split() if s.isdigit()])

    def reset(self):
        self.stacks = copy.deepcopy(self._stacks)

    def format_answer(self):
        return ''.join([s.pop() for s in self.stacks])

    def solve1(self):
        self.reset()

        # Start moving
        for nr, frm, to in self.moves:
            for i in range(nr):
                self.stacks[to-1].append(self.stacks[frm-1].pop())

        return self.format_answer()
    
    def solve2(self):
        self.reset()

        for nr, frm, to in self.moves:
            self.stacks[to - 1] += self.stacks[frm - 1][-nr:]
            del self.stacks[frm - 1][-nr:]

        return self.format_answer()


if __name__ == '__main__':
    s = Day05Solution(use_test_input=False)

    answer(s.solve1())
    answer(s.solve2())
    pruntime(_ST)


# Your puzzle answer was TDCHVHJTG.
# Your puzzle answer was NGCMPJLHV.



