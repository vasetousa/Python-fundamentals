symbol_start = ord(input())
symbol_end = ord(input())
string = input()
suma = 0

# sum of all characters between two given characters (their ascii code)
for el in string:
    asci = ord(el)
    if asci in range(symbol_start, symbol_end):
        suma += ord(el)

print(suma)