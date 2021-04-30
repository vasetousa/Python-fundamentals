events = input().split("|")
energy = 100
coins = 100

for el in range(len(events)):
    string = events[el]
    order, value = string.split("-")
    value = int(value)
    if order == "rest":
        energy += value
        if energy > 100:
            energy = 100
            difference = 100 - energy
            print(f"You gained {difference} energy.")
            print(f"Current energy: {energy}.")
        else:
            print(f"You gained {value} energy.")
            print(f"Current energy: {energy}.")
    elif order == "order":
        if energy >= 30:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")
        else:
            energy += 50
            print(f"You had to rest!")

    else:
        if coins > 0:
            coins -= value
            if coins > 0:
                print(f"You bought {order}.")
            else:
                print(f"Closed! Cannot afford {order}.")
                break

if coins > 0:
    print(f"""Day completed! 
Coins: {coins}
Energy: {energy}""")


# rest-2|order-10|eggs-100|rest-10