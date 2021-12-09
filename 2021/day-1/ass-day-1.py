import pathlib
f = open(pathlib.Path(__file__).parent.resolve().joinpath("ass-day-1-input.txt"), "r")
lines = f.read().split("\n")
depths = [int(line) for line in lines]

s = sum(1 if val>depths[k-1] else 0 for k, val in enumerate(depths))
print(s)