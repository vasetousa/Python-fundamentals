gifts = input().split()
gifts_after = []
command = input()
while not command == "No Money":
    order = command.split()
    if order[0] == "OutOfStock":
        for el in gifts:
            if order[1] == el:
                index = gifts.index(el)
                gifts[index] = "None"

    elif order[0] == "Required":
        index = int(order[2])
        if index in range(len(gifts)):
            gifts[index] = order[1]

    elif order[0] == "JustInCase":
        gifts[-1] = order[1]

    #print(" ".join(gifts))
    command = input()
for el in gifts:
    if el != "None":
        gifts_after.append(el)
print(" ".join(gifts_after))

