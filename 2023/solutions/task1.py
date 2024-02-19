import re


def day1_1():
    with open("../inputs/task_1.txt", "r") as txt:
        result = 0
        for text in txt.read().split():
            find_all = re.sub(r"[\D]", "", text)
            print(find_all)
            number = find_all[0] + find_all[-1]
            print(find_all[0])
            result += int(number)
        return result


print(day1_1())


def day1_2():
    digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    with open("../inputs/task_1.txt", "r") as txt:
        result = 0
        for line in txt.read().split():
            find_all_numbers = re.findall(
                r"[0-9]|{0}".format("|".join(digits.keys())), line
            )
            first, last = find_all_numbers[0], find_all_numbers[-1]
            if first.isdigit() and last.isdigit():
                result += int(first + last)
            elif not first.isdigit() and not last.isdigit():
                result += int(digits[first] + digits[last])
            elif first.isdigit() and not last.isdigit():
                result += int(first + digits[last])
            elif not first.isdigit() and last.isdigit():
                result += int(digits[first] + last)
    return result


print(day1_2())
