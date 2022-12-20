from abc import ABC
from pprint import pprint

from utils import Parser
from utils.lib import answer, ftimer
from utils.base_solution import BaseSolution

# Model sides as two points. Opposites mirror, for easier comparison
def get_surfaces(x, y, z):
    return set([
        ((x, y, z), (x+1, y+1, z)),
        ((x+1, y, z), (x+1, y+1, z+1)),
        ((x, y, z+1), (x+1, y+1, z+1)),
        ((x, y, z), (x, y+1, z+1)),
        ((x, y, z), (x+1, y, z+1)),
        ((x, y+1, z), (x+1, y+1, z+1))
    ])

def get_neighbours(x, y, z):
    return [
        (x+1, y, z),
        (x-1, y, z),
        (x, y-1, z),
        (x, y+1, z),
        (x, y, z-1),
        (x, y, z+1)
    ]

# CODE HERE
class Day18Solution(BaseSolution, ABC):
    _input = "2022/day_18/day_18.input.txt"
    _test_input = "2022/day_18/day_18_test.input.txt"

    def parse_input(self):
        self.drops = Parser.split_by(self.read_input(), "\n", ",", conv_func=lambda x:int(x))  # lambda x:int(x)
        
    def calc_exposed_surfaces(self):
        exposed_surfaces = get_surfaces(*self.drops[0])
        for drop in self.drops[1:]:
            surfaces = get_surfaces(*drop)
            # symmetric_difference combines everything, expect for whats in both sets
            exposed_surfaces = exposed_surfaces.symmetric_difference(surfaces)
        return exposed_surfaces
    
    @ftimer
    def solve1(self):
        return len(self.calc_exposed_surfaces())
    
    @ftimer
    def solve2(self):
        exposed_surfaces = self.calc_exposed_surfaces()
        
        min_x = min([f[0][0] for f in exposed_surfaces]) -1
        max_x = max([f[1][0] for f in exposed_surfaces])

        min_y = min([f[0][1] for f in exposed_surfaces]) -1
        max_y = max([f[1][1] for f in exposed_surfaces])

        min_z = min([f[0][2] for f in exposed_surfaces]) -1
        max_z = max([f[1][2] for f in exposed_surfaces])
        
        outside_surfaces = set()
        outer_space = [(min_x, min_y, min_z)]
        checked = set()
        while outer_space:
            current = outer_space.pop()
            cur_x, cur_y, cur_z = current
            
            # Been here
            if current in checked:
                continue
            
            checked.add(current)
            
            # If it's outside our space, skip
            if cur_x > max_x or cur_x < min_x \
                or cur_y > max_y or cur_y < min_y \
                or cur_z > max_z or cur_z < min_z:
                continue
            
            for nxt_x, nxt_y, nxt_z in get_neighbours(cur_x, cur_y, cur_z):
                if [nxt_x, nxt_y, nxt_z] in self.drops:
                    continue
                
                for f in get_surfaces(nxt_x, nxt_y, nxt_z):
                    if f in exposed_surfaces:
                        outside_surfaces.add(f)
                outer_space.append((nxt_x, nxt_y, nxt_z))
                
        return len(outside_surfaces)
        

if __name__ == '__main__':
    s = Day18Solution(use_test_input=False)
    answer(s.solve1())
    answer(s.solve2())


#  Your puzzle answer was 4482.
# Your puzzle answer was 2576.