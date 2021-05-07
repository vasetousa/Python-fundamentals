people_waiting = int(input())
wagon_state = input().split()
len_ = len(wagon_state)
counter = 0
is_full = False
if people_waiting == 0:
    print(*wagon_state)
    exit(0)
for el in range(len_):
    counter = int(wagon_state[el])
    if counter == 4:
        is_full = True
        continue
    for people in range(4):
        if people_waiting == 0:
            break
        people_waiting -=1
        counter += 1
        wagon_state[el] = counter
        is_full = False
        if counter == 4:
            break
        if people_waiting == 0:
            break

if is_full:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(*wagon_state)

elif counter < 4:
    print(f"The lift has empty spots!")
    print(*wagon_state)

elif people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(*wagon_state)
else:
    print(*wagon_state)