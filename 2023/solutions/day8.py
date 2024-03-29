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
count = 0
step = "AAA"
print(list(instructions))
while step != "ZZZ":
    ways = puz[step]
    step = ways[next(instructions)]
    count += 1
z = list(zip([1, 2, 3, 4, 5, 6, 7, 8, 9], range(1, 10)))
