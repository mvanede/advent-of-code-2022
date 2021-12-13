from utils import Parser
from collections import defaultdict
from utils.lib import get_timer, panswer, pruntime

_ST = get_timer()

f = open("ass-day-12-input.txt", "r")
commands = Parser.split_by(f.read(), "\n", "-", conv_func=None)  # lambda x:int(x)

# CODE HERE
steps = defaultdict(list)
for frm, to in commands:
    steps[frm].append(to)
    steps[to].append(frm)


def go_there(vertex, cave_count):
    if vertex not in cave_count.keys():
        return True

    if vertex in ['start', 'end']:
        return False

    return 2 not in cave_count.values()


visitedList = [[]]
def df_find_paths(graph, currentVertex, visited, dontgothereagain):
    if currentVertex.lower() == currentVertex:
        dontgothereagain[currentVertex] = dontgothereagain.get(currentVertex, 0) + 1

    visited.append(currentVertex)

    for vertex in graph[currentVertex]:
        if go_there(vertex, dontgothereagain):
            df_find_paths(graph, vertex, visited.copy(), dontgothereagain.copy())

    visitedList.append(visited)


df_find_paths(steps, 'start', [], {})
start_to_end = [v for v in visitedList if len(v) and v[0] == 'start' and v[-1] == 'end']
panswer(len(start_to_end))
pruntime(_ST)


