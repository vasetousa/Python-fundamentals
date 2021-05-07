n = int(input())
is_found = False
count = 0
for i in range(1, n):
    if n % i == 0:
        count += 1

if count > 2:
    print("False")
else:
    print("True")
