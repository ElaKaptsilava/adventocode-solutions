from copy import deepcopy
from typing import List

T = List[List[str]]


def expand_the_galaxy[T](puzzle: T) -> T:
    new_galaxy = deepcopy(puzzle)
    for OX, line in enumerate(puzzle):
        column, column_coordinates = [], []
        for OY in range(len(line)):
            column.append(puzzle[OY][OX])
            column_coordinates.append((OY, OX))
        if len(set(column)) == 1:
            for X, Y in column_coordinates:
                new_galaxy[X].insert(Y, '.')
        if len(set(line)) == 1:
            new_galaxy.insert(OX, line)
    return new_galaxy


def find_hashtag_coordinates(expanded_galaxy):
    coordinates = []
    for OX, line in enumerate(expanded_galaxy):
        for OY, char in enumerate(line):
            if char == '#':
                coordinates.append((OX, OY))
    return coordinates


with open('puzzle11.txt', 'r') as puzzle_input:
    galaxy = [list(line) for line in puzzle_input.read().split('\n')]
    expanded_galaxy = expand_the_galaxy(galaxy)
    hashtag_coordinates = find_hashtag_coordinates(expanded_galaxy)
    n = []
    for index, coordinates in enumerate(hashtag_coordinates):
        next_index = index + 1
        while next_index < len(hashtag_coordinates):
            x1, x2 = coordinates
            y1, y2 = hashtag_coordinates[next_index]
            n.append((abs(y1 - x1) + abs(y2 - x2)))
            next_index += 1
    # print(len(n))
    # x = 0
    # for y in range(len(hashtag_coordinates)-1, 0, -1):
    #     x += y
    # print(x)
    print(sum(n))

# 10876718
