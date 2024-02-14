with open('../imputs/input18.txt', 'r') as plan:
    dig_plan = plan.read().split('\n')
    dig_plan = list(map(lambda item: item.split(' '), dig_plan))
    direction, step, color = list(zip(*dig_plan))

point = 0
with open('../18/output18.txt', 'w+') as output:
    while True:
        output.seek(7)
        output.write('#')
        break
    print(output.read())
