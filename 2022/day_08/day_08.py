from abc import ABC
from utils import Parser, Grid
from utils.lib import get_timer, answer, pruntime
from utils.base_solution import BaseSolution

_ST = get_timer()


class Day08Solution(BaseSolution, ABC):
    _input = "2022/day_08/day_08.input.txt"
    _test_input = "2022/day_08/day_08_test.input.txt"
    MAX_TREE_HEIGHT = 9
    MIN_TREE_HEIGHT = 0

    def __init__(self, use_test_input):
        self.forrest = None
        super().__init__(use_test_input)

    def parse_input(self):
        self.forrest = Grid(Parser.split_by(self.read_input(), "\n", "", conv_func=lambda x: int(x)))

    def solve1(self):
        visible_count = 0
        for c in self.forrest.cells:
            max_up = max(self.forrest.get_above(c, view_direction=True) or [-1])
            max_down = max(self.forrest.get_below(c) or [-1])
            max_left = max(self.forrest.get_left_of(c, view_direction=True) or [-1])
            max_right = max(self.forrest.get_right_of(c) or [-1])

            tree_height = self.forrest.get(c.x, c.y)
            if tree_height > min(max_right, max_up, max_left, max_down):
                visible_count += 1
        return visible_count

    def get_scenic_score(self, c):
        col_idx, row_idx = c
        tree_height = self.forrest.get(col_idx, row_idx)

        up = self.forrest.get_above(c, view_direction=True)
        down = self.forrest.get_below(c)
        left = self.forrest.get_left_of(c, view_direction=True)
        right = self.forrest.get_right_of(c)

        total_score = 1
        for row in [up, down, left, right]:
            score = 0
            for u in row:
                score += 1
                if u >= tree_height:
                    break
            total_score *= score
        return total_score

    def solve2(self):
        max_score = 0
        for c in self.forrest.cells:
            sc = self.get_scenic_score(c)
            max_score = max(max_score, sc)
        return max_score


if __name__ == '__main__':
    s = Day08Solution(use_test_input=False)
    # s.forrest.print()

    answer(s.solve1())
    answer(s.solve2())
    pruntime(_ST)

# Your puzzle answer was 1845. 
# Your puzzle answer was 230112.