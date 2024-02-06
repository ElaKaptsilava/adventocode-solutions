import re

with open("puzzle6.txt", "r") as puzzle_file:
    read_puzzle = puzzle_file.read().splitlines()
    *time_k, time_mapping = read_puzzle[0].split(":")
    *distance_k, record_mapping = read_puzzle[1].split(":")


def boat_races_1(times, records):
    items = dict(zip(times, records))
    result = 1
    for time, record in items.items():
        # for mill....
        new_records = [
            score
            for millisecond in range(0, time + 1)
            if (score := (time - millisecond) * millisecond) > record
        ]
        result *= len(new_records)
    return result


time_map, record_map = list(map(int, time_mapping.split())), list(
    map(int, record_mapping.split())
)

print(boat_races_1(time_map, record_map))


def boat_races_2(time, record):
    new_records = [
        score
        for millisecond in range(0, time + 1)
        if (score := (time - millisecond) * millisecond) > record
    ]
    return len(new_records)


time = int(time_mapping.replace(" " * 5, "").strip())
record = int(record_mapping.replace(" " * 3, "").strip())
print(boat_races_2(time, record))
