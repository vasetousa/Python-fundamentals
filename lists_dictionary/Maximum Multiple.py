
divisor = int(input())
bound = int(input())

c=0

for i in range(divisor, bound+1):
    if i % divisor == 0:
        c = i
print(c)
