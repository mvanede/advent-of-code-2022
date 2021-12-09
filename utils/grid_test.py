import unittest
from utils import grid


class MyTestCase(unittest.TestCase):
    _alpha_grid_common_input = [['a', 'a', 'c'], ['a', 'e', 'f'], ['g', 'h', 'i']]
    _alpha_grid_rotate_input = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    _int_grid_common_input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    """
    Properties
    """
    def test_dimensions(self):
        grid_under_test = grid.Grid(self._alpha_grid_common_input)
        self.assertEqual(3, grid_under_test.width)
        self.assertEqual(3, grid_under_test.height)

    """
    GET methods
    """
    def test_get(self):
        grid_under_test = grid.Grid(self._alpha_grid_common_input)
        self.assertEqual('a', grid_under_test.get(0, 0))
        self.assertEqual('e', grid_under_test.get(1, 1))
        self.assertEqual('i', grid_under_test.get(2, 2))

    def test_get_row(self):
        grid_under_test = grid.Grid(self._alpha_grid_common_input)
        self.assertEqual(self._alpha_grid_common_input[0], grid_under_test.get_row(0))
        self.assertEqual(self._alpha_grid_common_input[2], grid_under_test.get_row(2))

    def test_get_col(self):
        grid_under_test = grid.Grid(self._alpha_grid_common_input)
        self.assertEqual(['a', 'a', 'g'], grid_under_test.get_col(0))
        self.assertEqual(['c', 'f', 'i'], grid_under_test.get_col(2))

    """
    MOST AND LEAST COMMON methods
    """
    def test_most_common_in_row(self):
        grid_under_test = grid.Grid(self._alpha_grid_common_input)
        self.assertEqual(('a', 2), grid_under_test.get_most_common_in_row(0))
        self.assertRaises(grid.NoMostCommonException, lambda: grid_under_test.get_most_common_in_row(1))

    def test_least_common_in_row(self):
        grid_under_test = grid.Grid(self._alpha_grid_common_input)
        self.assertEqual(('c', 1), grid_under_test.get_least_common_in_row(0))
        self.assertRaises(grid.NoLeastCommonException, lambda: grid_under_test.get_least_common_in_row(1))

    def test_most_common_in_col(self):
        grid_under_test = grid.Grid(self._alpha_grid_common_input)
        self.assertEqual(('a', 2), grid_under_test.get_most_common_in_col(0))
        self.assertRaises(grid.NoMostCommonException, lambda: grid_under_test.get_most_common_in_col(1))

    def test_least_common_in_col(self):
        grid_under_test = grid.Grid(self._alpha_grid_common_input)
        self.assertEqual(('g', 1), grid_under_test.get_least_common_in_col(0))
        self.assertRaises(grid.NoLeastCommonException, lambda: grid_under_test.get_least_common_in_col(1))

    def test_most_common(self):
        grid_under_test = grid.Grid(self._alpha_grid_common_input)
        self.assertEqual(('a', 3), grid_under_test.get_most_common())
        g = grid.Grid([['a', 'b'], ['b', 'a']])
        self.assertRaises(grid.NoMostCommonException, lambda: g.get_most_common())

    def test_least_common(self):
        grid_under_test = grid.Grid(self._alpha_grid_common_input)
        g = grid.Grid([['a', 'b'], ['b', 'b']])
        self.assertEqual(('a', 1), g.get_least_common())
        self.assertRaises(grid.NoLeastCommonException, lambda: grid_under_test.get_least_common())

    """
        ROTATE methods
    """
    def test_rotate_cw(self):
        grid_under_test = grid.Grid(self._alpha_grid_rotate_input)
        grid_under_test.rotate_cw()
        self.assertEqual(['g', 'd', 'a'], grid_under_test.get_row(0))
        self.assertEqual(['h', 'e', 'b'], grid_under_test.get_row(1))
        self.assertEqual(['i', 'f', 'c'], grid_under_test.get_row(2))

        grid_under_test.rotate_cw()
        self.assertEqual(['i', 'h', 'g'], grid_under_test.get_row(0))
        self.assertEqual(['f', 'e', 'd'], grid_under_test.get_row(1))
        self.assertEqual(['c', 'b', 'a'], grid_under_test.get_row(2))

    def test_rotate_ccw(self):
        grid_under_test = grid.Grid(self._alpha_grid_rotate_input)
        grid_under_test.rotate_ccw()
        self.assertEqual(['c', 'f', 'i'], grid_under_test.get_row(0))
        self.assertEqual(['b', 'e', 'h'], grid_under_test.get_row(1))
        self.assertEqual(['a', 'd', 'g'], grid_under_test.get_row(2))

        grid_under_test.rotate_ccw()
        self.assertEqual(['i', 'h', 'g'], grid_under_test.get_row(0))
        self.assertEqual(['f', 'e', 'd'], grid_under_test.get_row(1))
        self.assertEqual(['c', 'b', 'a'], grid_under_test.get_row(2))

    def test_flip_horizontal(self):
        grid_under_test = grid.Grid(self._alpha_grid_rotate_input)
        grid_under_test.flip_horizontal()
        self.assertEqual(['g', 'h', 'i'], grid_under_test.get_row(0))
        self.assertEqual(['d', 'e', 'f'], grid_under_test.get_row(1))
        self.assertEqual(['a', 'b', 'c'], grid_under_test.get_row(2))

    def test_flip_vertical(self):
        grid_under_test = grid.Grid(self._alpha_grid_rotate_input)
        grid_under_test.flip_vertical()
        self.assertEqual(['c', 'b', 'a'], grid_under_test.get_row(0))
        self.assertEqual(['f', 'e', 'd'], grid_under_test.get_row(1))
        self.assertEqual(['i', 'h', 'g'], grid_under_test.get_row(2))

    """
    SUM AND PRODUCT methods
    """
    def test_row_sum(self):
        grid_under_test = grid.Grid(self._int_grid_common_input)
        self.assertEqual(6, grid_under_test.get_row_sum(0))
        self.assertEqual(15, grid_under_test.get_row_sum(1))
        self.assertEqual(24, grid_under_test.get_row_sum(2))

    def test_col_sum(self):
        grid_under_test = grid.Grid(self._int_grid_common_input)
        self.assertEqual(12, grid_under_test.get_col_sum(0))
        self.assertEqual(15, grid_under_test.get_col_sum(1))
        self.assertEqual(18, grid_under_test.get_col_sum(2))

    def test_sum(self):
        grid_under_test = grid.Grid(self._int_grid_common_input)
        self.assertEqual(45, grid_under_test.get_sum())

    def test_row_prod(self):
        grid_under_test = grid.Grid(self._int_grid_common_input)
        self.assertEqual(6, grid_under_test.get_row_prod(0))
        self.assertEqual(120, grid_under_test.get_row_prod(1))
        self.assertEqual(504, grid_under_test.get_row_prod(2))

    def test_col_prod(self):
        grid_under_test = grid.Grid(self._int_grid_common_input)
        self.assertEqual(28, grid_under_test.get_col_prod(0))
        self.assertEqual(80, grid_under_test.get_col_prod(1))
        self.assertEqual(162, grid_under_test.get_col_prod(2))

    def test_prod(self):
        grid_under_test = grid.Grid(self._int_grid_common_input)
        self.assertEqual(362_880, grid_under_test.get_prod())

    def test_add(self):
        grid_under_test = grid.Grid(self._int_grid_common_input)
        self.assertEqual(7, grid_under_test.add_at(1, 1, 2).get(1,1))

    def test_substract(self):
        grid_under_test = grid.Grid(self._int_grid_common_input)
        self.assertEqual(3, grid_under_test.substract_at(1, 1, 2).get(1,1))

    """
    REPLACE methods
    """
    def test_replace_in_row(self):
        grid_under_test = grid.Grid(self._alpha_grid_common_input)
        grid_under_test.replace_in_row(0, 'a', 'Z')
        self.assertEqual(['Z', 'Z', 'c'], grid_under_test.get_row(0))
        self.assertEqual(['a', 'e', 'f'], grid_under_test.get_row(1))
        self.assertEqual(['g', 'h', 'i'], grid_under_test.get_row(2))

    def test_replace_in_col(self):
        grid_under_test = grid.Grid(self._alpha_grid_common_input)
        grid_under_test.replace_in_col(0, 'a', 'Z')
        self.assertEqual(['Z', 'a', 'c'], grid_under_test.get_row(0))
        self.assertEqual(['Z', 'e', 'f'], grid_under_test.get_row(1))
        self.assertEqual(['g', 'h', 'i'], grid_under_test.get_row(2))

    def test_replace(self):
        grid_under_test = grid.Grid(self._alpha_grid_common_input)
        grid_under_test.replace_all('a', 'Z')
        self.assertEqual(['Z', 'Z', 'c'], grid_under_test.get_row(0))
        self.assertEqual(['Z', 'e', 'f'], grid_under_test.get_row(1))
        self.assertEqual(['g', 'h', 'i'], grid_under_test.get_row(2))

    """
    FINDING AND ADJACENT
    """
    def test_adjacent_diagonal(self):
        grid_under_test = grid.Grid(self._alpha_grid_rotate_input)
        self.assertEqual(['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i'], list(grid_under_test.get_adjacent(1,1).values()))
        self.assertEqual(['b', 'd', 'e'], list(grid_under_test.get_adjacent(0, 0).values()))
        self.assertEqual(['b','c', 'e', 'h', 'i'], list(grid_under_test.get_adjacent(2, 1).values()))

    def test_adjacent_exclude_diagonal(self):
        grid_under_test = grid.Grid(self._alpha_grid_rotate_input)
        self.assertEqual(['b', 'd', 'f', 'h'], list(grid_under_test.get_adjacent(1,1, False).values()))
        self.assertEqual(['b', 'd' ], list(grid_under_test.get_adjacent(0, 0, False).values()))
        self.assertEqual(['c', 'e', 'i'], list(grid_under_test.get_adjacent(2, 1, False).values()))

    def test_find_all(self):
        grid_under_test = grid.Grid(self._alpha_grid_common_input)
        self.assertEqual([(0, 0), (1, 0), (0, 1)], grid_under_test.find_all('a'))
        self.assertEqual([(2, 2)], grid_under_test.find_all('i'))
        self.assertEqual([], grid_under_test.find_all('foobar'))


if __name__ == '__main__':
    unittest.main()
