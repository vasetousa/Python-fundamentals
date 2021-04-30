string = input().split()
len_first = len(string[0])
len_second = len(string[1])
total = 0
if len_first >= len_second:
    first = (string[0])[:len_second]
    second = (string[1])[:]
    rest = (string[0])[len_second:]
else:
    first = (string[0])[:]
    second = (string[1])[:len_first]
    rest = (string[1])[len_first:]

for letter in range(len(first)):
    result = ord(first[letter]) * ord(second[letter])
    total += result

for el in rest:
    total += ord(el)
print(total)