def decripting():
    letter = list_words[word]
    step1 = ord(letter[0])  # p
    step5 = chr(step1 - int(letter[2]))  # this will be the real letter from ASCII
    if step5 == ">":
        step5 = " "
    letter_list.append(step5)
    return


def print_result():
    print("".join(list_words))
    return


text = input()  # scripted text
text_counter = len(text)
letter_counter = text_counter / 4
list_words = []
letter_list = []
start = 0
count = 0
space = "@628"

#   Dividing the text by 4 parts (each letter)
for i in range(1, int(letter_counter + 1)):
    el = text[start:start + 4]
    list_words.append(el)
    start += 4

def print_result():
    print("".join(letter_list))
    return

while text[0] != "end":
    for word in range(0, int(letter_counter)):
        decripting()
        count += 1
    count = word
    print_result()
    letter_list = []
    text = input().split()
    count = 0

# Dear Daniela, L68>f11dh97Xv14qL68>h97Xn10mn15hf11dt18kh97X
# Vasko Boss, \86Nh97Xx15rr17jp11n@628H66<p11nx15rx15r


# j → p16i
# ASCII кодът на j e 106 → Първа цифра - 1, последна цифра - 6
# Залепяме първата и последната цифра → 16
# Към началото на стойността на низа, който представя резултата, залепяме символа
# който се получава от сбора на ASCII кода + последната цифра → 106 + 6 → 112 → p
# Към края на стойността на низа, който представя резултата, залепяме символа, който се получава от разликата
# на ASCII кода - първата цифра → 106 - 1 → 105 → i
