f = open("ass-day-3-input.txt", "r")
lines = f.read().split("\n")
input = [list(line) for line in lines]


def count_and_filter(l, more):
    idx = 0
    while len(l) > 1:
        _count = sum([int(item[idx]) for item in l])
        _filterval = int(_count >= len(l) / 2) if more else int(_count < len(l) / 2)
        l = [item for item in l if int(item[idx]) == _filterval]
        idx += 1
    return l


oxygen = int(''.join(count_and_filter(input, True)[0]), 2)
co2 = int(''.join(count_and_filter(input, False)[0]), 2)
print(oxygen*co2)