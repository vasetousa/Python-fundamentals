string = input().split(",")
digits = [int(el) for el in string]

# same as row  13-14
result_even = list([int(el) for el in string if int(el) % 2 == 0])
result_odd = list([int(el) for el in string if int(el) % 2 != 0])

# prints the True/False value
res1 = list(map((lambda el: int(el) % 2 == 0), digits))


# prints the even/odd numbers
res3 = list(filter((lambda el: int(el) % 2 == 0), digits))
res4 = list(filter((lambda el: int(el) % 2 != 0), digits))

# 1 row print only
res5 = list(filter((lambda el: int(el) % 2 != 0), map(lambda el: int(el), digits))) # lambda el: int(el), can put "int" instead

print(result_even)
print(result_odd)
print()
print(res1, end="  "); print("# Towards the Input")
print(res2, end="  "); print("# Towards the Input")
print()

print(res3)
print(res4)
print()
print(res5)



# Data input
# 1, 2, 9, 12, 33, 22, 100, -4, 34, 12, 39