from abc import ABC
from utils import Parser, Grid
from utils.lib import get_timer, answer, pruntime
from utils.base_solution import BaseSolution

_ST = get_timer()


class Day08Solution(BaseSolution, ABC):
    _input = "2022/day_08/day_08_input.txt"
    _test_input = "2022/day_08/day_08_test_input.txt"
    MAX_TREE_HEIGHT = 9
    MIN_TREE_HEIGHT = 0

    def __init__(self, use_test_input):
        self.forrest = None
        super().__init__(use_test_input)

    def parse_input(self):
        self.forrest = Grid(Parser.split_by(self.read_input(), "\n", "", conv_func=lambda x: int(x)))

    @staticmethod
    def visible(row_idx, lst):
        visible_trees = []
        tallest = Day08Solution.MIN_TREE_HEIGHT-1

        for col_idx, tree in lst:
            if tree > tallest:
                tallest = tree
                visible_trees.append((col_idx, row_idx))

            # Once we reached the heighest tree, we're done with this row
            if tallest == Day08Solution.MAX_TREE_HEIGHT:
                break

        return visible_trees

    @staticmethod
    def visible_from_left(row_idx, row):
        return Day08Solution.visible(row_idx, enumerate(row))

    @staticmethod
    def visible_from_right(row_idx, row):
        lst = reversed(list(enumerate(row)))
        return Day08Solution.visible(row_idx, lst)

    @staticmethod
    def visible_from_top(col_idx, col):
        # we can reuse this, but we need to swap the x & y coordinates
        return [point[::-1] for point in Day08Solution.visible_from_right(col_idx, col)]

    @staticmethod
    def visible_from_bottom(col_idx, col):
        # we can reuse this, but we need to swap the x & y coordinates
        return [point[::-1] for point in Day08Solution.visible_from_left(col_idx, col)]

    def solve1(self): 
        visible = []

        for row_idx, row in enumerate(self.forrest.rows):
            visible += self.visible_from_left(row_idx, row)
            visible += self.visible_from_right(row_idx, row)

        for col_idx, col in enumerate(self.forrest.cols):
            visible += self.visible_from_top(col_idx, col)
            visible += self.visible_from_bottom(col_idx, col)

        # Return set of unique trees
        return len(set(visible))

    def get_scenic_score(self, c):
        col_idx, row_idx = c
        tree = self.forrest.get(col_idx, row_idx)

        up = self.forrest.get_above(c, view_direction=True)
        down = self.forrest.get_below(c)
        left = self.forrest.get_left_of(c, view_direction=True)
        right = self.forrest.get_right_of(c)

        total_score = 1
        for row in [up, down, left, right]:
            score = 0
            for u in row:
                score += 1
                if u >= tree:
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