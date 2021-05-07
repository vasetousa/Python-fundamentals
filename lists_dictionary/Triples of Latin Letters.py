number = int(input())  # number of letters
a = 0
for i in range(0, number):
    for k in range(0, number):
        for h in range(0, number):
            print(f"{chr(97 + i)}{chr(97 + k)}{chr(97 + h)}")
            for f in range(0, 900000):
                a += 1