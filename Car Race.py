numbers = input().split()
numbers_len = len(numbers)
numbers_to_middle = (numbers_len - 1) // 2
sum_numbers_in_list = 0
sum_numbers_in_list2 = 0

for left in range(0, numbers_to_middle):
    sum_numbers_in_list += int(numbers[left])
    if int(numbers[left]) == 0:
        sum_numbers_in_list *= 0.8

for right in range(numbers_len-1, numbers_to_middle, -1):
    sum_numbers_in_list2 += int(numbers[right])
    if int(numbers[right]) == 0:
        sum_numbers_in_list2 *= 0.8

min_result = min(sum_numbers_in_list, sum_numbers_in_list2)
if sum_numbers_in_list < sum_numbers_in_list2:
    print(f"The winner is left with total time: {min_result:.1f}")
else:
    print(f"The winner is right with total time: {min_result:.1f}")
