from utils import Parser
from utils.lib import get_timer, panswer, pruntime
_ST = get_timer()

f = open("ass-day-8-input.txt", "r")
lines = Parser.split_by(f.read(), "\n", " | ", " ", conv_func=None)  # lambda x:int(x)

# CODE HERE
countr = 0
for signals, output in lines:
    for x in output:
        if len(x) in (2,3,4,7):
            countr += 1

panswer(countr)
pruntime(_ST)


