"""
    splitters :
    | -> up and down
    - -> left & right
    . -> continue as previous splitter
    / -> continue with previous splitter up or down
    \\ -> continue with previous splitter up or down

    For example:
            .|...\\....
            |.-.\\.....
            .....|-...
            ........|.
            ..........
            .........\
            ..../.\\..
            .-.-/..|..
            .|....-|.\\
            ..//.|....


"""
with open("../inputs/puzzle16.txt", "r") as grid:
    grid_ = {}
    for row, line in enumerate(grid):
        for column, char in enumerate(line.strip()):
            grid_[complex(column, row)] = char


def floor_will_be_lava(todo, grid):
    passed = set()
    while todo:
        position, direction = todo.pop()
        while not (position, direction) in passed:
            passed.add((position, direction))
            position += direction
            match grid.get(position):
                case "|":
                    direction = 1j
                    todo.append((position, -direction))
                case "-":
                    direction = 1
                    todo.append((position, -direction))
                case "/":
                    direction = -complex(direction.imag, direction.real)
                case "\\":
                    direction = complex(direction.imag, direction.real)
                case None:
                    break

    return len(set([x for x, y in passed])) - 1


print(floor_will_be_lava([(-1, 1)], grid_))

with open("../inputs/puzzle16.txt", "r") as grid:
    grid_ = {}
    for row, line in enumerate(grid):
        for column, char in enumerate(line.strip()):
            grid_[complex(column, row)] = char


def floor_will_be_lava(todo, grid):
    passed = set()
    while todo:
        position, direction = todo.pop()
        while not (position, direction) in passed:
            passed.add((position, direction))
            position += direction
            match grid.get(position):
                case "|":
                    direction = 1j
                    todo.append((position, -direction))
                case "-":
                    direction = 1
                    todo.append((position, -direction))
                case "/":
                    direction = -complex(direction.imag, direction.real)
                case "\\":
                    direction = complex(direction.imag, direction.real)
                case None:
                    break


s = []
directions_ = []
for i in range(len(grid_)):
    s.append(floor_will_be_lava([(-i, 1)], grid_))
