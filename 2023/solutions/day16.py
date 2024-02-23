"""
    splitters :
    | -> up & down
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

with open("../inputs/puzzle16.txt", "r") as grid:
    read = list(map(list, grid.read().split('\n')))


def floor_will_be_lava(todo):
    passed = set()
    while todo:
        position, direction = todo.pop()
        while not (position, direction) in passed:
            passed.add((position, direction))
            position += direction
            match grid_.get(position):
                case '|':
                    direction = 1j
                    todo.append((position, -direction))
                case '-':
                    direction = 1
                    todo.append((position, -direction))
                case '/':
                    direction = -complex(direction.imag, direction.real)
                case '\\':
                    direction = complex(direction.imag, direction.real)
                case None:
                    break

    return len(set([x for x, y in passed])) - 1


print(floor_will_be_lava([(-1, 1)]))

directions_ = []
for i in range(len(read)):
    u, d = 0, -1
    directions_.append((complex(-1, i.real), 1))
    directions_.append((complex(0, i.real), -1))
    directions_.append((complex(i, u.real), -1j))
    directions_.append((complex(i, d.real), 1j))

tiles = []
for direction in directions_:
    tiles.append(floor_will_be_lava([direction]))
print(max(tiles))
