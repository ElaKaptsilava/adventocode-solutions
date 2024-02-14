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
with open("../imputs/p10.txt") as file:
    maze = list(map(list, file.read().split("\n")))

start = "S"
exit_ = "E"
high = len(maze)
wight = len(maze[0])
directions = {
    "north": {("L", "|", "J", "S"): ["|", "7", "F", "S"]},
    "east": {("L", "-", "F", "S"): ["-", "7", "J", "S"]},
    "south": {("|", "7", "F", "S"): ["|", "L", "J", "S"]},
    "west": {("-", "7", "J", "S"): ["F", "-", "L", "S"]},
}


def find_start(maze):
    for row, line in enumerate(maze):
        if "".join(line).find(start) != -1:
            return row, line.index(start)


def is_allowed(pipe, pipe_to_connect, direction):
    if pipe == start and pipe_to_connect != ".":
        return True
    for current, to_connect in directions[direction].items():
        if pipe in current and pipe_to_connect in to_connect:
            return True
    return False


def go(maze, row=None, column=None, visited=None):
    if row is None or column is None:
        row, column = find_start(maze)
    if visited is None:
        visited = list()
    if maze[row][column] == start and len(visited)> 0:
        return True
    visited.append((row, column))
    if (
        row - 1 >= 0
        and (row - 1, column) not in visited
        and is_allowed(
            pipe=maze[row][column],
            pipe_to_connect=maze[row - 1][column],
            direction="north",
        )
    ):
        if go(maze, row - 1, column, visited):
            return True
    if (
        column + 1 < wight
        and (row, column + 1) not in visited
        and is_allowed(
            pipe=maze[row][column],
            pipe_to_connect=maze[row][column + 1],
            direction="east",
        )
    ):
        if go(maze, row, column + 1, visited):
            return True
    if (
        row + 1 < high
        and (row + 1, column) not in visited
        and is_allowed(
            pipe=maze[row][column],
            pipe_to_connect=maze[row + 1][column],
            direction="south",
        )
    ):
        if go(maze, row + 1, column, visited):
            return True
    if (
        column - 1 >= 0
        and (row, column - 1) not in visited
        and is_allowed(
            pipe=maze[row][column],
            pipe_to_connect=maze[row][column - 1],
            direction="west",
        )
    ):
        if go(maze, row, column - 1, visited):
            return True
    return False


print(go(maze))
# def go(maze, row=None, column=None, visited=None):
#     if row is None or column is None:
#         row, column = find_start(maze)
#     if visited is None:
#         visited = list()
#     if maze[row][column] == start and len(visited) > 0:
#         return True, len(visited)
#     if maze[row][column] != start:
#         visited.append((row, column))
#     print(row, column)
#     if row - 1 >= 0 and (row - 1, column) not in visited:
#         is_allow = is_allowed(pipe=maze[row][column], pipe_to_connect=maze[row - 1][column], direction="north")
#         if is_allow and go(maze, row - 1, column, visited):
#             return True
#     if column + 1 < wight and (row, column + 1) not in visited:
#         is_allow = is_allowed(pipe=maze[row][column], pipe_to_connect=maze[row][column + 1], direction="east")
#         if is_allow and go(maze, row, column + 1, visited):
#             return True
#     if row + 1 < wight and (row + 1, column) not in visited:
#         is_allow = is_allowed(pipe=maze[row][column], pipe_to_connect=maze[row + 1][column], direction="south")
#         if is_allow and go(maze, row + 1, column, visited):
#             return True
#     if column - 1 >= 0 and (row, column - 1) not in visited:
#         is_allow = is_allowed(pipe=maze[row][column], pipe_to_connect=maze[row][column - 1], direction="west")
#         if is_allow and go(maze, row, column - 1, visited):
#             return True
#     # if maze[row][column] == start and len(visited) > 0:
#     #     return (len(visited) + 1) / 2
#     # return False
#
