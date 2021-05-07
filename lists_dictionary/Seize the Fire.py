def check_validity_of_fire_cell(f_type, value): # calculating if fire cell has valid parameters
    is_valid = False
    if f_type == "High" and value in range(81, 126):
        is_valid = True
    elif f_type == "Medium" and value in range(51, 81):
        is_valid = True
    elif f_type == "Low" and value in range(1, 51):
        is_valid = True
    return is_valid


fires_data = input().split("#")
water_quantity = int(input())
total_fire = 0
total_effort = 0
fires_list = []
len_fires_list = len(fires_list) / 2


for el in range(len(fires_data)):
    x = fires_data[el]
    part1, part2 = x.split(" = ")
    part2 = int(part2)
    result = check_validity_of_fire_cell(part1, part2)      # return result is True or False

    if result:
        if water_quantity >= part2:
            water_quantity -= part2     # current water quantity
            total_effort += part2 * 0.25    # calc effort
            total_fire += part2     # calc total fire put out
            fires_list.append(part2)    # list of the cells put out

print("Cells:")
for el in fires_list:
    print(f" - {el}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")

# High = 89#Low = 28#Medium = 77#Low = 23
# 1250

# High = 150#Low = 55#Medium = 86#Low = 40#High = 110#Medium = 77
# 220