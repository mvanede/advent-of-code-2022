
class Location:

    def __init__(self, col=0, row=0):
        self._col = col
        self._row = row
        self.set_direction_map ('^', 'v','<', '>')

    @property
    def position(self):
        return self._col, self._row

    @property
    def col(self):
        return self._col

    @property
    def row(self):
        return self._row

    def set(self, col, row):
        self._col = col
        self._row = row

    def up(self, n=1):
        self._row -= n

    def down(self, n=1):
        self._row += n

    def left(self, n=1):
        self._col -= n

    def right(self, n=1):
        self._col += n

    def go(self, direction_char):
        self._direction_map[direction_char]()

    def set_direction_map(self, up, down, left, right):
        self._direction_map = {
            up: self.up,
            right: self.right,
            left: self.left,
            down: self.down
        }
