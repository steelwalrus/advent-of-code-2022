import re
from collections import OrderedDict


def parse_columns(input_stacks: list, stack_depth: int):
    offset = 1
    divisor = 4

    stack_data = {}

    for i in range(0, stack_depth):
        for j, col_data in enumerate(input_stacks[i]):
            r = re.match(r'[A-Z]', col_data)
            if r:
                j_offset = j - offset

                stack_number = int((j_offset / divisor) + 1 if j != 1 else 1)

                if stack_number not in stack_data:
                    stack_data[stack_number] = []

                stack_data[stack_number].append(col_data)

    stack_data = {k: [i for i in reversed(v)] for (k, v) in stack_data.items()}
    return OrderedDict(sorted(stack_data.items()))


instructions = []

with open('day_5/input.txt', 'r') as file:
    f = file.read()
    inputs = f.splitlines()

    for i, row in enumerate(inputs):
        r = re.match(r'^.*\d$', row)
        if r:
            columns = r.string.split()
            depth = i

        if row.startswith("move"):
            instruction_match = re.search('(\d+).*(\d+).*(\d+)', row)
            instruction = tuple(instruction_match.groups())
            instructions.append(instruction)

    supply_stacks = parse_columns(inputs, depth)


def apply_instruction_set(instruction_set: tuple, stack_to_update: dict):
    amount_to_move = int(instruction_set[0])
    move_from = int(instruction_set[1])
    move_to = int(instruction_set[2])

    for num in range(0, amount_to_move):
        try:
            to_move = stack_to_update[move_from].pop()
        except KeyError:
            raise KeyError(f"Cannot do {move_from} on {stack_to_update}: {instruction_set}")
        stack_to_update[move_to].append(to_move)

    return stack_to_update


for instruction in instructions:
    supply_stacks = apply_instruction_set(instruction, supply_stacks)


result = ""
for stack_key in supply_stacks:
    result += supply_stacks[stack_key][-1]

print(result)