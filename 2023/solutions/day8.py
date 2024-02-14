import itertools
from collections import OrderedDict

with open("../imputs/puzzle8.txt", "r") as puzzle:
    instructions, *lines = puzzle.read().split("\n\n")
    instructions = itertools.cycle(list(instructions))
    puz = OrderedDict()
    for line in lines[0].split("\n"):
        for sep in "()=l,":
            line = line.replace(sep, "")
        puz[line.split(" ")[0]] = {
            "R": line.split(" ")[-2],
            "L": line.split(" ")[-1],
        }
count = 0
step = "AAA"
while step != "ZZZ":
    ways = puz[step]
    step = ways[next(instructions)]
    count += 1
print(count)
z = list(zip([1, 2, 3, 4, 5, 6, 7, 8, 9], range(1, 10)))
print(z)
