import itertools


depth_of_nested_lists = lambda L: isinstance(L, list) and max(map(depth_of_nested_lists, L)) + 1

flatten_nested_lists = lambda x: [i for e in x for i in (flatten_nested_lists(e) if isinstance(e,list) else [e])]

max_in_list = lambda lst: max(flatten_nested_lists(lst))
