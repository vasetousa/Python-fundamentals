def swap(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    numbers[num1], numbers[num2] = numbers[num2], numbers[num1]
    #print(numbers)
    return


def multiply(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    mult = numbers[num1] * numbers[num2]
    numbers.pop(num1)
    numbers.insert(num1, mult)
    #print(numbers)
    return


def decrease(*num):
    numbers_decre = []
    for el in numbers:
        el -= 1
        numbers_decre.append(el)
    #print(numbers_decre)
    return numbers_decre


numbers = [int(el) for el in input().split()]
list_after_decrease = []
# receive the commands “swap”, “multiply” or “decrease”.
command = input().split()
while command[0] != "end":
    if command[0] == "swap":
        swap(command[1], command[2])
    if command[0] == "multiply":
        multiply(command[1], command[2])
    if command[0] == "decrease":
        list_after_decrease = decrease(command)
        numbers = list_after_decrease

    command = input().split()

print(", ".join(map(str, list_after_decrease)))  # prints the integers into strings with ","

# 1 0 2 0 3 0 4 0 decrease swap 0 1