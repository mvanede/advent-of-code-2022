from abc import ABC
from utils import Parser
from utils.lib import answer, ftimer
from utils.base_solution import BaseSolution

SNAFUBASE = 5
SNAFUDIGITS = {'-': '-1', '=': '-2'}
REV_SNAFUDIGITS = dict(reversed(item) for item in SNAFUDIGITS.items())


def convert_to_snafu(decimal_number):
    new_digits = []
    while decimal_number > 0:
        remainder = (decimal_number % SNAFUBASE)
        decimal_number = decimal_number // SNAFUBASE
        if remainder > 2:
            new_digits.append(REV_SNAFUDIGITS[str(remainder - SNAFUBASE)])
            decimal_number += 1
        else:
            new_digits.append(str(remainder))

    return ''.join(new_digits[::-1])


def convert_from_snafu(snafu_number):
    decimal_sum  = 0
    for idx, char in enumerate(snafu_number[::-1]):
        number = int(char) if char.isdigit() else int(SNAFUDIGITS[char])
        decimal_sum += (SNAFUBASE ** idx) * number
    return decimal_sum


class Day25Solution(BaseSolution, ABC):
    _input = "2022/day_25/day_25.input.txt"
    _test_input = "2022/day_25/day_25_test.input.txt"

    def parse_input(self):
        self.snafu_numbers = Parser.split_by(self.read_input(), "\n", conv_func=None)

    @ftimer
    def solve1(self):
        total = sum([convert_from_snafu(s) for s in self.snafu_numbers])
        return convert_to_snafu(total)


if __name__ == '__main__':
    s = Day25Solution(use_test_input=False)
    answer(s.solve1())

# Your puzzle answer was 2=01-0-2-0=-0==-1=01.