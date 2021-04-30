numbers = input().split()
message = input()
message_list = list(message)
nums = 0
sum_nums_as_elements = 0
string_len = len(message_list)
message_after_decipher = []
index = 0

for ele in numbers:
    for el in ele:
        sum_nums_as_elements += int(el)
    nums += sum_nums_as_elements
    if sum_nums_as_elements <= string_len:
        first_letter = message_list[sum_nums_as_elements]
        message_list.remove(first_letter)
        message_after_decipher.append(first_letter)
    else:
        difference = sum_nums_as_elements - string_len
        first_letter = message_list[difference]
        message_list.remove(first_letter)
        message_after_decipher.append(first_letter)

    sum_nums_as_elements = 0
    nums = 0

print(f"{''.join(message_after_decipher)}")