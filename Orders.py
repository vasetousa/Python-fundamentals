def calculate_the_price(item, count):
    if item == "coffee":
        return count * 1.50
    elif item == "water":
        return count
    elif item == "coke":
        return count * 1.40
    elif item == "snacks":
        return count * 2


product = input()
quantity = int(input())

result = calculate_the_price(product, quantity)
print(f'{result:.2f}')
