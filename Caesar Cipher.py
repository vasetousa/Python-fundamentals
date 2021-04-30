text = input()
encrypted = ''

for el in text:
    a = ord(el) + 3
    b = chr(a)
    encrypted += str(b)
print(encrypted)