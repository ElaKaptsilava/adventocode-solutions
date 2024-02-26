with open("../inputs/pzl13.txt", "r") as puzzle:
    row_pattern = [list(map(list, img.split("\n"))) for img in puzzle.read().split("\n\n")]
    column_patterns = [list(map(list, zip(*img))) for img in row_pattern]

point = 0
result = 0

current_axis = 0

axis = {0: 1, 1: 0}

while point < len(row_pattern):
    patterns = {0: column_patterns[point], 1: row_pattern[point]}
    data = patterns[current_axis]
    for index, line in enumerate(data):
        if index + 1 == len(data):
            current_axis = axis[current_axis]
            break
        elif line == data[index + 1]:
            results = {0: index + 1, 1: (index + 1) * 100}
            result += results[current_axis]
            current_axis = axis[current_axis]
            point += 1
            break
print(result)


