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

sum_of_calories_per_elf = []
for elf in elves:
    sum_of_calories_per_elf.append(
        elf.get_total_calories()
    )

print(max(sum_of_calories_per_elf))

# answer = 67622