
def operation(act, number_1, number_2):
    if act == "multiply":
        return first_num * second_num
    elif act == "divide":
        return first_num / second_num
    elif act == "add":
        return first_num + second_num
    elif act == "subtract":
        return first_num - second_num


# 'multiply', 'divide', 'add', 'subtract'

calc_operation = input()
first_num = int(input())
second_num = int(input())

result = operation(calc_operation, first_num, second_num, )
print(f'{result:.0f}')
