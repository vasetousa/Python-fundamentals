def factorial(n1, n2):
    res1 = 1
    res2 = 1
    for p in range(2, n1+1):
        res1 *= p
    for g in range(2, n2+1):
        res2 *= g
    return res1 / res2

num1 = int(input())
num2 = int(input())
result = factorial(num1, num2)
print(f'{result:.2f}')