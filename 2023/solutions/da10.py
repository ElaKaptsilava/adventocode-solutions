"""
    Implementations pipes:
        | -> north and south.
        - -> east and west.
        L -> north and east.
        J -> north and west.
        7 -> south and west.
        F -> south and east
        . is ground
        S -> start

    Can be connected:
        if way go to 'east' that way will be continuo with point which looks at 'west'
        if way go to 'west' that way will be continuo with point which looks at 'east'
        if way go to 'north' that way will be continuo with point which looks at 'earth'
        if way go to 'south' that way will be continuo with point which looks at 'north'

    Variables: high, wight, start, exit_, path, symbols_direction, permission

    Class: SymbolDirections(pipe)
            - @property def top -> return the pipe top direction
            - @property def bottom -> return the pipe bottom direction

    Solution:
    - (row, column) not in visited
        1. Explore the north neighboring point
            - condition: row + 1 < HIGH,
        2. Explore the east neighboring point
            - condition: column + 1 < WIGHT,
        3. Explore the south neighboring point
            - condition: row - 1 >= 0,
        4. Explore the west neighboring point
            - condition: column - 1 >= 0,

"""
with open("../inputs/puzzle10.txt", "r") as grid:
    pipe_maze, start = {}, None
    for row, line in enumerate(grid):
        for column, char in enumerate(line.strip()):
            pipe_maze[complex(column, row)] = char
            if char == 'S':
                start = complex(column, row)

directions_item = {
    -1j: {("L", "|", "J"): ["|", "7", "F"]},
    1: {("L", "-", "F"): ["-", "7", "J"]},
    1j: {("|", "7", "F"): ["|", "L", "J"]},
    -1: {("-", "7", "J"): ["F", "-", "L"]},
}


def is_allowed(pos: complex, direction: complex, pipe_maze: dict) -> float:
    pipe, pipe_to_connect = pipe_maze[pos], pipe_maze[pos + direction]
    if pipe_to_connect == 'S':
        return True
    if pipe_to_connect != ".":
        for current, to_connect in directions_item[direction].items():
            if pipe in current and pipe_to_connect in to_connect:
                return True
    return False


def go(start: complex, pipe_maze: dict) -> float:
    result = []
    ways = [start + direct for direct in list(directions_item)]
    for way in ways:
        todo, passed = [way], []
        while todo:
            if (position := todo.pop()) in passed:
                break
            if pipe_maze[position] == 'S':
                if len(passed) > 5:
                    result.append(len(passed) + 1)
                    break
                else:
                    continue
            passed.append(position)
            for direct in directions_item:
                if position + direct not in passed and is_allowed(position, direct, pipe_maze):
                    todo.append(position + direct)
    return max(result) / 2


print(go(start, pipe_maze))
# Part 1: 6867
# Part 2: 608