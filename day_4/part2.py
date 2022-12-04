with open('day_4/input.txt', 'r') as file:
    f = file.read().strip()
    inputs = f.splitlines()

overlaps = 0

for pair in inputs:
    split_pair = pair.split(',')
    pair1 = split_pair[0].split('-')
    pair2 = split_pair[1].split('-')

    work_area_1 = [i for i in range(int(pair1[0]), int(pair1[1]) + 1)]
    work_area_2 = [i for i in range(int(pair2[0]), int(pair2[1]) + 1)]

    intersection = set(work_area_1).intersection(work_area_2)

    if intersection:
        overlaps += 1

print(overlaps)

# 903