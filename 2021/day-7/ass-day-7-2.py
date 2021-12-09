from utils import Parser
from utils.lib import get_timer, panswer, pruntime
_ST = get_timer()

f = open("ass-day-7-input.txt", "r")
positions = Parser.split_by(f.read(), ",", conv_func=lambda x:int(x))  # lambda x:int(x)

fuels = []
for i in range (min(positions), max(positions) + 1):
    s = 0
    for p in positions:
        diff = abs(p - i)
        s += int((diff*(diff+1)) /2)  # 4+3+2+1 = 4*(4+1) / 2 = 10
    fuels.append(s)

panswer(min(fuels))
pruntime(_ST)
