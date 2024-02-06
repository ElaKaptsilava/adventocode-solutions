PARTS = {
    "|": ["N", "S"],
    "-": ["W", "E"],
    "L": ["N", "E"],
    "J": ["N", "W"],
    "7": ["W", "S"],
    "F": ["E", "S"],
    "S": [("N", "S"), ("W", "E")],
}
vertical = {"N", "S"}
horizontal = {"W", "E"}


memory = 'S'

def conditions_for_filter(items):
    hemisphere, point_up, point_down = items[0], PARTS[items[1]][0], PARTS[items[1]][1]
    start = '|'
    if hemisphere != memory:
        if hemisphere in ['W', 'E']:
            var = [{point_up, PARTS[start][0]}, {point_down, PARTS[start][0]}, {point_up, PARTS[start][1]},
                   {point_down, PARTS[start][1]}]
            return horizontal in var
        elif hemisphere == 'N':
            return {point_down, PARTS[start][0]} == vertical
        return {point_up, PARTS[start][1]} == vertical
    return False


suitables = list(filter(conditions_for_filter, [("N", '7'), ("W", '|'), ("E", '|'), ("S", '|')]))

print(suitables)