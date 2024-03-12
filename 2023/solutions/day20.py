# '''
#     Pulses : high and low
#     Pulses are always processed in the order they are sent.
#
#     % -> Flip-flop -> are either 'on' or 'off'; they are initially off;
#         If a flip-flop destination_module receives a high pulse, it is ignored and nothing happens
#         if a flip-flop destination_module receives a low pulse, it flips between on and off
#             - If it was off, it turns on and sends a high pulse
#             - If it was on, it turns off and sends a low pulse
#
#     & -> Conjunction
#         REMEMBER the type of the most recent pulse received from each of their connected input modules
#         they initially default to remembering a LOW pulse for each input
#            - When a pulse is received, the conjunction destination_module first UPDATES its MEMORY for that input
#            - Then, if it remembers high pulses for all inputs, it sends a low pulse; otherwise, it sends a high pulse.
#
#     broadcaster -> There is a single broadcast destination_module
#         When it receives a pulse, it sends the same pulse to all of its destination modules.
#     button -> When you push the button, a single low pulse is sent directly to the 'broadcaster' destination_module
#
#     Solution:
#
#         class Flip Flop:
#         status = False; def send_pluses(pulses): if not pulses:
#         status = not mode, return mode
#
#         class Conjunction:
#         pulses = False, mode = True; def send_messages(send_pluses):pulses = send_pluses, if pulses:
#         pulses = False; else: pulses = True
# '''
import copy
from collections import defaultdict, deque

# class Module:
#     def __init__(self, name, output):
#         self.name = name
#         self.output = output
#         self.messages = deque()


class FlipFlop:
    def __init__(self, name, destinations):
        self.name = name
        self.destinations = destinations
        self.status = False
        self.pulses = None

    def __repr__(self):
        return f"FlipFlop(name='{self.name}', status='{self.status}', pulses = {self.pulses}, destination='{self.destinations})"

    def receive_messages(self, pulses):
        if not pulses:
            self.status = not self.status
            self.pulses = self.status
        else:
            self.pulses = pulses


class Conjunction:
    def __init__(self, name, destinations):
        self.messages = defaultdict(lambda: False)
        self.name = name
        self.destinations = destinations
        self.pulses = False

    def __repr__(self):
        return f"Conjunction(name='{self.name}', pulses='{self.pulses}', destination='{self.destinations}')"

    def receive_messages(self, pulses):
        first_received = [self.messages[i] for i in self.input_modules]
        return not all(first_received)

class Broadcaster:
    def __init__(self, destinations):
        self.destinations = destinations
        self.pulses = False

    def __repr__(self):
        return f"Broadcaster(destination='{self.destinations}', pulses='{self.pulses}')"


with open('../inputs/input20.txt') as file:
    queue = deque(maxlen=1800)
    config = dict()

    for line in file.read().split('\n'):
        input_, outputs_ = line.replace(' ', '').split('->')
        match input_[0]:
            case 'b':
                broadcaster = Broadcaster(destinations=outputs_.split(','))
                queue.append(broadcaster)
            case '%':
                flipflop = FlipFlop(name=input_[1:], destinations=outputs_.split(','))
                config[input_[1:]] = flipflop
            case '&':
                conjunction = Conjunction(name=input_[1:], destinations=outputs_.split(','))
                config[input_[1:]] = conjunction

    high = 0
    low = 0
    for _ in range(1000):
        queue_copy = copy.deepcopy(queue)
        passed = []
        while queue_copy:
            print(queue_copy)
            message = queue_copy.popleft()
            for destination in message.destinations:
                destination_module = config.get(destination)
                if message.pulses:
                    high += 1
                else:
                    low += 1
                if destination_module:
                    destination_module.receive_messages(message.pulses)
                    queue_copy.append(destination_module)
            passed.extend(message.destinations)

    print(high)
    print(low)


