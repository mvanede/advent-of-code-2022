from abc import ABC
from enum import Enum
from utils import Parser
from utils.lib import get_timer, answer, pruntime
from utils.base_solution import BaseSolution
_ST = get_timer()


class OUTCOME(Enum):
    WIN = 2
    DRAW = 0
    LOOSE = 1

    @property
    def score(self):
        if self == self.WIN:
            return 6
        if self == self.DRAW:
            return 3
        return 0


class RPS(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

    # Return the weaker shape (value-1)
    def weaker(self):
        return RPS((self.value - 1) % 3)

    # Return the stronger shape (value+1)
    def stronger(self):
        return RPS((self.value + 1) % 3)

    def outcome(self, other_shape):
        # 0 = draw
        # 1 = other_shape loses
        # 2 = other_shape wins
        return OUTCOME((other_shape.value - self.value) % 3)

    @property
    def score(self):
        return self.value + 1


class Day02Solution(BaseSolution, ABC):
    _input = "2022/day_02/day_02_input.txt"
    _test_input = "2022/day_02/day_02_test_input.txt"
    strategy = None

    def parse_input(self):
        self.strategy = Parser.split_by(self.read_input(), "\n", " ", conv_func=None)  # lambda x:int(x)

    @staticmethod
    def get_score1(p1, p2):
        shape1 = RPS('ABC'.index(p1))
        shape2 = RPS('XYZ'.index(p2))

        outcome = shape2.outcome(shape1)
        return shape2.score + outcome.score

    def solve1(self):
        scores = [self.get_score1(r[0], r[1]) for r in self.strategy]
        return sum(scores)

    @staticmethod
    def get_score2(p1, o1):
        # X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
        # Shuffled the array to get the according index
        outcome = OUTCOME('YXZ'.index(o1))
        shape1 = RPS('ABC'.index(p1))

        # Get the right shape, based on the outcome
        if outcome is OUTCOME.WIN:
            shape2 = shape1.stronger()
        elif outcome is OUTCOME.LOOSE:
            shape2 = shape1.weaker()
        else:
            shape2 = shape1

        return shape2.score + outcome.score

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


