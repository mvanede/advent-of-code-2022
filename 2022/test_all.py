import sys
import pytest

from day_01 import Day01Solution
from day_02 import Day02Solution
from day_03 import Day03Solution
from day_04 import Day04Solution
from day_05 import Day05Solution
from day_06 import Day06Solution
from day_07 import Day07Solution
from day_08 import Day08Solution
from day_09 import Day09Solution
from day_10 import Day10Solution
from day_11 import Day11Solution
from day_12 import Day12Solution
from day_13 import Day13Solution
from day_14 import Day14Solution

def test_day_01():
    s = Day01Solution(use_test_input=False)
    assert s.solve1() == 71471
    assert s.solve2() == 211189


def test_day_02():
    s = Day02Solution(use_test_input=False)
    assert s.solve1() == 12645
    assert s.solve2() == 11756


def test_day_03():
    s = Day03Solution(use_test_input=False)
    assert s.solve1() == 7850
    assert s.solve2() == 2581


def test_day_04():
    s = Day04Solution(use_test_input=False)
    assert s.solve1() == 518
    assert s.solve2() == 909


def test_day_05():
    s = Day05Solution(use_test_input=False)
    assert s.solve1() == 'TDCHVHJTG'
    assert s.solve2() == 'NGCMPJLHV'


def test_day_06():
    s = Day06Solution(use_test_input=False)
    assert s.solve1() == 1987
    assert s.solve2() == 3059


def test_day_07():
    s = Day07Solution(use_test_input=False)
    assert s.solve1() == 1086293
    assert s.solve2() == 366028


def test_day_08():
    s = Day08Solution(use_test_input=False)
    assert s.solve1() == 1845
    assert s.solve2() == 230112


def test_day_09():
    s = Day09Solution(use_test_input=False)
    assert s.solve1() == 6384
    assert s.solve2() == 2734


def test_day_10():
    s = Day10Solution(use_test_input=False)
    assert s.solve1() == 14820
    s2 = s.solve2()
    assert s2[0:40] == '###..####.####.#..#.####.####.#..#..##..'
    assert s2[40:80] == '#..#....#.#....#.#..#....#....#..#.#..#.'
    assert s2[80:120] == '#..#...#..###..##...###..###..####.#..#.'
    assert s2[120:160] == '###...#...#....#.#..#....#....#..#.####.'
    assert s2[160:200] == '#.#..#....#....#.#..#....#....#..#.#..#.'
    assert s2[200:240] == '#..#.####.####.#..#.####.#....#..#.#..#.'


def test_day_11():
    s = Day11Solution(use_test_input=False)
    assert s.solve1() == 55930
    assert s.solve2() == 14636993466


def test_day_12():
    s = Day12Solution(use_test_input=False)
    assert s.solve1() == 352
    assert s.solve2() == 345


def test_day_13():
    s = Day13Solution(use_test_input=False)
    assert s.solve1() == 5684
    assert s.solve2() == 22932

def test_day_14():
    s = Day14Solution(use_test_input=False)
    assert s.solve1() == 715
    assert s.solve2() == 25248


if __name__ == '__main__':
    sys.exit(pytest.main(["-k", "test_all"]))
