from collections import Counter

deck_cards = list(
    reversed(["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"])
)
deck = "".join(deck_cards)


def sorted_by_stronger_cards(cards):
    type_ = tuple(sorted(Counter(cards).values())[::-1])
    return type_, *map(deck.index, cards)


with open("../inputs/puzzle7.txt", "r") as file:
    games = dict(dough.split() for dough in file)
    hands = sorted(games, key=sorted_by_stronger_cards)
    result = 0
    for row, hand in enumerate(hands, 1):
        result += int(games[hand]) * row
    print(result)

# 2

deck_cards_with_j = list(
    reversed(["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"])
)
deck = "".join(deck_cards_with_j)
print(deck)


def counter_j(cards):
    count_cards = Counter(cards)
    if "J" in cards and (len(count_cards) != 1):
        pop_amount_of_j = count_cards.pop("J")
        max_of_counter = max(count_cards.items(), key=lambda y: y[1])
        count_cards[max_of_counter[0]] += pop_amount_of_j
    return count_cards


def sorted_by_stronger_cards(cards):
    type_ = tuple(sorted(counter_j(cards).values())[::-1])
    return type_, *map(deck.index, cards)


with open("../inputs/puzzle7.txt", "r") as file:
    games = dict(dough.split() for dough in file)
    hands = sorted(games, key=sorted_by_stronger_cards)
    result = [int(games[hand]) * row for row, hand in enumerate(hands, 1)]
    print(sum(result))

# 251824095
