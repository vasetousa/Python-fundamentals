key = [int(num) for num in input().split()]
data = input()
length = len(key)
results_dict = {}

while not data == 'find':
    message = ""
    counter = 0
    for el in data:
        if counter == length:
            counter = 0
        asc = ord(el)
        asc -= key[counter]
        ord_asc = chr(asc)
        message += ord_asc
        counter += 1
    find_item = message.find('&')
    find_position = message.find('<')
    type_found = ""
    coordinates = ""
    for sym in range(find_item + 1, len(message) + 1):
        if message[sym] == "&":
            break
        type_found += message[sym]
    for sym in range(find_position + 1, len(message) + 1):
        if message[sym] == ">":
            break
        coordinates += message[sym]
    if type_found not in results_dict:
        results_dict[type_found] = coordinates

    data = input()

for item, numbers in results_dict.items():
    print(f"Found {item} at {numbers}")

