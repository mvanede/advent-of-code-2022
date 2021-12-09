f = open("ass-day-3-input.txt", "r")
lines = f.read().split("\n")
input = [list(line) for line in lines]

gamma, epsilon = '', ''
for i in range (0, len(input[0])):
    c = sum([int(item[i]) for item in input])
    gamma += '1' if c>len(input)/2 else '0'
    epsilon += '1' if c < len(input) / 2 else '0'

print(int(gamma,2)*int(epsilon,2))