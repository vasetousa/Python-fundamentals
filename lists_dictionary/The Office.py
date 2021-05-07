list_happiness = input().split()
factor = int(input())
# list_happiness = [int(el) for el in input().split()]  # direct list of integers with comprehension
# list_happiness = list(map(lambda el: int(el), input().split()))  # direct list of integers with map and lambda
# list_happiness = list(int, input().split()))  # direct list of integers with reference to "int"
# list with happiness multiplied by the factor
list_happiness_digits = [int(el) * factor for el in list_happiness]
average_factor = sum(list_happiness_digits) / len(list_happiness_digits) # average factor from the list

list_happiness_digits = [int(num) for num in list_happiness_digits if num >= average_factor]
if len(list_happiness_digits) >= len(list_happiness) / 2:
    print(f"Score: {len(list_happiness_digits)}/{len(list_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(list_happiness_digits)}/{len(list_happiness)}. Employees are not happy!")