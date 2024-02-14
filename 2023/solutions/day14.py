from copy import deepcopy

with open("../imputs/puzzle14.txt", "r") as file:
    input = tuple(file.read().splitlines())


def slide_rocks_north(grid):
    grid = list(map("".join, zip(*grid)))
    new_grid = []
    for row in grid:
        ordered_rows = []
        for group in row.split("#"):
            ordered_rows.append("".join(sorted(group, reverse=True)))
        new_grid.append("#".join(ordered_rows))
    return tuple(list(map("".join, zip(*new_grid))))


def cycle(grid):
    for _ in range(4):
        grid = slide_rocks_north(grid)
        grid = tuple(["".join(row[::-1]) for row in zip(*grid)])

    return grid


solution2 = 0

grid_slided = slide_rocks_north(input)
solution1 = 0
l = len(grid_slided)
for line in grid_slided:
    if count_o := line.count("O"):
        solution1 += count_o * l
        l -= 1
print(solution1)

CYCLES = 1000000000
grid = deepcopy(input)
for i in range(CYCLES):
    grid_cycle = cycle(grid)
    grid = grid_cycle
    print("end: ", i)

l = len(grid)
for line in grid:
    if count_o := line.count("O"):
        solution2 += count_o * l
        l -= 1

print(solution2)
