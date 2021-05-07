string = [x for x in input()]
string_list_after = []
index = 0
power = 0
for el in range(len(string)):

    if string[index] == ">":
        expl = int(string[el + 1])
        power += int(expl)

        string.pop(el+1)
        string.append('')
        power -= 1
        while power > 0:
            index = el
            string.pop(el + 1)
            string.append('')
            power -= 1

    else:
        string_list_after.append(string[index])
        index += 1

print()