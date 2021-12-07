from utils import Parser
from utils.lib import get_timer, panswer, pruntime
_ST = get_timer()

f = open("ass-day-6-input.txt", "r")
_CYCLE = 6
FIRST_CYCLE = 8
NR_DAYS = 256

# Construct dictionary, key=number of days left, value=nr of fish
fish = {}
for f in Parser.split_by(f.read(), ",", conv_func=lambda x:int(x) ):
    fish[f] = fish.get(f, 0) + 1

# Let the days roll
for i in range(NR_DAYS):
    new_fish = {}
    for days_left, nr_of_fish in fish.items():
        if days_left > 0:
            new_fish[days_left-1] = new_fish.get(days_left-1, 0) + nr_of_fish
        else:
            # Spawn fish
            new_fish[FIRST_CYCLE] = new_fish.get(FIRST_CYCLE, 0) + nr_of_fish
            new_fish[_CYCLE] = new_fish.get(_CYCLE, 0) + nr_of_fish
    fish = new_fish

# Count
panswer(sum(fish.values()))
pruntime(_ST)
