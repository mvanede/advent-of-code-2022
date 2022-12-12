import copy
from abc import ABC
from functools import reduce
from utils import Parser
from utils.lib import get_timer, answer, pruntime
from utils.base_solution import BaseSolution

_ST = get_timer()


class Monkey:
    def __init__(self, starting_items, operation, test, throw_to):
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.throw_to = throw_to
        self.nr_of_inspections = 0


class Day11Solution(BaseSolution, ABC):
    _input = "2022/day_11/day_11.input.txt"
    _test_input = "2022/day_11/day_11_test.input.txt"

    @staticmethod
    def parse_block_to_monkey(block):
        starting_items = [int(x) for x in block[1].strip()[16:].split(', ')]
        operation = eval('lambda old: ' + block[2].strip()[17:])
        test = int(block[3].strip()[19:])
        if_true = int(block[4].strip()[25:])
        if_false = int(block[5].strip()[26:])
        return Monkey(starting_items=starting_items, operation=operation, test=test, throw_to=[if_true, if_false])
        
    def parse_input(self):
        blocks = Parser.split_by(self.read_input(), "\n\n", "\n", conv_func=None)
        self.monkeys = []
        for block in blocks:
                self.monkeys.append(self.parse_block_to_monkey(block))

    def solve(self, nr_of_rounds, func_new_worry=None):
        monkeys = copy.deepcopy((self.monkeys))
        for _ in range(nr_of_rounds):
            for m in monkeys:
                for idx, item in enumerate(m.items):
                    m.nr_of_inspections += 1
                    new_worry_level = func_new_worry(m.operation(item))
                    if_true, if_false = m.throw_to
                    throw_to = if_true if new_worry_level % m.test == 0 else if_false
                    monkeys[throw_to].items.append(new_worry_level)
                        
                m.items = []

        x = [m.nr_of_inspections for m in monkeys]
        x.sort()
        return x.pop() * x.pop()

    def solve1(self):
        return self.solve(nr_of_rounds=20,  func_new_worry = lambda x: x // 3)
    
    def solve2(self):
        modulo_all = reduce((lambda x, y: x * y), [m.test for m in self.monkeys])
        return self.solve(nr_of_rounds=10000,  func_new_worry = lambda x: x % modulo_all)


if __name__ == '__main__':
    s = Day11Solution(use_test_input=False)
    answer(s.solve1())
    answer(s.solve2())
    pruntime(_ST)


# Your puzzle answer was 55930.
# Your puzzle answer was 14636993466
