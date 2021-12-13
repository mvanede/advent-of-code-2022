from utils import Grid


class ExpandingGrid(Grid):

    def __init__(self, width, height, default_value=0):
        self._default_value = default_value
        super().__init__([([self._default_value] * width) for i in range(height)])

    def set_default_value(self, default_value):
        self._default_value = default_value

    def expand_with(self, wdiff, hdiff):
        if wdiff > 0:
            for row in self.rows:
                row += [self._default_value] * wdiff
        elif wdiff < 0:
            for row_idx, row in enumerate(self.rows):
                self._grid[row_idx] = [self._default_value] * abs(wdiff) + row


        if hdiff > 0:
            self._grid += [([self._default_value] * self.width) for i in range(abs(hdiff))]
        elif hdiff < 0:
            self._grid = [([self._default_value] * self.width) for i in range(abs(hdiff))] + self._grid

    def expand_to(self, width, height):
        # print("expand_to ")
        # print(width, height)

        wdiff = width - (self.width-1)
        hdiff = height - (self.height-1)

        # print("expand with ")
        # print(wdiff, hdiff)

        self.expand_with(wdiff, hdiff)

    def _do_expand_first(self, col_idx:int, row_idx:int):
        # Expand if indexes are out of boundaries
        col_diff = col_idx if col_idx < 0 else max(0, col_idx - (self.width - 1))
        row_diff = row_idx if row_idx < 0 else max(0, row_idx - (self.height - 1))

        if col_diff != 0 or row_diff != 0:
            self.expand_with(col_diff, row_diff)

    def set(self, col_idx:int, row_idx:int, new_val):
        self._do_expand_first(col_idx, row_idx)
        col_idx, row_idx = max(0,col_idx), max(0,row_idx)
        super().set(col_idx, row_idx, new_val)
        return col_idx, row_idx

    def add_at(self, col_idx:int, row_idx:int, val):
        self._do_expand_first(col_idx, row_idx)
        col_idx, row_idx = max(0, col_idx), max(0, row_idx)
        super().add_at(col_idx, row_idx, val)
        return col_idx, row_idx

    def substract_at(self, col_idx:int, row_idx:int, val):
        self._do_expand_first(col_idx, row_idx)
        col_idx, row_idx = max(0, col_idx), max(0, row_idx)
        super().substract_at(col_idx, row_idx, val)
        return col_idx, row_idx