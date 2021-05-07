products = input()
products_data = {}


while not products == "buy":
    name, price, quantity = products.split()
    price = float(price)
    quantity = int(quantity)
    if name not in products_data:
        products_data[name] = [price, quantity]

    else:
        value = products_data[name][1]
        products_data[name] = [price, quantity + value]

    products = input()
for name, list1 in products_data.items():
    print(f"{name} -> {list1[0] * list1[1]:.2f}")