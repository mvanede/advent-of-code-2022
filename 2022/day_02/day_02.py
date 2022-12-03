from abc import ABC

from utils import Parser
from utils.lib import get_timer, answer, pruntime
from utils.base_solution import BaseSolution
_ST = get_timer()


class Day02Solution(BaseSolution, ABC):
    _input = "2022/day_02/day_02_input.txt"
    _test_input = "2022/day_02/day_02_test_input.txt"
    strategy = None

    def parse_input(self):
        self.strategy = Parser.split_by(self.read_input(), "\n", " ", conv_func=None)  # lambda x:int(x)

    @staticmethod
    def get_score1(p1, p2):
        shape1 = 'ABC'.index(p1)
        shape2 = 'XYZ'.index(p2)
        diff = (shape2 - shape1) % 3

        # 1 = p2 win, # 2 = p2 loose, # 0 = draw. Shuffle a bit to get the score
        shape_score = (shape2 + 1)
        outcome_score = ((diff + 1) % 3) * 3
        return  shape_score + outcome_score

    def solve1(self):
        scores = [self.get_score1(r[0], r[1]) for r in self.strategy]
        return sum(scores)

    @staticmethod
    def get_score2(p1, outcome):
        # X = lose = 0, # Y  = draw = 1, # Z = win = 2
        shape1 = 'ABC'.index(p1)
        outcome1 = 'XYZ'.index(outcome)

        # Get the right shape, based on the outcome
        shape2 = (shape1 + (outcome1 -1)) % 3
        shape_score = (shape2 + 1)
        outcome_score = outcome1 * 3

        return shape_score + outcome_score

    def solve2(self):
        scores = [self.get_score2(r[0], r[1]) for r in self.strategy]
        return sum(scores)


if __name__ == '__main__':
    s = Day02Solution(use_test_input=False)
    answer(s.solve1())
    answer(s.solve2())
    pruntime(_ST)

# Your puzzle answer was 12645.
# Your puzzle answer was 11756.


