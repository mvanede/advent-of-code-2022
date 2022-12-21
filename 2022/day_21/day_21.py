import copy
from abc import ABC
from collections import deque
from utils import Parser
from utils.lib import answer, ftimer
from utils.base_solution import BaseSolution


OPS = {
    '-': lambda a, b: a-b,
    '+': lambda a, b: a+b,
    '/': lambda a, b: a//b,
    '*': lambda a, b: a*b
}

REVERSE_OPS = {
    '-': (lambda a, b: a+b, lambda a, b: b-a),
    '+': (lambda a, b: a-b, lambda a, b: a-b),
    '/': (lambda a, b: a*b, lambda a, b: b+a),
    '*': (lambda a, b: a//b, lambda a, b: a//b)
}


def reverse_calculate(formula, value):
    if formula is None:
        return value
    else:
        v1, op, v2 = formula
        reversefunc1, reversefunc2 = REVERSE_OPS.get(op)
        match calculate(v1), calculate(v2):
            case leftvalue, None:
                return reverse_calculate(v2, reversefunc2(value, leftvalue))
            case None, rightvalue:
                return reverse_calculate(v1, reversefunc1(value, rightvalue))
    
def calculate(formula):
    if type(formula) is list:
        v1, op, v2 = formula
        func = OPS.get(op)
        leftvalue, rightvalue = calculate(v1), calculate(v2)
        
        if leftvalue is None or rightvalue is None:
            return None
        return func(leftvalue, rightvalue)
    else:
        return formula
    
# CODE HERE
class Day21Solution(BaseSolution, ABC):
    _input = "2022/day_21/day_21.input.txt"
    _test_input = "2022/day_21/day_21_test.input.txt"

    def parse_input(self):
        self.lines = Parser.split_by(self.read_input(), "\n",": ", " ",  conv_func=lambda x:int(x) if x.isdigit() else x  )  # lambda x:int(x)

    def build_formulas(self, lines):
        cache = {}
        # Build all formulas recursively
        heap = deque(lines)
        while len(heap):
            var, val = heap.popleft()
            if isinstance(val, str):
                cache[var[0]] = val
            elif val == None:
                cache[var[0]] = None
            elif len(val) == 1:
                cache[var[0]] = val[0]
            elif len(val) == 3 and val[0] in cache and val[2] in cache:
                cache[var[0]] = [cache[val[0]], val[1], cache[val[2]]]
            else:
                heap.append([var, val])
        return cache
    
    @ftimer
    def solve1(self):
        cache = self.build_formulas(self.lines)
        return calculate(cache['root'])
        
    
    @ftimer
    def solve2(self):
        lines = copy.deepcopy(self.lines)
        
        # Root element
        root_el = [(var, val) for var, val in lines if var[0] == 'root'][0]
        left_side_of_equation = root_el[1][0]
        right_side_of_equation = root_el[1][2]
        
        # Change 'our' monkey
        humn_el = [[var, val] for var, val in lines if var[0] == 'humn'][0]
        lines[lines.index(humn_el)] = [humn_el[0], None]
        cache = self.build_formulas(lines)

        # Only one of the parts contain 'our' monkey and cannot be calculated yet. The other side can be calculated to a number
        match calculate(cache[left_side_of_equation]), calculate(cache[right_side_of_equation]):
            case leftvalue, None:
                return reverse_calculate(cache[right_side_of_equation], leftvalue)
            case None, rightvalue:
                return reverse_calculate(cache[left_side_of_equation], rightvalue)


if __name__ == '__main__':
    s = Day21Solution(use_test_input=False)
    answer(s.solve1())
    answer(s.solve2())


# Your puzzle answer was 276156919469632.
# Your puzzle answer was 3441198826073.

