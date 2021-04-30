health = 100
bitcoins = 0
room_counter = 0
rooms = input().split("|")
command_list = []
value_list = []
is_dead = False
for el in rooms:
    for l in el:
        if l.isdigit():
            value_list.append(l)
        else:
            command_list.append(l)
            if l == " ":
                command_list.remove(l)
    value_list = "".join(value_list)
    command_list = "".join(command_list)
    command = command_list
    value = int(value_list)
    room_counter += 1
    if command == "potion":

        if health + value > 100:
            print(f"You healed for {100-health} hp.")
            health = 100
            print(f"Current health: {health} hp.")

        else:
            print(f"You healed for {value} hp.")
            print(f"Current health: {health + value} hp.")
            health += value
    elif command == "chest":
        value = int(value_list)
        print(f"You found {value} bitcoins.")
        bitcoins += value


    else:
        health -= value
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_counter}")
            is_dead = True
    command_list = []
    value_list = []
    if health <= 0:
        break
if not is_dead:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")

# rat 10|bat 20|potion 10|rat 10|chest 100|boss 70|chest 1000