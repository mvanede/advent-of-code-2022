from collections import Counter
import math

class NoMostCommonException(Exception):
    pass


class NoLeastCommonException(Exception):
    pass


class Grid:
    _grid = [[]]

    def __init__(self, grid: [[]]):
        self._grid = grid

    @property
    def height(self):
        return len(self._grid)

    @property
    def width(self):
        return len(self._grid[0])

    @property
    def rows(self):
        return self._grid

    @property
    def cols(self):
        return [list(col) for col in (list(zip(*self._grid)))]
    """
    GET methods
    """
    def get(self, row_idx:int, col_idx:int):
        return self._grid[row_idx][col_idx]

    def get_row(self, row_idx:int):
        return self._grid[row_idx]

    def get_col(self, col_idx:int):
        return [row[col_idx] for row in self._grid]
        #return list(list(zip(*self._grid))[col_idx])

    """
    MOST AND LEAST COMMON methods
    """
    def get_most_common_in_row(self, row_idx:int):
        data = Counter(self._grid[row_idx]).most_common(2)
        if data[0][1] == data[1][1]:
            raise NoMostCommonException
        return data[0]

    def get_least_common_in_row(self, row_idx:int):
        data = Counter(self._grid[row_idx]).most_common()
        data.reverse()

        if data[0][1] == data[1][1]:
            raise NoLeastCommonException
        return data[0]

    def get_most_common_in_col(self, col_idx:int):
        data = Counter(self.get_col(col_idx)).most_common(2)
        if data[0][1] == data[1][1]:
            raise NoMostCommonException
        return data[0]

    def get_least_common_in_col(self, col_idx:int):
        data = Counter(self.get_col(col_idx)).most_common()
        data.reverse()

        if data[0][1] == data[1][1]:
            raise NoLeastCommonException
        return data[0]

    def get_most_common(self):
        data = Counter(self._flatten()).most_common(2)
        if data[0][1] == data[1][1]:
            raise NoMostCommonException
        return data[0]

    def get_least_common(self):
        data = Counter(self._flatten()).most_common()
        data.reverse()

        if data[0][1] == data[1][1]:
            raise NoLeastCommonException
        return data[0]

    def rotate_cw(self):
        self._grid = [list(row) for row in zip(*reversed(self._grid))]
        return self

    def rotate_ccw(self):
        ccw = [list(r[::-1]) for r in  list(zip(*reversed(self._grid)))[::-1]]
        self._grid = ccw
        return self

    """
    SUM AND PRODUCT methods
    """
    def get_row_sum(self, row_idx):
        return sum([int(i) for i in self.get_row(row_idx)])

    def get_col_sum(self, col_idx):
        return sum([int(i) for i in self.get_col(col_idx)])

    def get_sum(self):
        return sum([int(i) for i in self._flatten()])

    def get_row_prod(self, row_idx):
        return math.prod([int(i) for i in self.get_row(row_idx)])

    def get_col_prod(self, col_idx):
        return math.prod([int(i) for i in self.get_col(col_idx)])

    def get_prod(self):
        return math.prod(self._flatten())

    def add_at(self, row_idx, col_idx, val):
        self._grid[row_idx][col_idx] += val
        return self

    def substract_at(self, row_idx, col_idx, val):
        self._grid[row_idx][col_idx] -= val
        return self

    """
    REPLACE methods
    """
    def replace_at(self, row_idx, col_idx, new_val):
        self._grid[row_idx][col_idx] = new_val
        return self

    def replace_in_row(self, row_idx, old_val, new_val):
        self._grid[row_idx] = [new_val if i==old_val else i for i in self._grid[row_idx]]
        return self

    def replace_in_col(self, col_idx, old_val, new_val):
        for row in self._grid:
            if row[col_idx] == old_val:
                row[col_idx] = new_val
        return self

    def replace_all(self, old_val, new_val):
        for i in range(0, len(self._grid[0])):
            self.replace_in_row(i, old_val, new_val)
        return self

    """
    FINDING AND ADJACENT
    """
    #Get all neigjbourds (inc diaginal?)
    #Find all instances positioons

    """
    ETC
    """
    def pprint(self):
        print(*self._grid, sep='\n')
        print("\n")

    def _flatten(self):
        return [el for row in self._grid for el in row]

#
# _alpha_grid = Grid([['d', 'b', 'c'], ['d', 'e', 'f'], ['g', 'd', 'i']])
# print(_alpha_grid.cols)
# _alpha_grid.pprint()
# print("\n--------------------\n")
#
# _alpha_grid.replace('d', "test")
# _alpha_grid.pprint()
# #
# # print(_alpha_grid.get(0,2))
# # #
# #
# # x = _alpha_grid.get_col(0)
# # print(x)
