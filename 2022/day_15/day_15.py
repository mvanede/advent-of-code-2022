import math
import re
from abc import ABC
from shapely import Polygon
import matplotlib.pyplot as plt
import geopandas as gpd
from utils import Parser
from utils.lib import answer, ftimer
from utils.base_solution import BaseSolution

manhattan = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1])


# CODE HERE
class Day15Solution(BaseSolution, ABC):
    _input = "2022/day_15/day_15.input.txt"
    _test_input = "2022/day_15/day_15_test.input.txt"

    def parse_input(self):
        lines = Parser.split_by(self.read_input(), "\n", conv_func=None)  # lambda x:int(x)
        self.input = []
        self.beacons = set()
        self.sensors = set()
        
        for l in lines:
            xs, ys, xb, yb = list(map(int, re.findall(r"-?\d+", l)))
            self.input.append(((xs, ys), (xb, yb)))
            # self.sensors.add((xs, ys))
            # self.beacons.add((xb, yb))
    
    # @ftimer
    def get_x_range_for(self, y, sensor, beacon):
        max_distance = manhattan(sensor, beacon)
        max_h_distance = max_distance - ( abs(sensor[1]-y) )
        
        if max_h_distance > 0:
            return range(sensor[0]-max_h_distance, sensor[0] + max_h_distance + 1)
                
    @ftimer
    def solve1(self, line_nr):
        self.no_beacons = set()
        y = line_nr
        for sensor, beacon in self.input:
            if r:= self.get_x_range_for(y, sensor, beacon):
                for x in r and beacon:
                    self.no_beacons.add((x, y))

        a = len(self.no_beacons)
        b = len([n for n in self.beacons if n[1] == line_nr])
        c = len([n for n in self.sensors if n[1] == line_nr])
        return a - b - c

    def match_ranges(self, max_y):
        for y in range(0, max_y + 1):
            ranges = []
            for sensor, beacon in self.input:
                # If the combine ranges cover the entire column, continue
                if r := self.get_x_range_for(y, sensor, beacon):
                    ranges.append(r)

            sorted_ranges = sorted(ranges, key=lambda rng: rng[0])

            # Rows should be filled, so each start of range should be lower or equal to end of max of all previous
            prev_range = sorted_ranges[0]
            mx_prev_range = prev_range.stop
            for r in sorted_ranges[1:]:
                mx_prev_range = max(mx_prev_range, prev_range.stop)

                if prev_range.stop > max_y:
                    break
                    
                # NOT ONLY PREV, BUT MAX OF ALL PREVS
                if r.start > mx_prev_range:
                    return (prev_range.stop, y)
                prev_range = r
                
    @ftimer
    def solve2(self, max_y):
        x, y = self.match_ranges(max_y)
        return x*4000000 +y 

            
        
if __name__ == '__main__':
    s = Day15Solution(use_test_input=False)
    answer(s.solve1(2000000))
    answer(s.solve2(4000000))

# Your puzzle answer was 5147333.
# Your puzzle answer was 13734006908372
