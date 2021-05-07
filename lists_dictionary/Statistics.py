products = {}
pairs = input()


while not pairs == "statistics":
    prod, quantity = pairs.split(":")
    if prod not in products:
        products[prod] = 0
    products[prod] += int(quantity)

    pairs = input()

print(f"Products in stock:")
for (prod, quantity) in products.items():
    print(f"- {prod}: {quantity}")

print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")

