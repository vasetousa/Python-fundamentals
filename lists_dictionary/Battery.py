l_bat = 12
w_bat = 9
h_bat = 0.5
batteries_volume = l_bat * w_bat * h_bat

box_l = int(input(f'box rows: '))
box_w = int(input(f'box columns: '))
box_h = float(input(f'box length in centimeters: ')) / 0.5
batt_count_in_the_box = box_l * box_w * box_h
batt_count_in_the_box = int(batt_count_in_the_box)

print(f"Battery packs in the box: {batt_count_in_the_box}")
print(f"Batteries in the box: {batt_count_in_the_box * 4}")
box_volume = (box_h) * (box_w * 9) * (box_l * 12)
container_volume = 63480000

box_count = container_volume / box_volume
box_count = round(box_count)

print(f"Box count in the container: {box_count}")
print(f"Batteries count in the container: {batt_count_in_the_box * box_count * 4}")
