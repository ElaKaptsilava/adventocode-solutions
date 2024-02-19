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
with open("../imputs/puzzle16.txt", "r") as grid:
    g = {}
    for row, line in enumerate(grid):
        for column, char in enumerate(line.strip()):
            g[complex(column, row)] = char


def fn(todo):
    passed = set()
    while todo:
        position, direction = todo.pop()
        while not (position, direction) in passed:
            passed.add((position, direction))
            position += direction
            get_ = g.get(position)
            match get_:
                case '|':
                    direction = 1j; todo.append((position, -direction))
                case '-':
                    direction = -1; todo.append((position, -direction))
                case '/':
                    direction = -complex(direction.imag, direction.real)
                case '\\':
                    direction = complex(direction.imag, direction.real)
                case None:
                    break

    return len(set(pos for pos, _ in passed)) - 1


print(fn([(-1, 1)]))