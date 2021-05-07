team_A = 11
team_B = 11
cards = input().split(" ")
cards_set = set(cards)      # ignoring cards for players already out
for element in cards_set:
    ele = element.split("-")
    letter = ele[0]
    num = int(ele[1])
    if letter == "A":
        team_A -= 1
        if team_A < 7:
            break
    elif letter == "B":
        team_B -= 1
        if team_B < 7:
            break
print(f"Team A - {team_A}; Team B - {team_B}")
if team_A < 7 or team_B < 7:
    print("Game was terminated")