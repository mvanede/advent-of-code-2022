from utils import Parser
from utils.lib import get_timer, panswer, pruntime, get_elements_of_length
_ST = get_timer()

f = open("ass-day-8-input.txt", "r")
lines = Parser.split_by(f.read(), "\n", " | ", " ", conv_func=None)  # lambda x:int(x)


def get_key(s):
    sorted_characters = sorted(s)
    return ''.join(sorted_characters)


total_sum = 0
for signals, output in lines:

    # Find ONE, FOUR , SEVEN, EIGHT (unique lengths)
    one = get_elements_of_length(2, signals)[0]
    signals.remove(one)

    seven = get_elements_of_length(3, signals)[0]
    signals.remove(seven)

    four = get_elements_of_length(4, signals)[0]
    signals.remove(four)

    eight = get_elements_of_length(7, signals)[0]
    signals.remove(eight)

    # FOUR is entirely part of NINE (and only NINE)
    for s in signals:
        if all(item in list(s) for item in list(four)):
            nine = s
            break
    signals.remove(nine)

    # SEVEN is part of THREE, NINE en ZERO. The element of length 5 is then THREE,  element of length 6 is ZERO
    elems = []
    for s in signals:
        if all(item in list(s) for item in list(seven)):
            elems.append(s)
    three = get_elements_of_length(5, elems)[0]
    signals.remove(three)

    zero = get_elements_of_length(6, elems)[0]
    signals.remove(zero)

    # Remaining element of length 6 is six
    six = get_elements_of_length(6, signals)[0]
    signals.remove(six)

    # FIVE and TWO remain. Length diff between FIVE and SIX is 1, between TWO and SIX 2
    for s in signals:
        z = list(set(six) - set(s))
        if len(z) == 1:
            five = s
        elif len(z) == 2:
            two = s
        else:
            print("PANIC, shouldnt occur")

    vals = {
        get_key(one): 1,
        get_key(two): 2,
        get_key(three): 3,
        get_key(four): 4,
        get_key(five): 5,
        get_key(six): 6,
        get_key(seven): 7,
        get_key(eight): 8,
        get_key(nine): 9,
        get_key(zero): 0
    }

    retval = 0
    i = 3
    for idx, o in enumerate(output):
        x = vals[get_key(o)]
        retval += x*(10**i)
        i -= 1
    total_sum += retval

panswer(total_sum)
pruntime(_ST)