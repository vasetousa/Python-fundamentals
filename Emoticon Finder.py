string = input()
el_string = ''
emot = []
for el in range(len(string)):
    if el == len(string) - 1:
        break
    a = string[el]
    b = string[el+1]
    if a == ":":
        el_string += a
        el_string += b
        emot.append(el_string)
        el_string = ''
for el in emot:
    print(el)

# There are so many emoticons nowadays :P. I have many ideas :O what input to place here :)