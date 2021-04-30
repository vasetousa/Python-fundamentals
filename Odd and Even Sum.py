def sum_of_all_even_odd_numbers(number):
    integer = 0
    list_of_single_digits = []
    sum_of_evens = 0
    sum_of_odds = 0
    for i in number_string:
        list_of_single_digits.append(i)
        integer = int(i)
        if integer % 2 == 0:
            sum_of_evens += integer

        else:
            sum_of_odds += integer
    return [sum_of_odds, sum_of_evens]


number_string = input()
result = sum_of_all_even_odd_numbers(number_string)
sum_of_odds = result[0]
sum_of_evens = result[1]
print(f"Odd sum = {sum_of_odds}, Even sum = {sum_of_evens}")