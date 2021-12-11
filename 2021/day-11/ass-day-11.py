from utils import Parser, Grid
from utils.lib import get_timer, panswer, pruntime
_ST = get_timer()

f = open("ass-day-11-input.txt", "r")
grid = Parser.split_by(f.read(), "\n", '', conv_func=lambda x:int(x))

octopuses = Grid(grid)
octopuses.pprint()


def flash(_local_grid, col_idx, row_idx):
    # Increase all neighbours (including diagonal)
    for col_idx2, row_idx2 in _local_grid.get_adjacent(col_idx, row_idx, True):
        _local_grid.add_at(col_idx2, row_idx2, 1)

        # Newly created flashes
        if _local_grid.get(col_idx2, row_idx2) == 10:
            flash(_local_grid, col_idx2, row_idx2)


def round(_local_grid: Grid):
    # First, the energy level of each octopus increases by 1.
    for col_idx, row_idx in _local_grid.get_cells():
        if _local_grid.get(col_idx, row_idx) <= 9:
            _local_grid.add_at(col_idx, row_idx, 1)

    # Then, any octopus with an energy level greater than 9 flashes.This increases the energy level of all adjacent octopuses by 1
    _grid_copy = _local_grid.get_copy()
    for col_idx, row_idx in _grid_copy.get_cells():
        v = _local_grid.get(col_idx, row_idx)
        if v == 10:
            flash(_grid_copy, col_idx, row_idx)
    _local_grid = _grid_copy

    # Finally, any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to flash.
    nr_flashes = 0
    for col_idx, row_idx in _local_grid.get_cells().keys():
        v = _local_grid.get(col_idx, row_idx)
        if v > 9:
            _local_grid.set(col_idx, row_idx, 0)
            nr_flashes +=1

    return _local_grid, nr_flashes


nr_flashes = 0
for i in range(0, 100):
    print ("ROUND " + str(i+1))
    octopuses, _nr_flashes = round(octopuses)
    octopuses.pprint()
    nr_flashes += _nr_flashes

panswer(nr_flashes)
pruntime(_ST)