def calculations(number):
    price_no_tax = float(number)
    price_with_tax = float(number) * 1.2  # price with tax
    list_prices_with_tax.append(price_with_tax)
    list_prices_no_tax.append(price_no_tax)
    return


list_prices_with_tax = []
list_prices_no_tax = []
taxes = 0
command = input()
total_sum_and_taxes = 0

while not command == "special" and not command == "regular":
    if float(command) > 0:
        calculations(command)
    else:
        print(f'Invalid price!')

    command = input()
if command == "special":
    total_sum_and_taxes = sum(list_prices_with_tax)
    discount = total_sum_and_taxes * 0.1
    total_sum_and_taxes -= discount
    taxes = (sum(list_prices_no_tax) * 0.2)
    if total_sum_and_taxes == 0:
        print(f"Invalid order!")
        exit(0)
    print(f"""Congratulations you've just bought a new computer!
Price without taxes: {sum(list_prices_no_tax):.2f}$
Taxes: {taxes:.2f}$
-----------
Total price: {total_sum_and_taxes:.2f}$""")
else:
    discount = total_sum_and_taxes * 0.1
    total_sum_and_taxes = sum(list_prices_with_tax)
    taxes = (sum(list_prices_no_tax) * 0.2)
    if total_sum_and_taxes == 0:
        print(f"Invalid order!")
        exit(0)
    print(f"""Congratulations you've just bought a new computer!
Price without taxes: {sum(list_prices_no_tax):.2f}$
Taxes: {taxes:.2f}$
-----------
Total price: {total_sum_and_taxes:.2f}$""")
