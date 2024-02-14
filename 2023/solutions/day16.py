"""
    splitters :
    | -> up & down
    - -> left & right
    . -> continue as previous splitter
    / -> continue with previous splitter up or down
    \\ -> continue with previous splitter up or down

    For example:
            .|...\\....
            |.-.\\.....
            .....|-...
            ........|.
            ..........
            .........\
            ..../.\\..
            .-.-/..|..
            .|....-|.\\
            ..//.|....


"""

splitters = ["|", "\\", "-", "/"]

with open("../imputs/puzzle16.txt", "r") as file:
    read = list(map(list, file.read().split("\n")))

row = 0
column = 0
