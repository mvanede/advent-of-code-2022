from abc import ABC
from utils import Parser, ExpandingGrid
from utils.lib import get_timer, answer, pruntime
from utils.base_solution import BaseSolution
from utils.position import Position

_ST = get_timer()


class Knot (Position):
    def __init__(self, x=0, y=0):
        super().__init__(x, y, True)

    def move_to(self, other):
        xdiff = other.x - self.x
        ydiff = other.y - self.y
        distance = abs(xdiff) + abs(ydiff)

        # assumption manhattan distance will never be > 4 (2 diagonal steps)
        if distance >= 3:
            # Move diagonal
            self.x += 1 if xdiff > 0 else -1
            self.y += 1 if ydiff > 0 else -1
        elif abs(xdiff) == 2:
            # Move horizontal
            self.x += 1 if xdiff > 0 else -1
        elif abs(ydiff) == 2:
            # Move vertical
            self.y += 1 if ydiff > 0 else -1


# CODE HERE
class Day09Solution(BaseSolution, ABC):
    _input = "2022/day_09/day_09.input.txt"
    _test_input = "2022/day_09/day_09_test.input.txt"

    def parse_input(self):
        self.grid = ExpandingGrid(8, 8, default_value='.')
        self.moves = Parser.split_by(self.read_input(), "\n", " ", conv_func=None)  # lambda x:int(x)

    def execute(self, rope):
        marked = [rope[len(rope) - 1].tuple]

        for idx, m in enumerate(self.moves):
            direction, steps = m
            
            # Move nr of steps into this direction, after each step, move rest of the rope
            for i in range(int(steps)):
                head = rope[0]
                head.move_dir(direction, 1)
                
                for idx, knot in enumerate(rope):
                    if idx == 0:
                        continue

                    predecessor = rope[idx - 1]
                    knot.move_to(predecessor)
                    
                    # Store position of the tail
                    if idx == len(rope) - 1:
                        marked.append(knot.tuple)

        return len(set(marked))

    def solve1(self):
        rope = [
            Knot(0, self.grid.height - 1),  # head
            Knot(0, self.grid.height - 1)
        ]
        return self.execute(rope)

    def solve2(self):
        rope = [
            Knot(0, self.grid.height - 1), # head
            Knot(0, self.grid.height - 1),
            Knot(0, self.grid.height - 1),
            Knot(0, self.grid.height - 1),
            Knot(0, self.grid.height - 1),
            Knot(0, self.grid.height - 1),
            Knot(0, self.grid.height - 1),
            Knot(0, self.grid.height - 1),
            Knot(0, self.grid.height - 1),
            Knot(0, self.grid.height - 1)
        ]
        return self.execute(rope)


if __name__ == '__main__':
    s = Day09Solution(use_test_input=False)
    answer(s.solve1())
    answer(s.solve2())
    pruntime(_ST)

# ANSWER: 6384
# ANSWER: 2734
