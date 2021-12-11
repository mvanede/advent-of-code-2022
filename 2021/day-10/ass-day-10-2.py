from utils import Parser
from utils.lib import get_timer, panswer, pruntime
import math
_ST = get_timer()

commands = Parser.split_by(open("ass-day-10-input.txt", "r").read(), "\n", '', conv_func=None)  # lambda x:int(x)
syntax = { '{':'}', '[': ']', '(':')', '<': '>'}
values = {')': 1, ']': 2, '}': 3, '>': 4}


def get_closing_score(state):
    state.reverse()
    closings = []
    for s in state:
        closings.append(syntax[s])

    score = 0
    for c in closings:
        score *= 5
        score += values[c]
    return score


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
                # IGNORE WRONG SYNTAX
                return

    # Incomplete if len(state)>0
    if len(state):
        return get_closing_score(state)


autocomplete_scores = []
for command in commands:
    v = validate_command(command)
    if v:
        autocomplete_scores.append(v)

autocomplete_scores.sort()
middle_index = int((len(autocomplete_scores) - 1)/2)

panswer(autocomplete_scores[middle_index])
pruntime(_ST)
