people = int(input())       # number of people
capacity = int(input())     # capacity of people
br = people / capacity

if people <= capacity:
    print(1)

else:
    if people % capacity != 0:
        print(int(br) + 1)
    else:
        print(f"{br:.0f}")
