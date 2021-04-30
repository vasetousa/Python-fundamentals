n = int(input())
text = ''

for _ in range(n):
    text = input()
    a = text.find("@")
    b = text.find("|")
    c = text.find("#")
    d = text.find("*")
    name = text[a+1:b]
    age = text[c+1:d]
    print(f"{name} is {age} years old.")