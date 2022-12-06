with open('day_6/input.txt', 'r') as file:
    f = file.read()

char_buffer = []

parsed = 0
marker_num = 4

for char in f:
    if len(char_buffer) == marker_num:
        del char_buffer[0]

    parsed += 1
    char_buffer.append(char)

    if(len(set(char_buffer))) == marker_num:
        print("".join(char_buffer))
        print(parsed)
        break
