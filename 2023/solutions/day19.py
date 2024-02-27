"""
    To start, each part is rated in each of four categories:
        x: Extremely cool looking
        m: Musical (it makes a noise when you hit it)
        a: Aerodynamic
        s: Shiny

    x>10:one -> If  x > 10 , send the part to the workflow = one
    m<20:two -> If  m < 20 , send the part to the workflow = two
    a>30:R -> If  a>30 , send the part is immediately rejected (R)
    A : Otherwise, because no other rules matched the part, the part is immediately accepted (A).
"""


def complete_value_dict(conditions):
    var = dict()
    for cond in conditions.split("\n"):
        way, rule = cond.rstrip("}").split("{")
        var[way] = rule.split(",")
    return var


def complete_workflows(workflow):
    return dict(variable.split("=") for variable in workflow[1:-1].split(","))


def solution_1(rules_item, workflows_item):
    result = 0
    for workflow in workflows_item.split("\n"):
        start = "in"
        workflows_item = complete_workflows(workflow)
        while True:
            match start:
                case "R":
                    break
                case "A":
                    result += sum(map(int, workflows_item.values()))
                    break

            for rules in rules_item[start]:
                if ":" in rules:
                    rule, way = rules.split(":")
                    if eval(rule.replace(rule[0], workflows_item[rule[0]])):
                        start = way
                        break
                start = rules

    return result


def solution_2(rules_item, workflows_item):
    result = 0
    for workflow in workflows_item.split("\n"):
        workflows_item = complete_workflows(workflow)
        is_allowed = [value for value in workflows_item.values() if int(value) in range(1, 4000)]
        if len(is_allowed) != len(workflows_item.values()):
            continue
        todo = list(rules_item)
        while todo:
            match (start := todo.pop()):
                case "A":
                    result += sum(map(int, workflows_item.values()))
                    continue

                case "R":
                    continue

            rules = rules_item[start]
            for rule in rules:
                if ":" in rule:
                    rule, way = rule.split(":")
                    if eval(rule.replace(rule[0], workflows_item[rule[0]])):
                        todo.append(way)
                else:
                    todo.append(rule)
    return result


with open("../inputs/input19.txt") as file:
    rules_, workflows_input = file.read().split("\n\n")
    variables = complete_value_dict(rules_)

# print(solution_1(variables, workflows_input))

print(solution_2(variables, workflows_input))

"670929499"
