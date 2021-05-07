def divider(string):  # determent the divider type
    str1 = " | "
    str2 = " -> "
    count1 = data.count(" | ")
    count2 = data.count(" -> ")
    if count1 > 0:
        string = " | "
        return string
    string = " -> "
    return string


data = input()
forceUser = {}
forceSide = {}

while not data == "Lumpawaroo":
    symbol = divider(data)
    command = data.split(symbol)
    if symbol == " | ":         # Symbol = " | "
        user = command[1]
        side = command[0]
        if user not in forceUser:       # Add User to Group if not there
            forceUser[user] = side
            if side not in forceSide:   # Add Side to Group if not there
                forceSide[side] = [user]
            else:
                forceSide[side].append(user)    # Side exist, so we add user to the list
    else:                   # Symbol " -> "
        user = command[0]
        side = command[1]
        if user not in forceUser:   # Add User to Group if not there
            forceUser[user] = side
            if side not in forceSide:
                forceSide[side] = [user]
            else:
                forceSide[side].append(user)
            print(f"{user} joins the {side} side!")
        else:                       # User is in the Group, but changes the Side to opposite
            forceUser[user] = side
            if side not in forceSide:    # If Group does not exist
                for _ in forceSide.copy():  # removing user from old side after been added to opposite
                    for el in range(len(forceSide[_])):
                        if user in forceSide[_][el]:
                            del forceSide[_][el]
                            break
                forceSide[side] = [user]
                forceSide[side].append(user)
            else:                           # Group exists with members, must remove member now
                for _ in forceSide.copy():      # removing user from old side after been added to opposite
                    for el in range(len(forceSide[_])):
                        if user in forceSide[_][el]:
                            del forceSide[_][el]
                            break
                forceSide[side].append(user)        # add User to the new Side
                print(f"{user} joins the {side} side!")
    data = input()

# sorting the [side] Descending by count and then, ordered by name
sorted_sides = sorted(forceSide.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

for side, users in sorted_sides:
    if not len(users) == 0:
        print(f"Side: {side}, Members: {len(users)}")
    for user in sorted(users):
        print(f'! {user}')