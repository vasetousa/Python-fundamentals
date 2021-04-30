budged = float(input())
flour_price = float(input())
import math

# 1 cozunak ingredients needed
eggs = 1         # 1 pack eggs
flour = 1        # 1 kg flour
milk = 0.250     # 0.250 l milk

eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25

cozunak_price = (flour_price + eggs_price + milk_price / 4)
cozunak_count = (budged / cozunak_price)  # calculate how many cozunaks we can make with this budged
cozunak_integer = int(cozunak_count)
money_left = (budged) - (cozunak_integer * cozunak_price)
sum = budged
egg = 0
count = 0
coz_count = 0

while sum > money_left:
    sum = sum - cozunak_price
    count += 1; coz_count += 1; egg += 3
    if coz_count == cozunak_integer:
        break
    if count == 3:
        count = 0
        egg -= 1


print(f"You made {cozunak_integer} cozonacs! Now you have {egg} eggs and {money_left:.2f}BGN left.")

