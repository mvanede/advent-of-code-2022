from utils import Parser, Grid
from utils.lib import get_timer, panswer, pruntime
import math
_ST = get_timer()

f = open("ass-day-9-input.txt", "r")
_input = Parser.split_by(f.read(), "\n", None, conv_func=lambda x:int(x))
floor = Grid(_input)


def get_lowest_points(_floor: Grid):
    low = {}
    for col in range(0, _floor.width):
        for row in range(0, _floor.height):
            curval = _floor.get(col, row)
            nb = _floor.get_adjacent(col, row, False)
            s = sum([1 if i>curval else 0 for i in nb.values() ])
            if s == len(nb):
                low[(col, row)] = curval
    return low


def get_higher_neighbours(_col_idx, _row_idx, higher_than):
    neighbours = floor.get_adjacent(_col_idx, _row_idx, False)
    basin = [(_col_idx, _row_idx)]
    for coord, val in neighbours.items():
        if val <= higher_than or val == 9:
            continue

        basin.append(coord)
        if val < 8:
            basin += get_higher_neighbours(coord[0], coord[1], val)

    return basin

# Get basin for each lowest point
pit_sizes = []
for col_idx, row_idx in get_lowest_points(floor).keys():
    low_val = floor.get(col_idx, row_idx)
    nb = get_higher_neighbours(col_idx, row_idx, low_val)
    pit_sizes.append(len(set(nb)))


# Get product of largest 3 bassins
pit_sizes.sort(reverse=True)
panswer(math.prod(pit_sizes[0:3]))
pruntime(_ST)


# 786780