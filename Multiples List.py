factor = int(input())
count = int(input())
factor_list = []

for i in range(1, count+1):
    result = factor * i
    if result % factor == 0:
        factor_list.append(result)

print(factor_list)