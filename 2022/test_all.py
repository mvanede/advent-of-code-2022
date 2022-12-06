import unittest
from day_01 import Day01Solution
from day_02 import Day02Solution
from day_03 import Day03Solution
from day_04 import Day04Solution
from day_05 import Day05Solution
from day_06 import Day06Solution

class AoCTestCase(unittest.TestCase):

    def test_day_01(self):
        s = Day01Solution(use_test_input=False)
        assert s.solve1() == 71471
        assert s.solve2() == 211189

    def test_day_02(self):
        s = Day02Solution(use_test_input=False)
        assert s.solve1() == 12645
        assert s.solve2() == 11756

    def test_day_03(self):
        s = Day03Solution(use_test_input=False)
        assert s.solve1() == 7850
        assert s.solve2() == 2581

    def test_day_04(self):
        s = Day04Solution(use_test_input=False)
        assert s.solve1() == 518
        assert s.solve2() == 909
        
    def test_day_05(self):
        s = Day05Solution(use_test_input=False)
        assert s.solve1() == 'TDCHVHJTG'
        assert s.solve2() == 'NGCMPJLHV'
        
    def test_day_06(self):
        s = Day06Solution(use_test_input=False)
        assert s.solve1() == 1987
        assert s.solve2() == 3059


if __name__ == '__main__':
    unittest.main()
