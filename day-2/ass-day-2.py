f = open("ass-day-2-input.txt", "r")
lines = f.read().split("\n")
commands = [line.split(" ") for line in lines]

x,y = 0,0
for c in commands:
    if c[0] == "forward":
       y += int(c[1])
    elif c[0] == "up":
        x -= int(c[1])
    elif c[0] == "down":
        x += int(c[1])

print(x*y)