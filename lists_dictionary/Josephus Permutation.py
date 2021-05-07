numbers = input().split(" ")    # string of numbers
k = int(input())        # step of numbers to remove
step = 0
result = []
is_result_over = False
lenght = len(numbers)
while not is_result_over:
    step = 0
    for number in range(1, lenght + 1):
        step += 1
        if number == lenght:
            lenght = len(numbers)
        if lenght == 0:
            is_result_over = True

        if step == k-1:
            result.append(numbers[number])
            numbers.remove(numbers[number])
            print(numbers)
            print(result)
            step = 0
# 2 4 1 5 7 6 3
print()