string = input().upper()
letters = []
for dig in range(len(string)):
    letters.append(string[dig])

symbol = ""
unique_string = ''
digit_string = ''
final_result = ''
counter = 0
for el in range(len(letters)):
    if letters[el] == "":
        break
    if letters[el].isdigit():
        if el != len(letters) - 1:
            if (letters[el+1]).isdigit():
                digit_string += letters[el]
                digit_string += letters[el+1]
                letters.remove(letters[el+1])
                final_result += (int(digit_string) * symbol)
                letters.append('')
                symbol = ''
                digit_string = ''
            else:
                digit_string += letters[el]
                final_result += (int(digit_string) * symbol)
                symbol = ''
                digit_string = ''
        else:
            digit_string += letters[el]
            final_result += (int(digit_string) * symbol)
            symbol = ''
            digit_string = ''
            break
    else:
        symbol += letters[el]
        if letters[el] not in unique_string:
            unique_string += letters[el]
            counter += 1

print(f"Unique symbols used: {counter}")
print(final_result)

# aSd2&5s@10