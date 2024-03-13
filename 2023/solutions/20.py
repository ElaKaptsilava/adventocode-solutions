import copy
from collections import defaultdict, deque


class Module(object):
    def __init__(self, name):
        self.name = name
        self.outputs = list()
        self.send_pules = False

    def receive_pules(self, pules: bool) -> None:
        pass


class FlipFlop(Module):
    def __init__(self, name):
        super().__init__(name)
        self.status = False

    def __repr__(self):
        return f"FlipFlop({self.name}: outputs= {self.outputs}, status= {self.status}, send_pules= {self.send_pules})"

    def receive_pules(self, pules: bool) -> None:
        if not pules:
            self.status = not self.status
        self.send_pules = self.status


class Conjunction(Module):
    def __init__(self, name):
        super().__init__(name)
        self.inputs = []
        self.memory = dict()

    def __repr__(self):
        return f"Conjunction({self.name}: inputs= {self.inputs}, outputs= {self.outputs}, send_pules= {self.send_pules}, memory= {self.memory})"

    def receive_pules(self, pules: bool) -> None:
        memory = []
        for module_ in self.memory.values():
            memory.append(module_.send_pules)
        self.send_pules = not all(memory)


class Broadcaster(Module):
    def __init__(self, name="Broadcaster"):
        super().__init__(name)

    def __repr__(self):
        return f"Broadcaster(outputs= {self.outputs}, outputs= {self.outputs})"


def get_modules(file) -> dict:
    global queue_
    modules = dict()
    for line in file.read().split("\n"):
        input_, outputs_ = line.replace(" ", "").split("->")
        match input_[0]:
            case "b":
                broadcaster = Broadcaster()
                broadcaster.outputs.extend(outputs_.split(","))
                queue_.append(broadcaster)
            case "%":
                flipflop = FlipFlop(name=input_[1:])
                flipflop.outputs.extend(outputs_.split(","))
                modules[input_[1:]] = flipflop
            case "&":
                conjunction = Conjunction(name=input_[1:])
                conjunction.outputs.extend(outputs_.split(","))
                modules[input_[1:]] = conjunction
        # for output in outputs_.split(','):
        #     if not modules.get(output):
        #         module_ = Module(name=input_[1:])
        #         modules[input_[1:]] = module_
    return modules


def set_inputs_for_conjunctions(moduls_item: dict[str, Conjunction | FlipFlop]) -> None:
    conjunctions_moduls = list(
        filter(lambda module_: isinstance(module_, Conjunction), moduls_item.values())
    )
    for conjunction in conjunctions_moduls:
        for name, module in moduls_item.items():
            if conjunction.name in module.outputs:
                conjunction.inputs.append(module.name)
                for input_ in conjunction.inputs:
                    conjunction.memory[input_] = moduls_item.get(input_)


with open("../inputs/input20.txt") as file:
    queue_ = deque(maxlen=1800)
    modules = get_modules(file)
    set_inputs_for_conjunctions(modules)
    high, low = 0, 0
    for _ in range(1):
        passed = []
        queue = copy.deepcopy(queue_)
        while queue:
            module = queue.popleft()
            pules_to_send = module.send_pules
            for output in module.outputs:
                if pules_to_send is True:
                    high += 1
                elif pules_to_send is False:
                    low += 1
                output_module = modules.get(output)
                # print(module, output_module)
                print(
                    module.name,
                    "->",
                    "HIGH" if pules_to_send else "LOW",
                    "->",
                    output_module.name if output_module else output,
                )
                if output_module:
                    output_module.receive_pules(pules_to_send)
                    queue.append(output_module)
        print()
    low += 1
    print(low, high)
    print(high * low)
# 817896682
