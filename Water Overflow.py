tank_capacity = 255
n = int(input())  # number of lines
water_total = 0
is_insufficient = False


for i in range(n):
    water_q = int(input())  # quantities of water for the tank
    water_total += water_q
    if water_total > 255 or water_q > tank_capacity:
        print(f"Insufficient capacity!"); is_insufficient = True
        if is_insufficient:
            water_total -= water_q
if is_insufficient or water_total <= tank_capacity:
    print(water_total)