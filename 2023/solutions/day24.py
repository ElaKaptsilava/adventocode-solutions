"""
    Each line of text uses the format: px py pz @ vx vy vz.

    Part 1:
    pos1: px1, py1 = (px, py) | px2, py2 = (px+vx, py+vy)
    pos2: px1, py1 = (px, py) | px2, py2 = (px+vx, py+vy)

    m1, m2 = (py2 - py1)/(px2 - px1)
    b1, b2 = py1 - (m *px1)

    if (m1 < 0 and m2 < 1) or (m1 < 0 and m2 < 1):
        Lines are parallel.
    else:
        y = mx + b
        x0 = (b2 - b1)/(m1 - m2)
        y0 = m1 * ( x0 ) + b1
"""
import copy
import pprint
from collections import deque
from itertools import combinations

with open("../inputs/input24.txt") as file:
    puzzle = list()
    for line in file.read().replace(" ", "").split("\n"):
        position, velocity = line.split("@")
        puzzle.append(
            [list(map(int, position.split(","))), list(map(int, velocity.split(",")))]
        )
    comb = deque(combinations(puzzle, 2))
# down_line = 200_000_000_000_000
# up_line = 400_000_000_000_000
up_line = 27
down_line = 7


def calculate_cross(b1, b2, m1, m2):
    x0 = (b2 - b1) / (m1 - m2)
    y0 = m1 * x0 + b1
    return round(x0, 3), round(y0, 3)


def slope_factor(p1: tuple, p2: tuple):
    px1, py1 = p1
    px2, py2 = p2
    return (py2 - py1) / (px2 - px1)


def axial_displacement_y(py1, m, px1):
    return py1 - (m * px1)


def calculate_coordinates(pos):
    px, py, _ = pos[0]
    vx, vy, _ = pos[1]
    return (px, py), (px + vx, py + vy)

def main():
    c = []
    counter = 0
    while comb:
        combination = list(comb.popleft())
        com = copy.deepcopy(combination)
        slope_factors = []
        axial = []
        while combination:
            point1, point2 = calculate_coordinates(combination.pop())
            slope = slope_factor(point1, point2)
            axial_displacement = axial_displacement_y(point1[1], slope, point1[0])
            slope_factors.append(slope)
            axial.append(axial_displacement)
        if all(m < 0 for m in slope_factors) or all(m > 0 for m in slope_factors):
            # print('Lines are parallel!')
            continue
        cross = calculate_cross(
            b1=axial[0], b2=axial[1], m1=slope_factors[0], m2=slope_factors[1]
        )
        if all(down_line <= point <= up_line for point in cross):
            c.append([cross, com])
            counter += 1
    pprint.pprint(c)
    print(counter)

main()
