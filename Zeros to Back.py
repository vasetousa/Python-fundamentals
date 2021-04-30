numbers = input().split(", ")
new_list = []
for num in numbers:
    nn = int(num)
    if nn == 0:
        numbers.remove(num)
        numbers.append(num)
for _ in numbers:
    new_list.append(int(_))
print(new_list)