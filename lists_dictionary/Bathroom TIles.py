import math
budged = float(input())
w_floor = float(input())
l_floor = float(input())
triangle_side = float(input())
triangle_h = float(input())
tile_price = float(input())
work_rate = float(input())

floor_area = w_floor * l_floor
triangle_area = (triangle_side * triangle_h) / 2
tiles_needed_count = math.ceil(floor_area / triangle_area) + 5
total_tiles_cost = tiles_needed_count * tile_price
total_work_cost = total_tiles_cost + work_rate
if budged >= total_work_cost:
    print(f"{budged - total_work_cost:.2f} lv left.")
else:
    print(f"You'll need {total_work_cost - budged:.2f} lv more.")