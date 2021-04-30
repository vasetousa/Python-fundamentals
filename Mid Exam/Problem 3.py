cards = input().split(", ")
n = int(input())    # commands


for comm in range(1, n+1):
    command = input().split(", ")

    if command[0] == "Add":
        if command[1] in cards:
            print("Card is already in the deck")
        else:
            print("Card successfully added")
            cards.append(command[1])

    elif command[0] == "Remove":
        if command[1] in cards:
            print("Card successfully removed")
            cards.remove(command[1])
        else:
            print("Card not found")

    elif command[0] == "Remove At":
        comm1 = int(command[1])
        lenn = len(cards)
        if not comm1 in range(lenn):
            print("Index out of range")
            continue
        print("Card successfully removed")
        cards.pop(comm1)

    elif command[0] == "Insert":
        comm1 = int(command[1])
        lenn = len(cards)
        if not comm1 in range(lenn):
            print("Index out of range")
            continue
        if command[2] in cards:
            print("Card is already in the deck")
            continue
        print("Card successfully added")
        cards.insert(comm1, command[2])


print(*cards, sep=", ")