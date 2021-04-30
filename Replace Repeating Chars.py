text = input()
new_text = ''
index = 0
end = False

for letter in range(len(text)):
    if end:
        break
    first = text[index]
    while first == text[index]:
        index += 1
        if index == len(text):
            end = True
            break

    new_text += first

print(new_text)

# qqqwerqwecccwd