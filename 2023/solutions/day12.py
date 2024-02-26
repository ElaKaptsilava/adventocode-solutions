unknown, operational, damaged = '?', '.', '#'

with open('../inputs/input12.txt', 'r') as conditions:
    ways = 0
    for line in conditions:
        springs, groups = line.split()
        groups = [int(n) for n in groups.split(',')]
        print(springs, groups)
        positions = {0: 1}
        for i, group in enumerate(groups):
            new_positions = {}
            for key, value in positions.items():
                for n in range(key, len(springs) - sum(groups[i + 1:]) + len(groups[i + 1:])):
                    if n + group - 1 < len(springs) and '.' not in springs[n:n + group]:
                        if (i == len(groups) - 1 and '#' not in springs[n + group:]) or (
                                i < len(groups) - 1 and n + group < len(springs) and springs[n + group] != '#'):
                            new_positions[n + group + 1] = new_positions[
                                                               n + group + 1] + value if n + group + 1 in new_positions else value
                    if springs[n] == '#':
                        break
            positions = new_positions
        ways += sum(positions.values())
print(ways)
