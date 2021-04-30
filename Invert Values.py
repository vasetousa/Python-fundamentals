numbers = input().split(" ");
values = []
inverted_values = []
for i in numbers:
    values.append(int(i))
for t in values:
    b = t
    t = -t
    inverted_values.append(t)
print(inverted_values)
