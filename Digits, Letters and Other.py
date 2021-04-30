string = input()
digit = []
letter = []
other = []

for el in string:
    d = el.isdigit()
    l = el.isalpha()
    o = el.isnumeric()
    if d:
        digit.append(el)
    if l:
        letter.append(el)
    if not d and not l:
        other.append(el)

print(''.join(digit))
print(''.join(letter))
print(''.join(other))