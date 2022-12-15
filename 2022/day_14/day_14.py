from abc import ABC
from utils import Parser, Grid
from utils.grid import Coord
from utils.lib import answer, ftimer
from utils.base_solution import BaseSolution


# CODE HERE
class Day14Solution(BaseSolution, ABC):
    _input = "2022/day_14/day_14.input.txt"
    _test_input = "2022/day_14/day_14_test.input.txt"

    def draw_cave_and_lines(self):
        self.cave = Grid.init_with(self.mx_x + 1, self.mx_y + 1, '.')

        for scanline in self.scanlines:
            start = scanline[0]

            for c in scanline[1:]:
                for x_idx in range(min(start.x, c.x), max(start.x, c.x) + 1):
                    for y_idx in range(min(start.y, c.y), max(start.y, c.y) + 1):
                        self.cave.set(x_idx, y_idx, '#')

                start = c
    @ftimer
    def parse_input(self):
        self.scanlines = Parser.split_by(self.read_input(), "\n", " -> ",
                                         conv_func=lambda x: Coord(int(x.split(',')[0]), int(x.split(',')[1])))

    @property
    def mx_x(self):
        return max([item.x for scanline in self.scanlines for item in scanline])

    @property
    def mx_y(self):
        return max([item.y for scanline in self.scanlines for item in scanline])

    def poor_sand(self, start_pos: Coord):
        v = self.cave.get2(start_pos.x, start_pos.y)
        if v == '0':
            return False

        try:
            if self.cave.get2(start_pos.x, start_pos.y + 1) == '.':
                return self.poor_sand(Coord(start_pos.x, start_pos.y + 1))
            elif self.cave.get2(start_pos.x - 1, start_pos.y + 1) == '.':
                return self.poor_sand(Coord(start_pos.x - 1, start_pos.y + 1))
            elif self.cave.get2(start_pos.x + 1, start_pos.y + 1) == '.':
                return self.poor_sand(Coord(start_pos.x + 1, start_pos.y + 1))
            elif self.cave.get2(start_pos.x, start_pos.y) != '0':
                return self.cave.set(start_pos.x, start_pos.y, '0')
            elif self.cave.get2(start_pos.x, start_pos.y) == '0':
                return False
        except Exception:
            # Out of bound, set the sand here
            return False

        return True

    @ftimer
    def solve1(self):
        self.draw_cave_and_lines()

        i = 0
        while self.poor_sand(Coord(500, 0)):
            i += 1

        return i

    @ftimer
    def solve2(self):
        mx_y = self.mx_y + 2
        mx_x = self.mx_x + mx_y
        self.scanlines.append([Coord(0, mx_y), Coord(mx_x, mx_y)])
        self.draw_cave_and_lines()

        i = 0
        while self.poor_sand(Coord(500, 0)):
            i += 1

        return i


if __name__ == '__main__':
    s = Day14Solution(use_test_input=False)
    answer(s.solve1())
    answer(s.solve2())

# Your puzzle answer was 715.
# Your puzzle answer was 25248.



