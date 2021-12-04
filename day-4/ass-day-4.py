f = open("ass-day-4-input.txt", "r")
lines = f.read().split("\n\n")
numbers = lines[0].split(',')

boards = []
for l in lines[1:]:
    board = [sl.split() for sl in l.split("\n") ]
    boards.append(board)


def has_bingo_row(board):
    for row in board:
        uniq = list(set(row))
        if uniq[0] == '-' and len(uniq) == 1:
            return True

def has_bingo_col(board):
    for i in range(0, len(board[0])):
        col = [row[i] for row in board]
        if has_bingo_row([col]):
            return True
    return False


def get_board_sum(board):
    return sum([sum([int(i) for i in row if i!='-']) for row in board])


def play(_numbers, _boards):
    for n in _numbers:
        for _board in _boards:
            for row in _board:
                try:
                    row[row.index(n)] = '-'
                except ValueError:
                    pass

            if has_bingo_row(_board) or has_bingo_col(_board):
                print("BINGO at " + n )
                return get_board_sum(_board) * int(n)


print (play(numbers, boards))