import copy
import itertools
from abc import ABC
from collections import defaultdict

from utils import Parser
from utils.graph import Graph
from utils.lib import answer, ftimer
from utils.base_solution import BaseSolution


class Day16Solution(BaseSolution, ABC):
    _input = "2022/day_16/day_16.input.txt"
    _test_input = "2022/day_16/day_16_test.input.txt"
    
    def parse_input(self):
        lines = Parser.split_by(self.read_input(), "\n",";", conv_func=None)  # lambda x:int(x)
        self.valves = {}
        self.flow = {}
        for l in lines:
            valve_name = l[0][6:8]
            flow_rate = int(l[0].split('=')[1])
            connected = [x.strip() for x in  l[1][23:].split(', ')]
            self.flow[valve_name] = flow_rate
            self.valves[valve_name] = connected
        
        self.graph = Graph()
        for v, connected in self.valves.items():
            for n in connected:
                self.graph.add_edge(v, n, 1)
                self.graph.add_edge(n, v, 1)
    
    def prep_graph_with_flow(self):
        valves_with_flow = [node for node, flow in self.flow.items() if flow > 0]
        valves_with_flow.append('AA')
        combinations = list(itertools.combinations(valves_with_flow, r=2))

        # Create a new graph, narrowing down the search space
        g = Graph()
        for frm, to in combinations:
            l, shortest_path = self.graph.dijkstra(frm, to)
            g.add_edge(frm, to, l)
            g.add_edge(to, frm, l)
        return g
    
    def calc_all_flows(self, minutes):
        g = self.prep_graph_with_flow()
        
        # Push initial state onto heap
        heap = [('AA', minutes, 0, set())]
        end_states = defaultdict(int)

        while heap:
            state = heap.pop()
            cur_pos, T, relieved_pressure, open_valves = state

            for nxt, traveltime in g.edges[cur_pos].items():
                remaining_time = T - traveltime - 1

                if remaining_time > 0 and nxt not in open_valves:
                    nw_valves = open_valves | {nxt}
                    pressure_release = self.flow[nxt] if nxt not in open_valves else 0
                    nw_flow = relieved_pressure + (pressure_release * remaining_time)

                    k = frozenset(nw_valves)
                    end_states[k] = max(end_states[k], nw_flow)
                    heap.append((nxt, remaining_time, nw_flow, nw_valves))
        return end_states
    
    @ftimer
    def solve1(self):
        end_states = self.calc_all_flows(30)
        return max(end_states.values())
         
    @ftimer
    def solve2(self):
        end_states = self.calc_all_flows(26)
        non_overlapping_paths  = [(t1, t2) for t1, t2 in itertools.product(end_states.keys(), end_states.keys()) if len(t1.intersection(t2)) == 0]
        max_value = 0
        for my_path, elephant_path in non_overlapping_paths:
            max_value = max(max_value, end_states[my_path]+end_states[elephant_path])
        return max_value


if __name__ == '__main__':
    s = Day16Solution(use_test_input=False)
    answer(s.solve1())
    answer(s.solve2())
