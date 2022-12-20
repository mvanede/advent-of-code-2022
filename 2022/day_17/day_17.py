import copy
from abc import ABC
from collections import defaultdict
from pprint import pprint

from utils import Parser, Grid, ExpandingGrid
from utils.lib import answer, ftimer
from utils.base_solution import BaseSolution


# CODE HERE
class Day17Solution(BaseSolution, ABC):
    _input = "2022/day_17/day_17.input.txt"
    _test_input = "2022/day_17/day_17_test.input.txt"

    def parse_input(self):
        self.jet_idx = 0
        self.shapes = [
            Grid([list('####')]),
            Grid([list('.#.'), list('###'), list('.#.')]),
            Grid([list('..#'), list('..#'), list('###')]),
            Grid([list('#'),list('#'), list('#'), list('#')]),
            Grid([list('##'),list('##')]),
        ]
        self.jets = Parser.split_by(self.read_input(), "", conv_func=None)  # lambda x:int(x)
        self._chamber = ExpandingGrid([list('.......'), list('.......'), list('-------')], default_value='.')
        
    
    def find_top_row(self):
        for row_idx, row in enumerate(self.chamber.rows):
            if len([c for c in row if c is not self.chamber.default_value ]):
                return row_idx
    
    def jet_set(self, shape_pos, shape, jet):
        match jet:
            case '>':
                if shape_pos[0] + shape.width < self.chamber.width:
                    if not self.is_collision(shape, [shape_pos[0] + 1, shape_pos[1] - 1]):
                        shape_pos[0] += 1
            case '<':
                if shape_pos[0] > 0:
                    if not self.is_collision(shape, [shape_pos[0] -1, shape_pos[1]-1]):
                        shape_pos[0] -= 1
        self.jet_idx += 1
        return shape_pos
    
    def is_collision(self, shape, shape_position):
        start_scanning = shape_position[1] + 1
        for row_idx, row in enumerate(shape.rows):
            for col_idx, shape_col in enumerate(shape.get_row(row_idx)):
                if shape_col == '#' and self.chamber.get2(col_idx + shape_position[0], row_idx + start_scanning) != '.':
                    return True
        return False
    
    def add_shape_to_chamber(self, shape: Grid, shape_position, chamber=None):
        chamber = chamber if chamber else self.chamber
        x_diff, y_diff = shape_position
        for pos in shape.cells:
            if shape.get(pos) == '#':
                chamber.set(pos.x+x_diff, pos.y+y_diff, shape.get(pos))
        return chamber
    
    
    def get_next_shape(self, i):
        shape_idx = i % 5
        shape = self.shapes[shape_idx]
        
        # Todo: simplify
        first_row_with_rock = self.find_top_row()
        height_to_add = (shape.height + 3) - first_row_with_rock        
        shape_start_pos = [2, 0]
        if height_to_add > 0:
            self.chamber.set(0, -height_to_add, self.chamber.default_value)
        elif height_to_add < 0:
            shape_start_pos = [2, -height_to_add]
    
        return shape_idx, shape, shape_start_pos

    def get_next_jet(self):
        jet_idx = self.jet_idx % len(self.jets)
        jet = self.jets[jet_idx]
        return jet_idx, jet
    
    def get_chamber_height(self):
        return (self.chamber.height - 1 - self.find_top_row())
    
    def reset(self):
        self.jet_idx = 0
        self.chamber = copy.deepcopy(self._chamber)
        
    @ftimer
    def solve1(self, nr_shapes_to_drop):
        self.reset()
        cache2 = defaultdict(list)
        
        for shape_nr in range(nr_shapes_to_drop):
            shape_idx, shape, shape_pos = self.get_next_shape(shape_nr)
            
            while True:
                jet_idx, jet = self.get_next_jet()
                key = (shape_idx, jet_idx)

                if key in cache2:
                    prev_shape_nr, height_offset = cache2[key]
                    repeat_size = shape_nr - prev_shape_nr
                    remaining_shapes_to_be_dropped = nr_shapes_to_drop - shape_nr
                    
                    # Repeating block can start at any line. We need to pick it up when and exact number
                    # of repetitions fit in the remaining nr blocks to be dropped
                    if remaining_shapes_to_be_dropped % repeat_size == 0:
                        repeat_height = self.get_chamber_height() - height_offset
                        reps_remaining = (remaining_shapes_to_be_dropped // repeat_size) + 1
                        return height_offset + (repeat_height * reps_remaining)
                else:
                    cache2[key] = (shape_nr, self.get_chamber_height())

                shape_pos = self.jet_set(shape_pos, shape, jet)
                if self.is_collision(shape, shape_pos):
                    # Settle and continue with next shape
                    self.add_shape_to_chamber(shape, shape_pos)
                    break
                else:
                    # Move down
                    shape_pos[1] += 1
        return self.get_chamber_height()
                
            
    
    @ftimer
    def solve2(self):
        pass


if __name__ == '__main__':
    s = Day17Solution(use_test_input=False)
    answer(s.solve1(nr_shapes_to_drop=2022))
    answer(s.solve1(nr_shapes_to_drop=1_000_000_000_000))


# Your puzzle answer was 3166.
# Your puzzle answer was 1577207977186.

# Offset = 1546