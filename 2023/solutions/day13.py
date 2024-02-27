with open("../inputs/pzl13.txt", "r") as puzzle:
    row_pattern = [
        list(map(list, img.split("\n"))) for img in puzzle.read().split("\n\n")
    ]
    column_patterns = [list(map(list, zip(*img))) for img in row_pattern]

point, result = 0, 0
current_axis, axis = 0, {0: 1, 1: 0}
while point < len(row_pattern):
    patterns = {0: column_patterns[point], 1: row_pattern[point]}
    data = patterns[current_axis]
    for index, line in enumerate(data):
        if index + 1 < len(data) and line == data[index + 1]:
            results = {0: index + 1, 1: (index + 1) * 100}
            result += results[current_axis]
            point += 1
            break
    current_axis = axis[current_axis]

print(result)
