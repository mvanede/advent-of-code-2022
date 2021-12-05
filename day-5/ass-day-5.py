from utils import Parser, Grid
from utils.lib import max_in_list

f = open("ass-day-5-input.txt", "r")
coordinates = Parser.split_by(f.read(),  "\n", " -> ", ",", conv_func=lambda x:int(x))
mx = max_in_list(coordinates)
grid = Grid.init_with(mx, mx, 0)

# coord := (col_idx, row_idx)
for frm, to in coordinates:
    row_range = col_range = []
    frm_col, frm_row, to_col, to_row = frm + to

    if frm_col == to_col:
        # VERTICAL (COLUMN REMAINS SAME)
        row_range = list(range(min(frm_row, to_row), max(frm_row, to_row) + 1))
        col_range = [frm_col] * len(row_range)
    elif frm_row == to_row:
        # HORIZONTAL (ROW REMAINS SAME)
        col_range = list(range(min(frm_col, to_col), max(frm_col, to_col) + 1))
        row_range = [frm_row] * len(col_range)

    points = zip(col_range, row_range)
    for col_idx, row_idx in points:
        grid.add_at(col_idx, row_idx, 1)


print(grid.count_if(lambda x:x>1))