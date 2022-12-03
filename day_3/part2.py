import string

with open('day_3/input.txt', 'r') as file:
    f = file.read().strip()
    inputs = f.splitlines()

class Rucksack:
    def __init__(self, items):

        half_of_items = len(items) // 2
        self.contents = items
        self.compartment_a = items[:half_of_items]
        self.compartment_b = items[half_of_items:]
        self.shared = []

    def get_shared_item(self):
        return [i for i in self.compartment_a if i in self.compartment_b][0]

    @staticmethod
    def get_item_priority(item: string):
        return string.ascii_letters.index(item) + 1


priority_sum = 0
size_of_group = 3

for group in zip(*(iter(i for i in inputs),) * size_of_group):
    tally = {}

    for i, bag_contents in enumerate(group):
        r = Rucksack(bag_contents)
        unique_contents = set(r.contents)

        for item in unique_contents:
            if item not in tally:
                tally[item] = 1
            else:
                tally[item] += 1
                if tally[item] == 3:
                    priority_sum += r.get_item_priority(item)
                    break

print(priority_sum)

# 2499