efficiency1 = int(input())  #
efficiency2 = int(input())  # employees
efficiency3 = int(input())  #
students_total = int(input())
total_students_per_hour = efficiency1 + efficiency2 + efficiency3
list1 = []
free_hour = 0
counter = 0
hours = students_total // total_students_per_hour
hours1 = students_total % total_students_per_hour
is_value_bigger = False

while not is_value_bigger:

    for el in range(3):
        list1.append(total_students_per_hour)
        counter += total_students_per_hour
        if counter >= students_total:
            is_value_bigger = True
            break
    list1.append(free_hour)

len_list = len(list1) - 1
print(f"Time needed: {len_list}h.")