import itertools

with open("puzzle8.txt", "r") as puzzle:
    instructions, *lines = puzzle.read().split("\n\n")
    instructions = itertools.cycle(" ".join(instructions).split())
    PUZZLE = dict()
    for line in lines[0].split("\n"):
        for sep in "()=l,":
            line = line.replace(sep, "")
        PUZZLE[line.split(" ")[0]] = {
            "R": line.split(" ")[-2],
            "L": line.split(" ")[-1],
        }
count = 0
step = "AAA"
while step != "ZZZ":
    ways = PUZZLE[step]
    step = ways[next(instructions)]
    count += 1
print(count)
