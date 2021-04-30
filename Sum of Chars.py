number_lines = int(input())
sum = 0
for i in range(number_lines):
    letters = int(ord(input()))
    sum = sum + letters


print(f"The sum equals: {sum}")