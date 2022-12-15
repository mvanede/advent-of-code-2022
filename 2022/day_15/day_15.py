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
            self.sensors.add((xs, ys))
            self.beacons.add((xb, yb))

    # @ftimer
    def get_x_range_for(self, y, sensor, beacon):
        max_distance = manhattan(sensor, beacon)
        max_h_distance = max_distance - (abs(sensor[1] - y))

        if max_h_distance > 0:
            return sensor[0] - max_h_distance, sensor[0] + max_h_distance

    @ftimer
    def solve1(self, line_nr):
        ranges = []
        y = line_nr
        for sensor, beacon in self.input:
            if r := self.get_x_range_for(y, sensor, beacon):
                ranges.append(r)

        sorted_ranges = sorted(ranges)
        no_beacon_possible_cntr = 0
        prev_range = sorted_ranges[0]

        # Add ranges
        for current_range in sorted_ranges[1:]:
            if prev_range[1] < current_range[0]:
                # GAP between ranges. Add range so far to count and reset
                no_beacon_possible_cntr += prev_range[1] - prev_range[0]
                prev_range = current_range
            else:
                prev_range = (prev_range[0], max(prev_range[1], current_range[1]))

        # Finally, add length of range to counter
        return no_beacon_possible_cntr + prev_range[1] - prev_range[0]

    def match_ranges(self, max_y):
        for y in range(0, max_y + 1):

            ranges = []
            for sensor, beacon in self.input:
                # If the combine ranges cover the entire column, continue
                if r := self.get_x_range_for(y, sensor, beacon):
                    ranges.append(r)

            # Rows should be completely filled, so each start of range should be lower or equal to end of max of all previous
            sorted_ranges = sorted(ranges)
            prev_range = sorted_ranges[0]

            # Add ranges
            for current_range in sorted_ranges[1:]:
                if prev_range[1] < current_range[0]:
                    # GAP between ranges! Let's assume it's where we need to be
                    return (prev_range[1], y)
                else:
                    prev_range = (prev_range[0], max(prev_range[1], current_range[1]))

    @ftimer
    def solve2(self, max_y):
        x, y = self.match_ranges(max_y)
        return x * 4000000 + y


if __name__ == '__main__':
    s = Day15Solution(use_test_input=False)
    answer(s.solve1(2000000))
    answer(s.solve2(4000000))

# Your puzzle answer was 5147333.
# Your puzzle answer was 13734006908372
