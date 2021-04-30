import re
text = input()
pattern = r"\+1 \d{3}( |.|-)\d{3}\1\d{4}\b"

number = [object.group() for object in re.finditer(pattern, text)]

print(', '.join(number))
# +1 407 800 5225, +1 407-800-5225, +1 407.800.5225