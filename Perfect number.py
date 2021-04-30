def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n


number = int(input())
result = perfect_number(number)

if perfect_number(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")

