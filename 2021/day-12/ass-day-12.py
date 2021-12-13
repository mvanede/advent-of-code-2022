from utils import Parser
from collections import defaultdict
from utils.lib import get_timer, panswer, pruntime
_ST = get_timer()

f = open("ass-day-12-input.txt", "r")
commands = Parser.split_by(f.read(), "\n","-", conv_func=None)  # lambda x:int(x)

# CODE HERE
steps = defaultdict(list)
for frm, to in commands:
    steps[frm].append(to)
    steps[to].append(frm)

visitedList = [[]]

def df_find_paths(graph, currentVertex, visited, dontgothereagain):
    if currentVertex.lower() == currentVertex:
        dontgothereagain.append(currentVertex)

    visited.append(currentVertex)

    for vertex in graph[currentVertex]:
        if vertex not in dontgothereagain:
            df_find_paths(graph, vertex, visited.copy(), dontgothereagain.copy())

    visitedList.append(visited)


df_find_paths(steps, 'start', [], [])
start_to_end = []
for v in visitedList:
    if len(v) and v[0] == 'start' and v[-1] == 'end':
        start_to_end.append(v)


panswer(len(start_to_end))
pruntime(_ST)


