import math
from abc import ABC
from heapq import heappush, heappop
from utils import Parser, Grid
from utils.grid import Coord
from utils.lib import answer, ftimer
from utils.base_solution import BaseSolution


isentrance = lambda x, y, w, h: x==1 and y==0 
isexit = lambda x, y, w, h: y==h-1 and x==w-2
isborder = lambda x, y, w, h: (y==0 or y==h-1 or x==0 or x==w-1)


class BlizzardGrid(Grid):

    def draw(self, blizzards, position_self):
        m = Grid.init_with(self.width, self.height, default_value='.')
        positions = [pos for pos, _ in blizzards]
        for pos, dir in blizzards:
            m.set(pos.x, pos.y, str(positions.count(pos)) if positions.count(pos)> 1 else dir)
        
        m.set(position_self.x, position_self.y, 'E')

    # @ftimer
    def move_blizzards(self, blizzards):
        new_blizzards = []
        for pos, dir in blizzards:
            match dir:
                case'>':
                    nw_pos = (pos.x+1, pos.y) if not isborder(pos.x+1, pos.y, self.width, self.height) else (1, pos.y)
                case '<':
                    nw_pos = (pos.x - 1, pos.y) if not isborder(pos.x - 1, pos.y, self.width,
                                                                self.height) else (self.width-2, pos.y)
                case '^':
                    nw_pos = (pos.x, pos.y-1) if not isborder(pos.x, pos.y-1, self.width,
                                                                self.height) else (pos.x, self.height - 2)
                case 'v':
                    nw_pos = (pos.x, pos.y + 1) if not isborder(pos.x, pos.y + 1, self.width,
                                                                self.height) else (pos.x, 1)
            new_blizzards.append((Coord(*nw_pos), dir))
        return new_blizzards
    
    @ftimer
    def build_blizzard_cache(self, blizzards):
        lcm = math.lcm(self.width - 2, self.height - 2)
        blizzard_cache = {
            0: frozenset(blizzards)
        }
        
        for i in range(lcm):
            blizzards = self.move_blizzards(blizzards)
            blizzard_cache[i + 1] = set([p for p, _ in blizzards])
        return blizzard_cache
        
    def dijkstra2(self, src: Coord, dest: Coord, blizzard_cache, start_minute=0):
        lcm = math.lcm(self.width - 2, self.height - 2)
        allow_func = lambda nb, _blizzards: nb not in _blizzards and not isborder(nb.x, nb.y,
                                                                                    self.width,
                                                                                    self.height)

        seen = set()
        heap = []
        heappush(heap, (start_minute, src))
        
        while heap:
            cost, node = heappop(heap)
            minute = cost + 1
            
            if node == dest:
                return minute-1
            else:
                blizzards = blizzard_cache[minute % lcm]
                neighbours = self.get_adjacent(node, include_diagonal=False, include_self=True)
                
                # Get all directions, but can't be outside field, nor a  border, nor occupied by blizzards
                valid_neighbours = [neighbour for neighbour in neighbours if 
                                    allow_func(neighbour, blizzards) or isexit(neighbour.x, neighbour.y, self.width, self.height) 
                                    or isentrance(neighbour.x, neighbour.y, self.width, self.height)]

                # Little optimization
                if dest in valid_neighbours:
                    valid_neighbours = [dest]
                
                for successor in valid_neighbours:
                    key = (successor, minute % lcm)
                    if key not in seen:
                        seen.add(key)
                        heappush(heap, (minute, successor))

        # Done, but no cigar
        return math.inf, [], 'did not finish'

# CODE HERE
class Day24Solution(BaseSolution, ABC):
    _input = "2022/day_24/day_24.input.txt"
    _test_input = "2022/day_24/day_24_test.input.txt"

    def parse_input(self):
        self.map = BlizzardGrid(Parser.split_by(self.read_input(), "\n", "", conv_func=None)) 
        blizzards = [] 
        for d in ['<', '>', '^', 'v']:
            blizzards += [(x, d) for x in self.map.find_all(d)]
        self.blizzard_cache = self.map.build_blizzard_cache(blizzards)
    
    @ftimer
    def solve1(self):
        startp = Coord(1, 0)
        exitp  = Coord(self.map.width-2, self.map.height-1)
        return self.map.dijkstra2(startp, exitp, self.blizzard_cache, 0)
        
        
    @ftimer
    def solve2(self):
        startp = Coord(1, 0)
        exitp = Coord(self.map.width - 2, self.map.height - 1)
        
        first = self.map.dijkstra2(startp, exitp, self.blizzard_cache, 0)
        second = self.map.dijkstra2(exitp, startp, self.blizzard_cache, first)
        return self.map.dijkstra2(startp, exitp, self.blizzard_cache, second)
        
    


if __name__ == '__main__':
    s = Day24Solution(use_test_input=False)
    answer(s.solve1())
    answer(s.solve2())

# Your puzzle answer was 301.
# Your puzzle answer was 859.