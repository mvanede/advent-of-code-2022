import json
from abc import ABC
from functools import cmp_to_key
from utils import Parser
from utils.lib import answer, ftimer
from utils.base_solution import BaseSolution
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(format="%(message)s", level=logging.INFO)


def ints_are_in_right_order(left, right):
    if left < right:
        logger.debug("Left side is smaller, return inputs are in RIGHT order")
        return True
    elif left > right:
        logger.debug("Right side is smaller, return inputs are NOT in right order")
        return False
    else:
        return None


def is_valid(left, right):
    logger.debug('COMPARE {} {}'.format(left, right))
    
    match left, right:
        case int(), int():
            return ints_are_in_right_order(left, right)
        case int(), list():
            return is_valid([left], right)
        case list(), int():
            return is_valid(left, [right])
        case list(), list():
            for i in range(min(len(left), len(right))):
                lft = left[i]
                rght = right[i]
    
                if (validity := is_valid(lft, rght)) is not None:
                    return validity
    
            if len(left) < len(right):
                logger.debug("Left side ran out of items, so inputs are in the RIGHT order")
                return True
            elif len(left) > len(right):
                logger.debug("Right side ran out of items, so inputs are NOT in the right order")
                return False
    return None


class Day13Solution(BaseSolution, ABC):
    _input = "2022/day_13/day_13.input.txt"
    _test_input = "2022/day_13/day_13_test.input.txt"

    def parse_input(self):
        self.pairs = Parser.split_by(self.read_input(), "\n\n","\n", conv_func=lambda x: json.loads(x))

    @ftimer
    def solve1(self):
        valid_pairs = []
        for idx, pair in enumerate(self.pairs):
            left, right = self.pairs[idx]
            if is_valid(left, right):
                valid_pairs.append(idx + 1)

        return sum(valid_pairs)
    
    @ftimer
    def solve2(self):
        divider_packet1 = [[2]]
        divider_packet2 = [[6]]
        
        all_pairs = [item for pair in self.pairs for item in pair]
        all_pairs.append(divider_packet1)
        all_pairs.append(divider_packet2)
        
        sorted_list = sorted(all_pairs, key=cmp_to_key(lambda item1, item2: -1 if is_valid(item1, item2) else 1))
        return (sorted_list.index(divider_packet1)+1 ) * (sorted_list.index(divider_packet2)+1)
    

if __name__ == '__main__':
    s = Day13Solution(use_test_input=False)
    answer(s.solve1())
    answer(s.solve2())

# Your puzzle answer was 5684.
# Your puzzle answer was 22932.

