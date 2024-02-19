with open('../imputs/input18.txt', 'r') as plan:
    dig_plan = plan.read().split('\n')
    dig_plan = list(map(lambda item: item.split(' '), dig_plan))
    directions, step, color = list(map(list, zip(*dig_plan)))
    step = list(map(int, step))

empty = '.'
hashtag = '#'
object_ = []

point = 0
prev = 0
p = 0
while p < 2:
    line = []


print(object_)