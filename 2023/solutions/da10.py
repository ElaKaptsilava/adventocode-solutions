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
with open("../imputs/puzzle10.txt", "r") as grid:
    g = {}
    start = {}
    for row, line in enumerate(grid):
        for column, char in enumerate(line.strip()):
            g[complex(column, row)] = char
            if char == 'S':
                start[char] = complex(column, row)

directions_item = {
    -1j: {("L", "|", "J"): ["|", "7", "F"]},
    1: {("L", "-", "F"): ["-", "7", "J"]},
    1j: {("|", "7", "F"): ["|", "L", "J"]},
    -1: {("-", "7", "J"): ["F", "-", "L"]},
}


def is_allowed(pos, direction):
    pipe, pipe_to_connect = g[pos], g[pos + direction]
    if pipe_to_connect not in [".", 'S']:
        for current, to_connect in directions_item[direction].items():
            if pipe in current and pipe_to_connect in to_connect:
                return True
    return False


def go(start):
    result = []
    ways = [start + direct for direct in list(directions_item)]
    p = 0
    while p < len(ways):
        passed = []
        todo = [ways[p]]
        while todo:
            position = todo.pop()
            if position in passed:
                break
            passed.append(position)
            point = 0
            while point < 4:
                direct = list(directions_item)[point]
                if g[position + direct] == 'S' and len(passed) > 5:
                    result.append(len(passed))
                    todo.clear()
                    break
                if position + direct not in passed and is_allowed(position, direct):
                    todo.append(position + direct)
                point += 1
        p += 1
    print(result)
    return max(result) / 2


print(go(start['S']))
