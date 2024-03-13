from pprint import pprint


def complete_building_item(data):
    item = dict()
    for i_row, row in enumerate(data):
        for i_column, column in enumerate(row):
            item[complex(i_column, i_row)] = int(column)
    return item


with open("../inputs/input17.txt") as file:
    city_block = file.read().split("\n")
    city_block_item = complete_building_item(city_block)
    print(city_block_item)

start = 0j
step = 0
current_direct = 1
count = 0
for _ in range(2):
    directions = [-1j, 1, 1j, -1]
    current_building_heat_los = city_block_item.get(start)
    directions.remove(-current_direct)
    heat_los = 10
    if step + current_building_heat_los < 4:
        for direction in directions:
            for i in range(1, current_building_heat_los + 1):
                count += city_block_item.get(start + i)
            step += current_building_heat_los
    print(step)
    print(count)
    # print(current_direct, heat_los, step)
