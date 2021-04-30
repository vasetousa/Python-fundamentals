import re
text = input()

word = input()
pattern = rf"\b{word}\b"

count = re.findall(pattern, text, re.IGNORECASE)
print(len(count))

# There was one. Therefore I bought it. I wouldn't buy it otherwise.
# there