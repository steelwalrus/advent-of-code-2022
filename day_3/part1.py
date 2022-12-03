import string

with open('day_3/input.txt', 'r') as file:
    f = file.read().strip()
    inputs = f.splitlines()

class Rucksack:
    def __init__(self, items):

        half_of_items = len(items) // 2
        self.compartment_a = items[:half_of_items]
        self.compartment_b = items[half_of_items:]
        self.shared = []

    def get_shared_item(self):
        return [i for i in self.compartment_a if i in self.compartment_b][0]

    @staticmethod
    def get_item_priority(item: str):
        return string.ascii_letters.index(item) + 1


priority_sum = 0

for c in inputs:
    r = Rucksack(c)
    value = r.get_item_priority(r.get_shared_item())
    priority_sum += value

print(priority_sum)

# 7793