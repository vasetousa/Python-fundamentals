num_wagons = int(input())
wagons = [0] * num_wagons

command = input()


while command != 'End':
    data = command.split()
    if data[0] == "add":
        wagons[-1] += int(data[1])
    elif data[0] == "insert":
        people = int(data[2])       #   adds people
        index = int(data[1])        #
        wagons[index] += people     #   by indexing
    elif data[0] == "leave":
        people = int(data[2])
        index = int(data[1])
        wagons[index] -= people
    command = input()

print(wagons)