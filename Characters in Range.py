def print_ASCII_codes(x, y):
    el1 = ord(x)
    el2 = ord(y)
    chars = []
    if el1 <= el2:
        for i in range(el1+1, el2):
            chars.append(chr(i))
            print(chr(i), end=" ")      # remove rows 8, 12 and 14 and print direct on screen.
        # return chars

    else:
        for b in range(el1-1, el2, -1):
            chars.append(chr(b))
            print(chr(b), end=" ")      # remove rows 8, 12 and 14 and print direct on screen.
        # return chars

element1 = input()
element2 = input()

# result = print_ASCII_codes(element1, element2)
print_ASCII_codes(element1, element2)
# print(" ".join(result))     # takes elements from list and creates a string