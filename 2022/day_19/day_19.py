import copy
import math
from abc import ABC
from pprint import pprint
import re

from utils import Parser, MapReduceList
from utils.lib import answer, ftimer
from utils.base_solution import BaseSolution


# CODE HERE
class Day19Solution(BaseSolution, ABC):
    _input = "2022/day_19/day_19.input.txt"
    _test_input = "2022/day_19/day_19_test.input.txt"

    # def __init__(self, use_test_input):
    #     super().method(use_test_input)

    def parse_input(self):
        lines = Parser.split_by(self.read_input(), "\n", conv_func=None)  # lambda x:int(x)

        self.blueprints = []
        for l in lines:
            bp_nr, ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian = list(
                map(int, re.findall(r"-?\d+", l)))
            self.blueprints.append({
                'ore': [ore_ore, 0, 0],
                'clay': [clay_ore, 0, 0],
                'obsidian': [obsidian_ore, obsidian_clay, 0],
                'geode': [geode_ore, 0, geode_obsidian]
            })

    def calculate_blueprint(self, bp, max_time):
        maxima = {
            'ore': max([v[0] for k, v in bp.items()]),
            'clay': max([v[1] for k, v in bp.items()]),
            'obsidian': max([v[2] for k, v in bp.items()]),
            'geode': math.inf
        }

        # Push initial state onto heap
        heap = [(['ore'], 0, {'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0})]
        max_geode = 0
        visited = {}
        end_states = []

        while heap:
            arsenal, T, wallet = heap.pop()
            max_geode = max(max_geode, wallet['geode'])
            if T == max_time:
                end_states.append((T, arsenal, wallet))
                continue

            # If we've been here, ignore this state
            vkey = tuple(arsenal), T
            if vkey in visited:
                w = visited[vkey]
                if w['ore'] >= wallet['ore'] and w['clay'] >= wallet['clay'] and w['obsidian'] >= wallet['obsidian']:
                    continue

            visited[vkey] = wallet
            new_wallet = copy.copy(wallet)

            # Then collect
            for robot in arsenal:
                new_wallet[robot] += 1
            max_geode = max(max_geode, new_wallet['geode'])

            # Skip too big wallets. Not sure where the threshold is, increased it until new run didnt provide a higher outcome
            time_left = (max_time - T) + 3
            if new_wallet['ore'] > time_left * maxima['ore'] or new_wallet['clay'] > time_left * maxima['clay'] or \
                    new_wallet[
                        'obsidian'] > time_left * maxima['obsidian']:
                continue

            heap.append((copy.copy(arsenal), T + 1, copy.copy(new_wallet)))

            # If we can afford a geode machine, do so. otherwise, pick one of the others
            if wallet['ore'] >= bp['geode'][0] and wallet['clay'] >= bp['geode'][1] and wallet['obsidian'] >= \
                    bp['geode'][2]:
                w = copy.copy(new_wallet)
                new_arsenal = copy.copy(arsenal)
                new_arsenal.append(rname)
                w['ore'] -= bp['geode'][0]
                w['clay'] -= bp['geode'][1]
                w['obsidian'] -= bp['geode'][2]
                heap.append((new_arsenal, T + 1, w))
            else:
                for rname, rcost in bp.items():

                    # If we have enough robots of this type, skip it
                    if arsenal.count(rname) >= maxima[rname]:
                        continue

                    if wallet['ore'] >= rcost[0] and wallet['clay'] >= rcost[1] and wallet['obsidian'] >= rcost[2]:
                        w = copy.copy(new_wallet)
                        new_arsenal = copy.copy(arsenal)
                        new_arsenal.append(rname)
                        w['ore'] -= rcost[0]
                        w['clay'] -= rcost[1]
                        w['obsidian'] -= rcost[2]
                        heap.append((new_arsenal, T + 1, w))
        return max_geode

    @ftimer
    def solve1(self):
        all_values = []
        for idx, bp in enumerate(self.blueprints):
            all_values.append((idx + 1, self.calculate_blueprint(bp, 24)))
        return sum([a * b for a, b in all_values])

    @ftimer
    def solve2(self):
        all_values = []
        for idx, bp in enumerate(self.blueprints[0:3]):
            all_values.append((idx + 1, self.calculate_blueprint(bp, 32)))
        return MapReduceList(all_values).map(lambda x: x[1]) \
            .reduce(lambda x, y: x * y)


if __name__ == '__main__':
    s = Day19Solution(use_test_input=False)
    answer(s.solve1())
    answer(s.solve2())

# Your puzzle answer was 1427.
# Your puzzle answer was 4400.