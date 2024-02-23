import itertools
from collections import OrderedDict

with open("../inputs/puzzle8.txt", "r") as puzzle:
    instructions, *lines = puzzle.read().split("\n\n")
    instructions = itertools.cycle(list(instructions))
    puz = OrderedDict()
    for line in lines[0].split("\n"):
        for sep in "()=l,":
            line = line.replace(sep, "")
        puz[line.split(" ")[0]] = {
            "L": line.split(" ")[-2],
            "R": line.split(" ")[-1],
        }

steps = [step for step in puz if step.endswith('A')]
count = 0
while True:
    base, instruction = set(), next(instructions)
    for i, step in enumerate(steps):
        ways = puz[step]
        step = ways[instruction]
        if step.endswith('Z'):
            base.add(True)
        else:
            base.add(False)
        steps[i] = step
    count += 1
    if base == {True, }:
        break

print(count)
