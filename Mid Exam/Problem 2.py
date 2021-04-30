integers = input()
data = [int(el) for el in integers.split()]
string = ''
count = 0
command = input()
while not command == "END":

    command = command.split()
    if command[0] == "add" and command[1] == "to" and command[2] == "start":
        for integer in command:
            if integer.isdigit():
                data.insert(count, integer)
                count += 1
    elif command[0] == "add" and command[1] == "to" and command[2] == "end":
        for integer in command:
            if integer.isdigit():
                data.append(integer)

    elif command[0] == "replace":
        for integer in data:
            if integer == int(command[1]):
                index = data.index(integer)
                data.pop(index)
                data.insert(index, command[2])
                break
    elif command[0] == "remove" and command[1] == "at": # remove at
        if int(command[3]) in range(len(data)):
            data.pop(int(command[3]))

    elif command[0] == "remove" and command[1] == "greater":    # remove greater than
        data1 = [int(el) for el in data]
        for integer in command:
            max_value = max(data1)
            if max_value > int(command[3]):
                data1.remove(max_value)
                data = data1

    elif command[0] == "remove" and command[1] == "lower":  # remove lower
        for integer in data:
            min_value = min(data)
            if min_value < int(command[3]):
                data.remove(min_value)

    elif command[0] == "find" and command[1] == 'odd':      # find odd
        for integer in data:
            if integer % 2 != 0:
                print(integer, end=" ")

    elif command[0] == "find" and command[1] == 'even':      # find even
        for integer in data:
            if integer % 2 == 0:
                print(integer, end=" ")
                print()

    elif command[0] == "remove" and command[1] == 'count':      # remove count
        n = int(command[2])
        del data[-n:]

    command = input()
print()
print(*data, sep=", ")