import re
from functools import reduce

with open("../inputs/puzzle_input_5.txt") as puzzle:
    seeds, *mappings = puzzle.read().split("\n\n")
    seeds = map(int, seeds.split()[1:])


def day_5_1(start, mapping):
    for m in mapping.split("\n")[1:]:
        destination_range, source_range, len_range = map(int, m.split())
        delta = start - source_range
        if delta in range(len_range):
            return destination_range + delta
    return start


x = list(reduce(day_5_1, mappings, seed) for seed in seeds)
print(x)
print(min(x))
