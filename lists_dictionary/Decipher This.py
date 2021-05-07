message = input().split()

for word in message:
    number = ""
    letters = ""
    for char in word:
        if char.isdigit():
            number += char
        else:
            letters += char
    first_letter = chr(int(number))
    current_word = first_letter + letters
    current_word = list(current_word)
    current_word[1], current_word[-1] = current_word[-1], current_word[1]
    current_word = "".join(current_word)

    print(current_word, end=" ")


#   data input
#   72olle 103doo 100ya