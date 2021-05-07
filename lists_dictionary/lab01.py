num = float(input())
if num == 0:
    print("zero")


elif num > 0:
    if num > 1000000:
        print("large positive")
    elif num < 1:
        print("small positive")
    else:
        print("positive")

else:
    if abs(num) < 1:
        print("small negative")
    elif abs(num) > 1000000:
        print("large negative")
    else:
        print("negative")
