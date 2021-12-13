from utils import Parser, ExpandingGrid, Grid
from utils.lib import get_timer, panswer, pruntime
_ST = get_timer()

f = open("ass-day-13-input.txt", "r")
commands = Parser.split_by(f.read(), "\n\n", conv_func=None)

folding = Parser.split_by(commands[1], "\n", ",", conv_func=lambda x: x.replace('fold along ', ''))
coordinates = Parser.split_by(commands[0], "\n",",", conv_func=lambda x:int(x))

grid = ExpandingGrid(1,1, '.')
for col, row in coordinates:
    grid.set(col, row, '#')

for instruction in folding:
    axis, linenr = instruction[0].split('=')
    linenr = int(linenr)

    copy_to = copy_from = None
    if axis == 'y':
        copy_to = Grid(grid.get_rows(0, linenr))
        copy_from = Grid(grid.get_rows(linenr+1,grid.height))
        copy_from.flip_horizontal()

    elif axis == 'x':
        copy_to = Grid(grid.get_cols(0, linenr))
        copy_from = Grid(grid.get_cols(linenr + 1, grid.width))
        copy_from.flip_vertical()

    # Copy it
    for coord, val in copy_to.cells.items():
        col_idx, row_idx = coord
        if copy_to.get(col_idx, row_idx) == '#' or copy_from.get(col_idx, row_idx) == '#':
            copy_to.set(col_idx, row_idx, '#')
    grid = copy_to


grid.replace_all('.','⬜')
grid.replace_all('#','🟥')
grid.pprint()

cnt = grid.count_if(lambda x: x=='#')
panswer(cnt)

pruntime(_ST)


