import math
from collections import defaultdict
from heapq import heappush, heappop


class Graph:
    def __init__(self):
        self.edges = defaultdict(dict)
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight

    def dijkstra(self, src, dest):
        predecessor = {}
        shortest_distance = {}

        # Store lowest cost so far to get to this point
        heap = []
        heappush(heap, (0, src, None))

        while heap:
            cost, node, prev = heappop(heap)
            if node in shortest_distance:
                # Already been here, prevent endless looping
                continue

            shortest_distance[node] = cost
            predecessor[node] = prev

            if node == dest:
                path = []
                while node:
                    path.append(node)
                    node = predecessor[node]
                return cost, path[::-1]
            else:
                neighbours = self.edges[node]
                for successor, successor_cost in neighbours.items():
                    heappush(heap, (cost + successor_cost, successor, node))
        # Done, but no cigar
        return math.inf, []