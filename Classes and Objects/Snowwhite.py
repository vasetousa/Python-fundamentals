data = input()
store = {}
name_counter = {}
is_stored = False

while not data == "Once upon a time":
    dwarf, hat_color, power = data.split(" <:> ")
    power = int(power)

#   Check for same name
    if dwarf not in name_counter:
        name_counter[dwarf] = 1
        store[dwarf] = {hat_color: power}
    else:           # we have same name ->>>
        for key, value in store.copy().items():
            for k, v in value.copy().items():
                if k == hat_color:
                    if v < power:
                        store[key].update({hat_color: power})  # ako power > store the same dwarf with the new power
                        is_stored = True
                else:
                    store[key].update({hat_color: power})
        if not is_stored:
            name_counter[dwarf] += 1

    data = input()

sorted_powers = sorted(store.items(), key=lambda kvp: (kvp[0][1], kvp[1]))
for key, value in sorted_powers:
    for k, v in value.items():
        print(f'({k}) {key} <-> {v}')

print()