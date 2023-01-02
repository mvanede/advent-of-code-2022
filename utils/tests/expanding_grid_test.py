import unittest
from utils import ExpandingGrid

class ExpandingGridTestCase(unittest.TestCase):


    def test_expand_with_right(self):
        grid_under_test = ExpandingGrid(1,1, '.')
        grid_under_test.set_default_value('!')
        self.assertEqual('.', grid_under_test.get(0,0))

        grid_under_test.expand_with(1,1)
        self.assertEqual(2, len(grid_under_test.rows))
        self.assertEqual(2, len(grid_under_test.cols))
        self.assertEqual('.', grid_under_test.get(0,0))
        self.assertEqual('!', grid_under_test.get(1, 1))

    def test_expand_with_left(self):
        grid_under_test = ExpandingGrid(1, 1, '.')
        grid_under_test.set_default_value('!')
        self.assertEqual('.', grid_under_test.get(0, 0))

        grid_under_test.expand_with(-1, -1)
        self.assertEqual(2, len(grid_under_test.rows))
        self.assertEqual(2, len(grid_under_test.cols))
        self.assertEqual('!', grid_under_test.get(0, 0))
        self.assertEqual('.', grid_under_test.get(1, 1))

    def test_set_right(self):
        grid_under_test = ExpandingGrid(1, 1, '.')
        grid_under_test.print()
        grid_under_test.set(1, 0, '!')

        grid_under_test.print()

        self.assertEqual('.', grid_under_test.get(0, 0))
        self.assertEqual('!', grid_under_test.get(1, 0))

    def test_set_bottom(self):
        grid_under_test = ExpandingGrid(1, 1, '.')
        grid_under_test.set(0 , 1, '!')

        self.assertEqual('.', grid_under_test.get(0, 0))
        self.assertEqual('!', grid_under_test.get(0, 1))

    def test_set_left(self):
        grid_under_test = ExpandingGrid(1, 1, '.')
        grid_under_test.set(-1 ,0, '!')
        self.assertEqual('!', grid_under_test.get(0, 0))
        self.assertEqual('.', grid_under_test.get(1, 0))

    def test_set_top(self):
        grid_under_test = ExpandingGrid(1, 1, '.')
        grid_under_test.set(0 , -1, '!')

        self.assertEqual('!', grid_under_test.get(0, 0))
        self.assertEqual('.', grid_under_test.get(0, 1))

    def test_set_topleft(self):
        grid_under_test = ExpandingGrid(1, 1, '.')
        grid_under_test.set(-2 , -2, '!')
        grid_under_test.print()

        self.assertEqual(3, len(grid_under_test.rows))
        self.assertEqual(3, len(grid_under_test.rows))

        self.assertEqual('!', grid_under_test.get(0, 0))

    def test_set_bottom_left(self):
        grid_under_test = ExpandingGrid(1, 1, '.')
        grid_under_test.set(-2 , 2, '!')

        self.assertEqual(3, len(grid_under_test.rows))
        self.assertEqual(3, len(grid_under_test.rows))

        self.assertEqual('!', grid_under_test.get(0, 2))


if __name__ == '__main__':
    unittest.main()
