import queue

with open("../inputs/puzzle9.txt", "r") as puzzle:
    lines = puzzle.read().split("\n")
    lines = [list(map(int, line.split(" "))) for line in lines]


def mirage_maintenance(pzl):
    score = 0
    for line in pzl:
        step = 0
        sequences = []
        while set(line) != {
            0,
        }:
            sequences.append(line)
            line = [line[ind + 1] - line[ind] for ind in range(len(line) - 1)]
        for seq in sequences[::-1]:
            step = step + seq[-1]
            seq.append(step)
        score += step


mirage_maintenance(lines)


def mirage_maintenance_2(pzl):
    score = 0
    for line in pzl:
        step = 0
        sequences = []
        while set(line) != {
            0,
        }:
            sequences.append(line)
            line = [line[ind + 1] - line[ind] for ind in range(len(line) - 1)]

        for seq in sequences[::-1]:
            step = seq[0] - step
            seq.insert(0, step)

        score += step
