def check_for_legendary(material_stuff):
    if material_stuff == "fragments":
        return "Valanyr"
    elif material_stuff == "shards":
        return "Shadowmorne"
    elif material_stuff == "motes":
        return "Dragonwrath"
    return


items = input().split()
key_items = ("motes", "fragments", "shards")
legend_items_obtained = {"Legendary Item": {}}
key_materials_dict = {"shards": 0, "fragments": 0, "motes": 0}
junk_dict = {}
material_obtained = ""
is_obtained = False

while not is_obtained:
    # creating the materials dictionary
    for el in range(0, len(items), 2):
        digit = int(items[el])
        item = items[el+1].lower()
        if item in key_materials_dict:
            key_materials_dict[item] += int(digit)
            legendary_key = key_materials_dict.get(item)
            if legendary_key >= 250:
                material_obtained = item
                legend = check_for_legendary(item)  # determent which legendary item was obtained
                if legend is not None:
                    print(f"{legend} obtained!")
                    legendary_key -= 250
                    key_materials_dict[item] = legendary_key
                    # just for fun, nested in nested in nested dictionary, see row 13
                    legend_items_obtained["Legendary Item"] = {legend: {item: legendary_key+250}}
                    is_obtained = True
                    break

        else:
            if item not in junk_dict:
                junk_dict[item] = int(digit)

            else:
                junk_dict[item] += int(digit)

    if is_obtained:
        break
    items = input().split()

# sorting the 2 dictionaries - key items and junk
sorted_material = sorted(key_materials_dict.items(), key=lambda kvp: (-kvp[1], kvp[0])) # descending by value,
# then by alphabet
sorted_junk = sorted(junk_dict.items(), key=lambda kvp: kvp[0]) # sorting by alphabet

# print the key materials in descending order
for material, quantity in sorted_material:
    print(f"{material}: {quantity:}")

# print the junk materials in alphabet order
for el, qu in sorted_junk:
    print(f"{el}: {qu:}")


# 3 Motes 5 stones 5 Shards 6 leathers 200 fragments 7 Shards
# 123 silver 6 shards 8 shards 5 motes 235 fangs 40 fragments
# 75 motes 103 MOTES 8 Shards 86 Motes 7 stones 300 silver
# 6 leathers 255 fragments 7 Shards 12 feathers 166 copper



