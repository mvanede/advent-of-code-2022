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
            return range(sensor[0] - max_h_distance, sensor[0] + max_h_distance + 1)

    @ftimer
    def solve1(self, line_nr):
        self.no_beacons = set()
        y = line_nr
        for sensor, beacon in self.input:
            if r := self.get_x_range_for(y, sensor, beacon):
                for x in r:
                    self.no_beacons.add((x, y))

        a = len(self.no_beacons)
        b = len([n for n in self.beacons if n[1] == line_nr])
        c = len([n for n in self.sensors if n[1] == line_nr])
        return a - b - c

    @ftimer
    def solve2(self, line_nr):
        search_area = Polygon([
            (0, 0),
            (line_nr, 0),
            (line_nr, line_nr),
            (0, line_nr),
        ])
        for sensor, beacon in self.input:
            max_distance = manhattan(sensor, beacon)
            coords = [
                (sensor[0] - max_distance, sensor[1]),
                (sensor[0], sensor[1] - max_distance),
                (sensor[0] + max_distance, sensor[1]),
                (sensor[0], sensor[1] + max_distance),
            ]
            polygon = Polygon(coords)
            search_area = search_area.difference(search_area.intersection(polygon))

        # p = gpd.GeoSeries(search_area)
        # p.plot()
        # plt.show()

        x = (search_area.bounds[0] + search_area.bounds[2]) // 2
        y = (search_area.bounds[1] + search_area.bounds[3]) // 2

        return int(x * line_nr + y)


if __name__ == '__main__':
    s = Day15Solution(use_test_input=False)
    answer(s.solve1(2000000))
    answer(s.solve2(4000000))

# Your puzzle answer was 5147333.
# Your puzzle answer was 13734006908372
