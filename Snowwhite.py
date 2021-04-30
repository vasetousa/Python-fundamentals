data = input()
store = {}
name_counter = {}
counter = 0
is_stored = False

while not data == "Once upon a time":
    string = data.split(" <:> ")
    dwarf = string[0]
    hat_color = string[1]
    power = int(string[2])
#   Check for same name
    if dwarf not in name_counter:
        name_counter[dwarf] = 1
        store[counter] = (dwarf, hat_color, power)
        counter += 1
    else:           # imame same name ->>>
        for key, value in store.items():
            if value[0] == dwarf and value[1] == hat_color: # ako i hat e same color
                if value[2] < power:
                    store[key] = (dwarf, hat_color, power)  # ako power > store the same dwarf with the new power
                    is_stored = True
        if not is_stored:
            name_counter[dwarf] += 1
            store[counter] = (dwarf, hat_color, power)
            counter += 1


    data = input()

sorted_powers1 = dict(sorted(store.items(), key=lambda kvp: (-(kvp[1][2]), kvp[1][1])))
for key, value in sorted_powers1.items():
    print(f'({value[1]}) {value[0]} <-> {value[2]}')
print()