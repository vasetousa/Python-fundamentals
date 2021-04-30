string = input()
command = input()
leny = len(string)


while command != "Travel":
    data, val1, val2 = command.split(":")

    if data == "Add Stop":
        num = int(val1)
        if num in range(leny):
            string = string[:num] + val2 + string[num:]
    elif data == "Remove Stop":
        num1 = int(val1)
        num2 = int(val2)
        if num1 in range(leny) and num2 in range(leny):
            string = string[:num1] + string[num2+1:]
    elif data == "Switch":
        string = string.replace(val1, val2)
    leny = len(string)
    print(string)
    command = input()
print(f"Ready for world tour! Planned stops: {string}")
