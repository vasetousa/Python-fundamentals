number = int(input())

number_to_string = str(number)  # make the number a string
take_len_of_number = len(number_to_string)  # take the length of the string

start_list = []
new_list_numbers = []

for _ in range(take_len_of_number):
    start_list.append(number_to_string[_])

for i in range(take_len_of_number):
    num = (start_list[i])
    numm = int(num)
    new_list_numbers.append(numm)

start_list.clear()
for b in range(take_len_of_number):
    maxx = max(new_list_numbers)
    start_list.append(maxx)
    new_list_numbers.remove(maxx)

for t in range(take_len_of_number):
    string = (start_list[t])
    strr = str(string)
    new_list_numbers.append(strr)

num = ""
for r in range(take_len_of_number):
    num += new_list_numbers[r]

number = int(num)
print(number)
