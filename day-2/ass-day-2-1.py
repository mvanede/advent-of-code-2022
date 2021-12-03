f = open("ass-day-2-input.txt", "r")
lines = f.read().split("\n")
commands = [line.split(" ") for line in lines]

x,y, aim = 0,0,0
for c in commands:
    if c[0] == "forward":
       y += int(c[1])
       x += aim*int(c[1])
    elif c[0] == "up":
        aim -= int(c[1])
    elif c[0] == "down":
        aim += int(c[1])

print(x*y)