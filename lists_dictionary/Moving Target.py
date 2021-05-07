def shoot_the_target(index, power):
    if index > len_targets - 1 or index < 0:
        return
    elif power < 0:
        return
    targets[index] -= power
    if targets[index] <= 0:
        del targets[index]
    # print(targets)
    return


def add_the_target(index, value):
    if index > len_targets - 1 or index < 0:
        print(f"Invalid placement!")
        return
    elif value <= 0 or value > 10000:
        print(f"Invalid placement!")
        return
    targets.insert(index, value)
    # print(targets)
    return


def strike_the_target(index, radius):
    if index < 0 or index > len_targets - 1:
        print(f"Strike missed!")
        return
    elif index + radius > len_targets-1 or index - radius < 0:
        print(f"Strike missed!")
        return
    elif radius < 0:
        print(f"Strike missed!")
        return
    del targets[index - radius:index + radius + 1]
    # print(targets)
    return


#   input the targets
targets = [int(el) for el in input().split()]
len_targets = len(targets)

#   receive commands of action or End
command = input().split()
while command[0] != "End":
    if command[0] == "Shoot":
        shoot_the_target(int(command[1]), int(command[2]))
    elif command[0] == "Add":
        add_the_target(int(command[1]), int(command[2]))
    elif command[0] == "Strike":
        strike_the_target(int(command[1]), int(command[2]))

    command = input().split()

targets_to_strings = list(map(lambda el: str(el), targets))  # Convert the list of digits to list of strings

#   print the output

print("|".join(targets_to_strings))
