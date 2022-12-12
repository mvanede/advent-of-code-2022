import math
from abc import ABC
from utils import Parser, Grid
from utils.lib import get_timer, answer, pruntime
from utils.base_solution import BaseSolution

_ST = get_timer()


class Solve1Grid(Grid):
    def custom_cost_func(self, coord):
        return 1

    def custom_allow_func(self, current, neighbour):
        return self.get(neighbour) - self.get(current) <= 1
    

# CODE HERE
class Day12Solution(BaseSolution, ABC):
    _input = "2022/day_12/day_12.input.txt"
    _test_input = "2022/day_12/day_12_test.input.txt"

    def parse_input(self):
        self.grid_input = Parser.split_by(self.read_input(), "\n", "", conv_func=lambda x: ord(x))

    def solve1(self):
        grid = Solve1Grid(self.grid_input)

        start = grid.find_all(ord('S'))[0]
        end = grid.find_all(ord('E'))[0]

        # Set start/end position to actual value
        grid.set(start.x, start.y, ord('a'))
        grid.set(end.x, end.y, ord('z'))

        cost, path = grid.dijkstra2(start, end, custom_cost_func=Solve1Grid.custom_cost_func,
                             custom_allow_func=Solve1Grid.custom_allow_func)
        return len(path) - 1

    def solve2(self):
        grid = Solve1Grid(self.grid_input)

        start = grid.find_all(ord('S'))[0]
        end = grid.find_all(ord('E'))[0]

        # Set start/end position to actual value
        grid.set(start.x, start.y, ord('a'))
        grid.set(end.x, end.y, ord('z'))
        
        all_possible = grid.find_all(ord('a'))
        
        minlen = math.inf
        for idx, ps in enumerate(all_possible):
            cost, path = grid.dijkstra2(ps, end, custom_cost_func=Solve1Grid.custom_cost_func,
                             custom_allow_func=Solve1Grid.custom_allow_func)
            if path:
                if len(path) > 1:
                    minlen = min(minlen, len(path) - 1)
        return minlen


if __name__ == '__main__':
    s = Day12Solution(use_test_input=False)
    answer(s.solve1())
    pruntime(_ST)
    answer(s.solve2())
    pruntime(_ST)

# Your puzzle answer was 352.
# Your puzzle answer was 345.
