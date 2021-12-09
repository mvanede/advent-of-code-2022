from utils import Parser
f = open("ass-day-2-input.txt", "r")
commands = Parser.split_by(f.read(), "\n", " ", conv_func=None )


x,y = 0,0
for c in commands:
    if c[0] == "forward":
       y += int(c[1])
    elif c[0] == "up":
        x -= int(c[1])
    elif c[0] == "down":
        x += int(c[1])

print(x*y)