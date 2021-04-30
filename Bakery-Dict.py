data = input().split()
products = {}
product = input().split()

for element in range(0, len(data), 2):
    key = data[element]
    value = data[element+1]
    products[key] = value

for prod in product:

    if prod in products:
        quantity = products.get(prod)
        print(f"We have {quantity} of {prod} left")
    else:
        print(f"Sorry, we don't have {prod}")
