import re


def task_4_1():
    with open("puzzle_input_4.txt") as file:
        read_file = file.read().replace("  ", " ").splitlines()
        result = 0
        for index, line in enumerate(read_file):
            match = re.match(
                r"Card[\s]+(?P<CARD>[0-9]+):[\s](?P<WIN>([0-9]+[\s])+)[|][\s](?P<PLAYER>([0-9\s]+)+)",
                string=line,
            )
            card, win, player = (
                match.group("CARD"),
                match.group("WIN").split(" "),
                match.group("PLAYER").split(" "),
            )
            if (amount_win := len(set(win) & set(player))) > 0:
                result += 2 ** (amount_win - 1)
    return result


def task_4_2():
    with open("puzzle_input_4.txt") as file:
        read_file = file.read().replace("  ", " ").splitlines()
        cards_instance = {index: 1 for index in range(1, len(read_file) + 1)}
        result = 0
        for index, line in enumerate(read_file):
            match = re.match(
                r"Card[\s]+(?P<CARD>[0-9]+):[\s](?P<WIN>([0-9]+[\s])+)[|][\s](?P<PLAYER>([0-9\s]+)+)",
                string=line,
            )
            card, win, player = (
                match.group("CARD"),
                match.group("WIN").split(" "),
                match.group("PLAYER").split(" "),
            )
            if (amount_win := len(set(win) & set(player))) > 0:
                for instance in range(1, amount_win + 1):
                    cards_instance[int(card) + instance] += cards_instance.get(
                        int(card)
                    )
            result += cards_instance[int(card)]
        return result
