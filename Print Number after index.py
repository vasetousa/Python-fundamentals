def find_nth_digit(number, index):      #  2465981
    counter = 1
    while number != "0":
        index_n = number[-1]
        if counter == int(index):
            return index_n
        number = int(number) / 10
        number = int(number)
        number = str(number)
        counter += 1



digit_to_check = input()
num_to_compare_to = input()
result = find_nth_digit(digit_to_check, num_to_compare_to)
if result is None:
    print(0)
else:
    print(result)
