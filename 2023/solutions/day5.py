import numpy

with open("../inputs/puzzle_input_5.txt") as file:
    read = file.read().split("\n\n")
    seeds = list(map(int, read.pop(0).replace("seeds:", "").split()))


def solve(seeds, to_convert):
    s = []
    for seed in seeds:
        memory = seed
        for source_category in to_convert:
            for category in source_category.split("\n")[1:]:
                destination, source, length = list(map(int, category.split()))
                destination_range = range(destination, destination + length)
                source_range = range(source, source + length)
                if memory in source_range:
                    memory = destination_range[source_range.index(memory)]
                    break
        s.append(memory)
    return min(s)


a = solve(seeds, read)
print(a)
# 1181555926
# 1181555926
# seeds = numpy.array(seeds).reshape(10, 2)
# seeds = numpy.concatenate([numpy.arange(start, start + end) for start, end in seeds])
# print(solve(seeds[:50], read))
