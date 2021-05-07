def collect(items, item):
    if item in collecting_items:
        return
    collecting_items.append(item)
    return


def drop(items, item):
    if item in collecting_items:
        collecting_items.remove(item)
        return
    return


def combine_items(old, new):
    if old in collecting_items:
        for el in collecting_items:
            if el == old:
                index_of_el = collecting_items.index(el)
                collecting_items.insert(index_of_el + 1, new)
                return
    return


def renew(items, item):
    if item in collecting_items:
        collecting_items.remove(item)
        collecting_items.append(item)
        return
    return


def split_items(items, item):
    oldy, newy = item.split(":")
    return oldy, newy


def is_item_in_list(items, item):
    if item in items:
        is_item_there = True
        return is_item_there
    return


collecting_items = input().split(", ")
command, item = input().split(" - ")
is_item_there = False

while command != "Craft!":
    if command == "Collect":
        is_item_in_list(collecting_items, command)
        if not is_item_there:
            collect(command)
    if command == "Drop":
        is_item_in_list(collecting_items, command)
        if not is_item_there:
            drop(command)
    if command == "Combine Items":
        if not is_item_there:
            result3, result4 = split_items(item)  # splitting the combining items by ":"
            combine_items(result3, result4)
    if command == "Renew":
        is_item_in_list(collecting_items, command)
        if not is_item_there:
            renew(command)
    print(collecting_items)
    command = input().split(" - ")

print(", ".join(collecting_items))
print(*collecting_items, sep=", ")

# Iron, Sword, Stone
# Drop - Bronze
# Combine Items - Sword:Bow
# Renew - Iron
# Craft!
