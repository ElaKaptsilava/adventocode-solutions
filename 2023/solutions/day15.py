with open("../imputs/puzzle15.txt") as file:
    read = file.read().split(",")


def hush_code(step):
    start = 0
    for char in step:
        start += ord(char)
        start *= 17
        start %= 256
    return start


solution1 = sum(map(hush_code, read))
print(solution1)

boxes = [[] for _ in range(256)]
focal_lengths = {}
for step in read:
    if "=" in step:
        label, focal_length = step.split("=")
        box = hush_code(label)
        focal_lengths[label] = int(focal_length)
        if label in boxes[box]:
            label_index = boxes[box].index(label)
            boxes[box][label_index] = label

        else:
            boxes[box].append(label)

    if "-" in step:
        label = step[:-1]
        box = hush_code(label)
        if label in boxes[box]:
            boxes[box].remove(label)

solution2 = 0
for box_index, box in enumerate(boxes, start=1):
    for slot_index, label in enumerate(box, start=1):
        solution2 += box_index * slot_index * focal_lengths[label]
print(solution2)
