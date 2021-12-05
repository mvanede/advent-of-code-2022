from pprint import pprint
class Parser:
    @classmethod
    def to_int_grid(cls):
        return ""

    @classmethod
    def split_by(cls, input, conv_func=None,  *args):
        if not len(args):
            return list(map(conv_func, input)) if conv_func else input

        if type(input) is not list:
            return cls.split_by(input.split(args[0]), conv_func, *args[1:])

        ret_val = []
        for line in input:
            cur_line = []
            for part in line.split(args[0]):
                cur_line.append(cls.split_by(part, conv_func,*args[1:]))
            ret_val.append(cur_line)

        return ret_val