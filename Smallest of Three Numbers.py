def smallest_number(n1, n2, n3):
    res = min(n1, n2, n3)
    return res

num1 = int(input())
num2 = int(input())
num3 = int(input())

result = smallest_number(num1, num2, num3)
print(result)