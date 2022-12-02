class Elf:
    def __init__(self, calories):
        self.calories = calories

    def get_total_calories(self):
        return sum(self.calories)


with open('2022/day_1/input.txt', 'r') as file:
    f = file.read().strip()
    elf_calories = f.splitlines()

    elves = []

    elf_cal = []
    for calory in elf_calories:
        if calory == '':
            elves.append(
                Elf(elf_cal)
            )
            elf_cal = []
        else:
            elf_cal.append(int(calory))

elves = sorted(elves, key=lambda elf: elf.get_total_calories(), reverse=True)
r = sum(e.get_total_calories() for e in elves[0:3])

print(r)

# answer 201491