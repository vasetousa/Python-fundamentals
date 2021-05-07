# numbers = [int(num) for num in input().split(",")]
# current_result = []
# lower_border = 0
# higher_border = 10
# max_number = max(numbers)
#
# while max_number >= higher_border - 9:
#     for dig in numbers:
#         if dig in range(lower_border, higher_border+1):
# #        if lower_border < dig < higher_border:
#             current_result.append(dig)
#     lower_border += 10; higher_border += 10
#     print(f"Group of {higher_border - 10}'s: {current_result}")
#     current_result = []


#  SECOND VARIANT
numbers = [int(num) for num in input().split(",")]
current_result = []
lower_border = 0
higher_border = 10
while numbers:
    for dig in numbers:
        if dig in range(lower_border, higher_border + 1):
            current_result.append(dig)
    lower_border += 10; higher_border += 10

    print(f"Group of {higher_border - 10}'s: {current_result}")
    for el in current_result:   # removing the current list of numbers from the main list
        numbers.remove(el)
    current_result = []

# input data
# 8, 12, 38, 3, 17, 19, 25, 35, 50
