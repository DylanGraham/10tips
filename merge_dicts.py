import timeit
from functools import partial


def merge_dicts():
    d1 = {'aaa': 1}
    d2 = {'bbb': 2}
    d3 = {'ccc': 3}
    return {**d1, **d2, **d3}


times = timeit.Timer(partial(merge_dicts)).repeat(3, 1000)

time_taken = min(times) / 1000

print(time_taken)

