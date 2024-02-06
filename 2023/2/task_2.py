"""12 red cubes, 13 green cubes, and 14 blue cubes."""

import re

red, green, blue = 12, 13, 14


def filter_games(item):
    amount, color = item
    return (
        (int(amount) > red and color == "red")
        or (int(amount) > green and color == "green")
        or (int(amount) > blue and color == "blue")
    )


def task_2_1():
    all_games = 0
    with open("task_2.txt") as file:
        for line in file.readlines():
            new_line = line.replace(" ", "")
            find_all = re.findall(r"(?P<AMOUNT>[0-9]+)(?P<COLOR>[a-z]+)", new_line)
            if not list(filter(filter_games, find_all)):
                game = re.match(r"^Game(?P<NUMBER>[0-9]+)", new_line)
                all_games += int(game.group("NUMBER"))
    return all_games


print(task_2_1())


# 2


def task_2_2():
    all_games = 0
    with open("task_2.txt") as file:
        for line in file.readlines():
            find_all = re.findall(
                r"(?P<AMOUNT>[0-9]+)(?P<COLOR>[a-z]+)", line.replace(" ", "")
            )
            set_amount_as_integer = [(int(amount), color) for amount, color in find_all]
            max_green = max(
                filter(lambda item: item[1] == "green", set_amount_as_integer)
            )[0]
            max_blue = max(
                filter(lambda item: item[1] == "blue", set_amount_as_integer)
            )[0]
            max_red = max(filter(lambda item: item[1] == "red", set_amount_as_integer))[
                0
            ]
            all_games += max_green * max_red * max_blue

    return all_games


print(task_2_2())
