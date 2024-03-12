def get_maze(read_file: list[str]):
    start_way, exit_way = 'S', 'E'
    maze = {}
    for row, line in enumerate(read_file):
        for col, char in enumerate(line):
            if row == 0 and char == '.':
                char = start_way
                start_way = complex(col, row)
            elif row == len(read_file) - 1 and char == '.':
                char = exit_way
                exit_way = complex(col, row)
            maze[complex(col, row)] = char
    return maze, start_way, exit_way


def find_largest_way(maze: dict[complex, str], start) -> int:
    ways = list()
    todo = [start]
    passed = set()
    count = 0
    while todo:
        directions = [-1j, 1, 1j, -1]
        pos = todo.pop()
        passed.add(pos)
        if maze.get(pos) == 'E':
            ways.append(count)
            count = 0
        for direction in directions:
            next_pos = pos + direction
            if next_pos not in passed and maze.get(next_pos) not in [None, '#', 'S']:
                todo.append(next_pos)
                count += 1
            passed.add(next_pos)
    return ways

with open('../inputs/input23.txt') as file:
    read_file = file.read().split('\n')
    maze, start, exit_ = get_maze(read_file)
    print(find_largest_way(maze, start))
