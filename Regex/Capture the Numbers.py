import re
pattern = r"\d+"
numbers = []

text = input()
while not text == "":
    matched_numbers = re.findall(pattern, text)
    numbers.extend(matched_numbers)
    text = input()
print(*numbers)