def move(number_of_letters):  # digit
    number_of_letters = int(number_of_letters)
    part_to_move = encrypted_message[:number_of_letters]
    new_string = encrypted_message[number_of_letters:] + part_to_move
    #print(new_string)
    return new_string


def insert(index, value):  # digits
    part1 = encrypted_message[:int(index)]
    part2 = encrypted_message[int(index):]
    new_string = part1 + value + part2
    #print(new_string)
    return new_string



def change_all(substring, replacement):  # strings
    new_string = encrypted_message
    count = encrypted_message.count(substring)
    for el in range(count):
        x = new_string.index(substring)
        part1 = new_string[:x]
        part2 = new_string[x+1:]
        new_string = part1 + replacement + part2
    #print(new_string)
    return new_string


encrypted_message = input()

command = input()
while not command == "Decode":
    orders = command.split('|')
    ord0 = orders[0]
    ord1 = orders[1]
    if ord0 == "Move":
        encrypted_message = move(ord1)
    elif ord0 == "Insert":
        ord2 = orders[2]
        encrypted_message = insert(ord1, ord2)
    elif ord0 == "ChangeAll":
        ord2 = orders[2]
        encrypted_message = change_all(ord1, ord2)


    command = input()


print(f"The decrypted message is: {encrypted_message}")
