with open("../inputs/input18.txt", "r") as plan:
    dig_plan = plan.read().split("\n")
    dig_plan = list(map(lambda item: item.split(" "), dig_plan))
    directions, steps, colors = list(map(list, zip(*dig_plan)))
    steps = list(map(int, steps))


def complete_object(border, y, x):
    north, east, south, west = (-1, 0), (0, 1), (1, 0), (0, -1)
    dir = {"U": north, "R": east, "D": south, "L": west}
    while len(directions) > 0:
        direct, step = directions.pop(0), steps.pop(0)
        yd, xd = dir[direct]
        for _ in range(step):
            border.append((y, x))
            y += yd
            x += xd
    return border


laguna = complete_object(list(), y=0, x=0)
area = 0

for i in range(len(laguna) - 1):
    x1, y1 = laguna[i]
    x2, y2 = laguna[i + 1]
    area += x1 * y2 - x2 * y1

perimeter = len(laguna)
interior_area = abs(area) // 2 - perimeter // 2 + 1
print("Part 1:", interior_area + perimeter)

# matplotlib.image.imsave('name.png', numpy.array(arr))

directions = list(map(lambda color: int(color[-2]), colors))
steps = list(map(lambda color: int(color[2:-2], 16), colors))


def complete_object(border, y, x):
    north, east, south, west = (-1, 0), (0, 1), (1, 0), (0, -1)
    dir = {3: north, 0: east, 1: south, 2: west}
    while len(directions) > 0:
        direct, step = directions.pop(0), steps.pop(0)
        yd, xd = dir[direct]
        for _ in range(step):
            border.append((y, x))
            y += yd
            x += xd
    return border


laguna = complete_object(list(), y=0, x=0)
area = 0

for i in range(len(laguna) - 1):
    x1, y1 = laguna[i]
    x2, y2 = laguna[i + 1]
    area += x1 * y2 - x2 * y1

perimeter = len(laguna)
interior_area = abs(area) // 2 - perimeter // 2 + 1
print("Part 2:", interior_area + perimeter)
