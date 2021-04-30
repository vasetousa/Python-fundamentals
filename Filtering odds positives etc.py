n = int(input())
nums = []
filtered = []

for _ in range(n):
    number= int(input())
    nums.append(number)

command = input()

if command == "even":
    for num in list(nums):
        if num % 2 == 0:
            filtered.append(num)
elif command  == "odd":
    for num in list(nums):
        if num % 2 == 1:
            filtered.append(num)
elif command  == "positive":
    for num in list(nums):
        if num >= 0:
            filtered.append(num)
elif command  == "negative":
    for num in list(nums):
        if num < 0:
            filtered.append(num)
print(filtered)