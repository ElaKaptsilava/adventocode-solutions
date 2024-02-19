from typing import List

T = List[List[str]]


def expand_the_galaxy[T](puzzle: T) -> T:
    point1 = 0
    while point1 < len(puzzle[0]):
        column = [puzzle[index][point1] for index in range(len(puzzle))]
        if len(set(column)) == 1:
            for X in range(len(puzzle)):
                puzzle[X].insert(point1, "../11")
            point1 += 1
        point1 += 1
    point1 = 0
    while point1 < len(puzzle):
        line = puzzle[point1]
        if len(set(line)) == 1:
            puzzle.insert(point1, line)
            point1 += 1
        point1 += 1
    return puzzle


def find_hashtag_coordinates(expanded_galaxy):
    coordinates = []
    for x, line in enumerate(expanded_galaxy):
        for y, char in enumerate(line):
            if char == "#":
                coordinates.append((x, y))
    return coordinates


def calculate_distance(hashtag_coordinates):
    result = 0
    for index, coordinates in enumerate(hashtag_coordinates):
        next_index = index + 1
        while next_index < len(hashtag_coordinates):
            x1, x2 = coordinates
            y1, y2 = hashtag_coordinates[next_index]
            result += abs(y1 - x1) + abs(y2 - x2)
            next_index += 1
    return result


with open("../inputs/puzzle11.txt", "r") as puzzle_input:
    galaxy = [list(line) for line in puzzle_input.read().split("\n")]
    expanded_galaxy = expand_the_galaxy(galaxy)
    hashtag_coordinates = find_hashtag_coordinates(expanded_galaxy)
    x = calculate_distance(hashtag_coordinates)
    print(x)


# 10885634


def older_the_galaxy[T](puzzle: T) -> T:
    point1 = 0
    while point1 < len(puzzle[0]):
        column = [puzzle[index][point1] for index in range(len(puzzle))]
        if len(set(column)) == 1:
            for _ in range(1000000):
                for X in range(len(puzzle)):
                    puzzle[X].insert(point1, "../11")
                point1 += 1
            print("Done 1 part")
        point1 += 1
    point1 = 0
    while point1 < len(puzzle):
        line = puzzle[point1]
        if len(set(line)) == 1:
            for _ in range(1000000):
                puzzle.insert(point1, line)
                point1 += 1
            print("Done 2 part")

        point1 += 1
    print("Done")

    return puzzle


with open("../inputs/puzzle11.txt", "r") as puzzle_input:
    galaxy = [list(line) for line in puzzle_input.read().split("\n")]
    expanded_galaxy = older_the_galaxy(galaxy)
    hashtag_coordinates = find_hashtag_coordinates(expanded_galaxy)
    x = calculate_distance(hashtag_coordinates)
    print(x)
