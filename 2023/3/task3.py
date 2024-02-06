import re


def task_3_1():
    with open("task_3.txt") as file:
        read_file = file.read()
        lines = read_file.split("\n")

        symbol_adjacent = []
        for line_index, line in enumerate(lines):
            symbols_location = re.finditer(r"[^.\d]", line)
            for match in symbols_location:
                for row in range(line_index - 1, line_index + 2):
                    for column in range(match.start() - 1, match.end() + 1):
                        symbol_adjacent.append((row, column))

        result = 0
        for line_index, line in enumerate(lines):
            numbers_location = re.finditer(r"\d+", line)
            for number_location in numbers_location:
                is_engine_part = any(
                    (line_index, location) in symbol_adjacent
                    for location in range(*number_location.span())
                )
                if is_engine_part:
                    result += int(number_location.group())

        return result


# Part 1: 544664
# Part 2: 84495585


def task_3_2():
    with open("task_3.txt") as file:
        read_file = file.read()
        lines = read_file.split("\n")
        gears = {}
        for line_index, line in enumerate(lines):
            symbols_location = re.finditer(r"[*]", line)
            for match in symbols_location:
                gears[(line_index, match.start())] = []

        result = 0
        for line_index, line in enumerate(lines):
            numbers_location = re.finditer(r"\d+", line)
            for number_location in numbers_location:
                for row in range(line_index - 1, line_index + 2):
                    for column in range(
                        number_location.start() - 1, number_location.end() + 1
                    ):
                        if (row, column) in gears:
                            gears[(row, column)].append(int(number_location.group()))

        for location, numbers in gears.items():
            if len(numbers) == 2:
                result += numbers[0] * numbers[1]

        return result


print(task_3_2())
