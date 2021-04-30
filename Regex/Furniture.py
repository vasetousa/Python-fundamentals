import re
text = input()
furniture_names = []
total_amount = 0
pattern = r'>>(?P<name>[a-zA-Z]+)<<(?P<price>\d+\.?\d+)\!(?P<quantity>\d+\b)'

while not text == "Purchase":
    match = re.match(pattern, text)
    if match:
        data = match.groupdict()
        furniture_names.append(data['name'])
        total_amount += float(data['price']) * int(data['quantity'])

    text = input()

print(f"Bought furniture:")
if furniture_names:    # this line is to avoid the additional new line, which gives an error in Judge
    print(*furniture_names, sep="\n")
print(f"Total money spend: {total_amount:.2f}")

# >>Sofa<<312.23!3
# >>TV<<300!5
# >Invalid<<!5
# Purchase