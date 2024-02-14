import collections

deck_cards = list(
    reversed(["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"])
)
types = {
    (5,): 7,
    (1, 4): 6,
    (2, 3): 5,
    (1, 1, 3): 4,
    (1, 2, 2): 3,
    (1, 1, 1, 2): 2,
    (1, 1, 1, 1, 1): 1,
}

with open("../imputs/puzzle7.txt", "r") as puzzle_file:
    puzzle_read = puzzle_file.read().splitlines()


def camel_cards(puzzle):
    d = dict.fromkeys(range(1, len(puzzle)), None)
    result = []
    for hand in puzzle:
        cards, bid_amount = hand.split()[0], int(hand.split()[1])
        type_ = tuple(sorted(collections.Counter(cards).values()))
        result.append([cards, types.get(type_), bid_amount])

    for strong in range(1, len(types)):
        filter_by_strong = list(filter(lambda x: x[1] == strong, result))
        for itt in range(len(filter_by_strong) - 1, 0, -1):
            for index in range(itt):
                hand1, hand2 = filter_by_strong[index], filter_by_strong[index + 1]
                if deck_cards.index(hand1[0][0]) > deck_cards.index(hand2[0][0]):
                    filter_by_strong[index], filter_by_strong[index + 1] = (
                        filter_by_strong[index + 1],
                        filter_by_strong[index],
                    )
        print(filter_by_strong)
        break


camel_cards(puzzle_read)


def partition(array, low, high):
    index = low - 1
    for j in range(low, high):
        pivot = deck_cards.index(array[high][0][0])
        if deck_cards.index(array[j][0][0]) <= pivot:
            for i in range(0, 5):
                if deck_cards.index(array[j][0][i]) < deck_cards.index(
                    array[high][0][i]
                ):
                    index = index + 1
                    (array[index], array[j]) = (array[j], array[index])
                    break
    (array[index + 1], array[high]) = (array[high], array[index + 1])

    return index + 1


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


data = [
    ["9TQ2A", 1, 211],
    ["J25T4", 1, 559],
    ["TK3A4", 1, 877],
    ["8K62J", 1, 596],
    ["9Q728", 1, 582],
    ["265T8", 1, 757],
    ["Q2584", 1, 807],
    ["9Q7T8", 1, 674],
]

size = len(data)

quickSort(data, 0, size - 1)

# size = len(filter_by_strong)
# quickSort(filter_by_strong, 0, size - 1)
# print(filter_by_strong)
