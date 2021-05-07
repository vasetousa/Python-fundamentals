def important(prod1):
    if prod1 in products:
        index = products.index(prod1)
        products.remove(prod1)
        products.insert(0, prod1)
        return
    # print(products)
    return


def swap(prod1, prod2):
    if prod1 in products and prod2 in products:
        in1 = products.index(prod1)
        in2 = products.index(prod2)
        products[in1], products[in2] = products[in2], products[in1] # swap
        return
    else:
        if prod1 not in products:
            print(f"Product {prod1} missing!")
        elif prod2 not in products:
            print(f"Product {prod2} missing!")
        # print(products)
    return


def add(prod1):
    if prod1 in products:
        print(f"This product is already in the list.")
        return
    else:
        products.insert(0, prod1)
    # print(products)
    return


def remove(prod1):
    if prod1 in products:
        products.remove(prod1)
        return
    print(f"Product {prod1} isn't in the list.")
    return


products = input().split("|")
command = input()

while command != "Shop!":
    order = command.split("%")
    product = order[1]
    if order[0] == "Important":
        important(product)
    elif order[0] == "Add":
        add(product)
    elif order[0] == "Swap":
        product2 = order[2]
        swap(product, product2)
    elif order[0] == "Remove":
        remove(product)

    command = input()

for el in range(len(products)):
    print(f'{el + 1}. {products[el]}')
