numbers_string = input().split()
numbers_string_backward = sorted(numbers_string, reverse=True)
numbers = "".join(numbers_string_backward)


print(numbers)