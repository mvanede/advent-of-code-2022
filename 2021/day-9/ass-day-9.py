from utils import Parser, Grid
from utils.lib import get_timer, panswer, pruntime
_ST = get_timer()

f = open("ass-day-9-input.txt", "r")
commands = Parser.split_by(f.read(), "\n", None, conv_func=lambda x:int(x))  # lambda x:int(x)
print(commands)


# Fix
floor = Grid(commands)
floor.print()

# CODE HERE
# print(floor.height)
found = {}
for col in range(0,floor.width):
    for row in range(0, floor.height):
        curval = floor.get(col, row)
        nb = floor.get_adjacent(col, row, False)

        s = sum([1 if i>curval else 0 for i in nb.values() ])
        if s==len(nb):
            found[(col, row)] = curval


panswer(sum([x+1 for x in found.values()]))



panswer("answer")
pruntime(_ST)


