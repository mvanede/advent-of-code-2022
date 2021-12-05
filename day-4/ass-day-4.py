from utils import Parser, Grid
from typing import List


f = open("ass-day-4-input.txt", "r")
lines = Parser.split_by(f.read(), "\n\n", conv_func=None)
numbers = lines[0].split(',')
boards = [Grid(b) for b in Parser.split_by(lines[1:], "\n", None, conv_func=lambda x:int(x))]


def has_bingo_row(board:Grid):
    for row in board.rows:
        uniq = list(set(row))
        if uniq[0] == '-' and len(uniq) == 1:
            return True


def has_bingo_col(board:Grid):
    for col in board.cols:
        uniq = list(set(col))
        if uniq[0] == '-' and len(uniq) == 1:
            return True
    return False


def play(_numbers, _boards:List[Grid]):
    for n in _numbers:
        for _board in _boards:
            _board.replace_all(int(n), '-')

            if has_bingo_row(_board) or has_bingo_col(_board):
                return _board.get_sum_if(lambda x:x!='-') * int(n)


print (play(numbers, boards))