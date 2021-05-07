Ornament_Set = 2
Tree_Skirts = 5
Tree_Garlands = 3
Tree_Lights = 15

quantity = int(input())
days = int(input())
spirit = 0
Ornament_Set_count = 0
Tree_Skirts_count = 0
Tree_Garlands_count = 0
Tree_Lights_count = 0
counter_of_days = 0
string_2 = ""

for i in range(1, days+1):
    counter_of_days += 1    # counting the days to find out every 10th day
    string = str(i)     # here we finds the 11th, 22nd, 33rd ... days. see rows #20-23
    string_1 = string[0]
    if i > 9:
        string_2 = string[1]
    if string_1 == string_2:    # compare first number to second number
        quantity += 2           # if they are the same, add quantity +2, every 11th day
    if i % 2 == 0:  # every 2nd day
        Ornament_Set_count = Ornament_Set_count + (Ornament_Set * quantity)
        spirit += 5
    if i % 3 == 0:  # every 3rd day
        Tree_Skirts_count = Tree_Skirts_count + (Tree_Skirts * quantity)
        Tree_Garlands_count = Tree_Garlands_count + (Tree_Garlands * quantity)
        spirit += 13
    if i % 5 == 0:    # every 5th day
        Tree_Lights_count = Tree_Lights_count + (Tree_Lights * quantity)
        spirit += 17
    if i % 3 == 0 and i % 5 == 0:  # if you bought Skirts, Garlands and every 5th day all together
        spirit += 30
    if i % 10 == 0:    # every 10th day
        spirit -= 20
        Tree_Skirts_count += 5
        Tree_Garlands_count += 3
        Tree_Lights_count += 15

    total_ornaments_price = (Ornament_Set_count + Tree_Skirts_count + Tree_Garlands_count + Tree_Lights_count)
    total_Spirits = spirit
if counter_of_days % 10 == 0:
    spirit -= 30
total_ornaments_price = Ornament_Set_count + Tree_Skirts_count + Tree_Garlands_count + Tree_Lights_count
total_Spirits = spirit
print(f"Total cost: {total_ornaments_price}")
print(f"Total spirit: {total_Spirits}")
