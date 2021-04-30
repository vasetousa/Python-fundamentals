number = int(input())
shell_count = 1
electrons = 1
list_electrons = []

while number >= 0:
    electrons = 2 * (shell_count ** 2)
    if number == 0:
        break
    if number < electrons:
        list_electrons.append(number)
        break
    list_electrons.append(electrons)
    shell_count += 1
    number -= electrons

print(list_electrons)
