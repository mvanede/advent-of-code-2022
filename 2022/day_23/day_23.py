import itertools
from abc import ABC
from collections import deque, defaultdict
from utils import Parser, Grid
from utils.grid import Coord
from utils.lib import answer, ftimer
from utils.base_solution import BaseSolution

N = (0, -1)
NE = (1, -1)
E = (1, 0)
SE = (1,1)
S = (0,1)
SW = (-1, 1)
W = (-1, 0)
NW = (-1, -1)
N_NE_NW = [N, NE, NW]
S_SE_SW = [S, SE, SW]
W_NW_SW = [W, NW, SW]
E_NE_SE = [E, NE, SE]
        
# CODE HERE
class Day23Solution(BaseSolution, ABC):
    _input = "2022/day_23/day_23.input.txt"
    _test_input = "2022/day_23/day_23_test.input.txt"

    def parse_input(self):
        self.map = Grid(Parser.split_by(self.read_input(), "\n","", conv_func=None), default_value='.')  # lambda x:int(x)
    
    def get_adjacent(self, position):
        directions = (0, -1, 1)
        vectors = itertools.product(directions, directions)
        return [(position[0]+vector[0], position[1]+vector[1]) for vector in vectors if not vector[0]==vector[1]==0]
        
    def do_round(self, elves_positions, considerations):
        new_elve_positions = set()
        goto = defaultdict(list)

        # First half
        for elve in elves_positions:
            
            adjacent = set(self.get_adjacent(elve))
            if adjacent.isdisjoint(elves_positions):
                # Noone around, do nothing
                continue

            for scan in considerations:
                scanned = set([(elve.x+vector[0], elve.y+vector[1]) for vector in scan])
                
                if scanned.isdisjoint(elves_positions):
                    mv = Coord(elve.x + scan[0][0], elve.y + scan[0][1])
                    goto[mv].append(elve)
                    break
        
        # Second half
        moved = set()
        for move_to, elves in goto.items():
            if len(elves) == 1:
                new_elve_positions.add(move_to)
                moved.add(elves.pop())
        
        return new_elve_positions | elves_positions.difference(moved)

    @ftimer
    def solve1(self):
        all_elves = set(self.map.find_all('#'))

        considerations = deque([N_NE_NW, S_SE_SW, W_NW_SW, E_NE_SE])
        for i in range(10):
            all_elves = self.do_round(all_elves, considerations)
            considerations.rotate(-1)

        all_elves_x = [elve.x for elve in all_elves]
        all_elves_y = [elve.y for elve in all_elves]
        width = max(all_elves_x) + 1 - min(all_elves_x)
        height = max(all_elves_y) + 1 - min(all_elves_y)
        return width * height - len(all_elves)
        
    @ftimer
    def solve2(self):
        all_elves = set(self.map.find_all('#'))
         
        considerations = deque([N_NE_NW, S_SE_SW, W_NW_SW, E_NE_SE])
        for i in range(10000):
            all_elves2 = self.do_round(all_elves, considerations)
            diff = all_elves2.difference(all_elves)
            if len(diff) == 0:
                break
            all_elves = all_elves2
            considerations.rotate(-1)
        return i+1
        

if __name__ == '__main__':
    s = Day23Solution(use_test_input=False)
    answer(s.solve1())
    answer(s.solve2())
