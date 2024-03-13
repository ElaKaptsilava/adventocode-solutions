def solve_1(plan, start):
    directions = (-1j, 1, 1j, -1)
    todo = {
        start,
    }
    for _ in range(10):
        new_todo = set()
        while todo:
            pos = todo.pop()
            for dir in directions:
                if (step := pos + dir) and plan.get(step) == ".":
                    new_todo.add(step)
                if not plan.get(step):
                    print(step)
        todo = new_todo
    return len(todo)


def solve_2(plan, start, row, column):
    x = 0
    directions = (-1j, 1, 1j, -1)
    todo = {
        start,
    }
    print(plan.get(4j))
    for _ in range(10):
        new_todo = set()
        while todo:
            pos = todo.pop()
            for dir in directions:
                step = pos + dir
                if not plan.get(step):
                    row_index, column_index = int(step.imag), int(step.real)
                    if row_index < 0:
                        step = complex(column_index, row)
                    elif column_index > column:
                        step = complex(0, row_index)
                    elif column_index < 0:
                        step = complex(column, row_index)
                    elif row_index > row:
                        step = complex(column_index, 0)
                if plan.get(step) == ".":
                    new_todo.add(step)
        todo = new_todo
        x += len(todo)
    return x


with open("../inputs/input21.txt") as file:
    start, plan = None, {}
    read_file = file.read().split("\n")
    for row, line in enumerate(read_file):
        for column, char in enumerate(line):
            if char == "S":
                start = complex(column.real, row.real)
                char = "."
            plan[complex(column.real, row.real)] = char
    print(solve_2(plan, start, len(read_file) - 1, len(read_file[0]) - 1))

print(0j - 1j)
