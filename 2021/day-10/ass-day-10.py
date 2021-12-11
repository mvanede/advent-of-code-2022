from utils import Parser
from utils.lib import get_timer, panswer, pruntime
_ST = get_timer()

commands = Parser.split_by(open("ass-day-10-input.txt", "r").read(), "\n", '', conv_func=None)  # lambda x:int(x)
syntax = { '{':'}', '[': ']', '(':')', '<': '>'}
values = {')': 3, ']': 57, '}': 1197, '>': 25137}


def validate_command(command):
    state = []
    for c in command:
        if c in syntax.keys():
            state.append(c)
        elif c in syntax.values():
            # closing, should match last opening in c
            if syntax[state[-1]] == c:
                # matching, remove
                state.pop()
            else:
                print("Expected {}, but found {} instead".format(syntax[state[-1]], c))
                return values[c]

    # Incomplete if len(state)>0. Return 0 to not affect the sum
    return 0


invalid_entries = [validate_command(command) for command in commands]
panswer(sum(invalid_entries))
pruntime(_ST)


