numbers = [int(el) for el in input().split()]
average = sum(numbers) / (len(numbers))

top_5_list = []
current_max = 0

for num in range(5):
    current_max = max(numbers)
    if current_max > average:
        top_5_list.append(current_max)
        numbers.remove(current_max)
list(top_5_list)
if top_5_list:
    print(*top_5_list)
else:
    print("No")