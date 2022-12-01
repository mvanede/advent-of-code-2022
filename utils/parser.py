from pprint import pprint
from utils.grid import Grid


class Parser:
    @classmethod
    def get_int_grid(cls, _input ):
        grid = cls.split_by(_input, "\n", " ", conv_func=lambda x: int(x))
        pprint(grid)
        return Grid(grid)

    @classmethod
    def group_by_double_newline(cls, _input, conv_func=None):
        return cls.split_by(_input, "\n\n", "\n", conv_func=conv_func)

    @classmethod
    def split_by(cls, _input, *args, conv_func=None):
        if not len(args):
            if type(_input) is list:
                return list(map(conv_func, _input)) if conv_func else _input
            else:
                return conv_func(_input) if conv_func else _input

        if type(_input) is not list:
            if args[0] == '':
                return cls.split_by(list(_input), *args[1:], conv_func=conv_func)
            else:
                return cls.split_by(_input.split(args[0]), *args[1:], conv_func=conv_func)

        ret_val = []
        for line in _input:
            # Split if there's a separator, otherwise cast to list (string to list of characters)
            parts = line.split(args[0]) if args[0] else list(line)
            cur_line = []
            for part in parts:
                cur_line.append(cls.split_by(part, *args[1:], conv_func=conv_func))

            ret_val.append(cur_line)
        return ret_val
