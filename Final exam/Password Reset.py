
password = input()
string = input()
result = ""

while not string == "Done":
    if string.startswith("TakeOdd"):
        for index in range(len(password)):
            if not index % 2 == 0:
                result += password[index]
        print(result)
    elif string.startswith("Cut"):
        command, index, length = string.split()
        index = int(index)
        length = int(length)
        result = password[:index] + password[index+length:]
        print(result)
    elif string.startswith("Substitute"):
        command, substring, substitute = string.split()
        cheker = password.find(substring)
        if cheker < 0:
            print("Nothing to replace!")
        else:
            result = password.replace(substring, substitute)
            print(result)
    password = result
    string = input()
print(f"Your password is: {password}")