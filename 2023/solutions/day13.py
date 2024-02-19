with open("../imputs/pzl13.txt", "r") as puzzle:
    patterns = [list(map(list, img.split("\n"))) for img in puzzle.read().split("\n\n")]
    patterns_clm = [list(map(list, zip(*img))) for img in patterns]

point = 0
result = 0
while point < len(patterns):
    image, image_clm = patterns[point], patterns_clm[point]
    for index, line in enumerate(image):
        if index + 1 < len(image) and line == image[index + 1]:
            result += (index + 1) * 100
            break
    for index, line in enumerate(image_clm):
        if index + 1 < len(image_clm) and line == image_clm[index + 1]:
            result += index + 1
            break
    point += 1
print(result)
