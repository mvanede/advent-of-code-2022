from abc import ABC

from utils import Parser
from utils.lib import get_timer, answer, pruntime
from utils.base_solution import BaseSolution

_ST = get_timer()


class Dir():
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.subdirs = {}
        self.files = {}
        self.sum = 0


class Day07Solution(BaseSolution, ABC):
    _input = "2022/day_07/day_07_input.txt"
    _test_input = "2022/day_07/day_07_test_input.txt"
    basedir = Dir('/')

    def __init__(self, use_test_input):
        self.use_test_input = use_test_input
        self.all_dirs = None
        self.parse_input()

    def parse_input(self):
        commands = Parser.split_by(self.read_input(), "\n", conv_func=None)  # lambda x:int(x)
        commands.reverse() # so we can pop

        current_dir = self.basedir
        self.all_dirs = [self.basedir]

        while commands:
            c = commands.pop()

            if c.startswith('$ cd'):
                goto = c[5:]
                if goto == '..':
                    current_dir = current_dir.parent
                else:
                    current_dir = current_dir.subdirs[goto]
            elif c.startswith('$ ls'):
                # Read the next lines while there are and while next line is not a new command ('$')
                while commands and not commands[-1].startswith('$'):
                    nxt = commands.pop()
                    c, val = nxt.split(' ')
                    if c == 'dir':
                        # Create a new directory and add it to current
                        new_dir = Dir(name=val, parent=current_dir)
                        current_dir.subdirs[val] = new_dir
                        self.all_dirs.append(new_dir)
                    else:
                        # add files to directory
                        current_dir.files[val] = int(c)

        # Recursively calculate the sum of all files in all directories
        self.calculate_sum(self.basedir)

    def calculate_sum(self, dir):
        if not dir.subdirs:
            dir.sum = sum(dir.files.values())
        else:
            sums_subdirs = [self.calculate_sum(subdir) for subdir in dir.subdirs.values()]
            dir.sum = sum(dir.files.values()) + sum(sums_subdirs)
        return dir.sum

    def solve1(self):
        return sum([d.sum for d in self.all_dirs if d.sum < 100000])

    def solve2(self):
        diskspice_to_gain = 30000000 - (70000000 - self.basedir.sum)
        return min([d.sum for d in self.all_dirs if d.sum >= diskspice_to_gain])


if __name__ == '__main__':
    s = Day07Solution(use_test_input=False)
    answer(s.solve1())
    answer(s.solve2())
    pruntime(_ST)

# Your puzzle answer was 1086293.
# Your puzzle answer was 366028.