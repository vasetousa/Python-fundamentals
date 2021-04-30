def calculate_result(string, number):   # Ab, AB, aB, ab
    number = int(number)

    if string[0].isupper() and string[1].islower():
        aa = string[0].lower()
        bb = string[1].lower()
        res = number / int((alphabet.index(aa))) + int((alphabet.index(bb)))    # Ab  (number / a position) + b position)
    elif string[0].isupper() and string[1].isupper():
        aa = string[0].lower()
        bb = string[1].lower()
        res = number / int((alphabet.index(aa))) - int((alphabet.index(bb)))      # AB  (number / a position) * number
    elif string[0].islower() and string[1].isupper():
        aa = string[0].lower()
        bb = string[1].lower()
        res = int((alphabet.index(aa))) * number - int((alphabet.index(bb)))        # aB   (a position * number) - b position
    elif string[0].islower() and string[1].islower():
        aa = string[0].lower()
        bb = string[1].lower()
        res = int((alphabet.index(aa))) * number + int((alphabet.index(bb)))            # ab  (a position * number) + b position

    return res
data = [el.strip() for el in input().split()]
alphabet = [
'>', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
'v', 'w', 'x', 'y', 'z']
string = ''
number = ''
outcome = []
index = 0
len_data = len(data)

count = 0
for unit in data:
    len_unit = len(unit)
    for el in unit:
        len_data = len(unit)
        if index < len_data:
            if el.isalpha():
                string += el            # upper letter added to string
                index += 1
            else:
                if el.isdigit():  # a number added to string
                    number += str(el)
                    index += 1
    result = calculate_result(string, number)
    index = 0
    outcome.append(result)
    string = ''
    number = ''
print(f"{sum(outcome):.2f}")
