import re
pattern = r"(@#+[A-Z])[a-zA-Z0-9]{4,}([A-Z]@#+)"
n = int(input())
digits = ""
code_list = []
for el in range(n):
    string = input()
    for index in string:       # determine the digit group
        if index.isdigit():
            digits += index
    if not digits:
        digits = "00"
    valid_code = re.search(pattern, string)
    if valid_code:
        print(f'Product group: {digits}')
    else:
        print(f'Invalid barcode')
    digits = ""
