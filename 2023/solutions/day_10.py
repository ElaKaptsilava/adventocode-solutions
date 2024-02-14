import dataclasses
from collections import defaultdict

# Marcin Senk
# 10:41
# > sprawdzamy prawa strone czy sie laczy z S
# idziemy na prawo [0,1]
# sprawdzamy czy prawa strona laczy sie z [0,1]
# trzeba pamietac ze z lewej przyszlismy
# Marcin Senk
# 10:42
# > TA koordynata juz byla odwiedzona
# idziemy do [1,1]
# dwie opcje:
# dojdziemy do slepego zaułku
# wówczas wracamy do S i sprawdzamy dół
# Marcin Senk
# 10:43
# możemy wrócić do S
# mamy pętle
# Marcin Senk
# 10:44
# sprawdzamy dlugosc petli
# idziemy do elementu = polowie dlugosci petli
# w stosunku do S


PASSED = defaultdict(list)
# Z = {"N": "S", "W": "E", "E": "W", "S": "N"}
# v, h = {"", "S"}, {"W", "E"}


@dataclasses.dataclass
class Coordinate:
    row: int
    column: int


@dataclasses.dataclass
class SymbolDirections:
    symbols_direction = {
        "|": ["U", "D"],
        "-": ["L", "R"],
        "L": ["U", "D"],
        "J": ["U", "L"],
        "7": ["L", "D"],
        "F": ["R", "D"],
    }
    symbol: str

    @property
    def top(self):
        return self.symbols_direction[self.symbol][0]

    @property
    def bottom(self):
        return self.symbols_direction[self.symbol][1]


with open("../imputs/p10.txt", "r") as file:
    r_file = file.read()
    start, scheme = None, []
    for x, line in enumerate(r_file.split("\n")):
        if (y := line.find("S")) != -1:
            start = Coordinate(x, y)
        scheme.append(list(line))
    print(scheme)
    print(start)


def check_coordinates(symbol, coordinates):
    global PASSED
    return False if PASSED[symbol] and coordinates in PASSED[symbol] else True


def filter_ways(pivot_point, *ways):
    ways = [way for way in ways if way and way != "."]
    if pivot_point == "S":
        return ways
    for way in ways:
        d1, d2 = SymbolDirections(pivot_point), SymbolDirections(way)
        x1y1, x2y2 = (d1.top, d1.bottom), (d2.top, d2.bottom)

    return None


vertical, horizontal = start.row, start.column
while True:
    pivot_point = scheme[vertical][horizontal]
    up = scheme[vertical + 1][horizontal] if vertical != -1 else None
    down = scheme[vertical - 1][horizontal] if vertical != 0 else None
    left = scheme[vertical][horizontal - 1] if horizontal != 0 else None
    right = scheme[vertical][horizontal + 1] if horizontal != -1 else None
    ways = filter_ways(pivot_point, *(up, down, left, right))
    print(ways)
    for way in ways:
        print(SymbolDirections(way).top)
    break
