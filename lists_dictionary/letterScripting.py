def scripting():
    step1 = ord(letter)
    step2 = str(step1)
    step3 = step2[0] + step2[-1]
    step4 = step1 + int(step3[-1])
    step5 = chr(step4) + step3
    step6 = step1 - int(step2[0])
    step7 = chr(step6)
    step8 = step5 + step7
    list_letters.append(step8)
    return

def print_result():
    print("".join(list_letters))
    return

text = input().split()
word_counter = len(text)
list_letters = []
count = 0
space = "@628"

while text[0] != "end":

    for word in range(1, word_counter+1):
        for letter in text[count]:
            scripting()
            count += 1
        count = word
        if word != word_counter:
            list_letters.append(space)
    print_result()
    list_letters = []
    text = input().split()
    count = 0
    # Meeting on Saturday in the park 16:00

    # j → p16i
    # ASCII кодът на j e 106 → Първа цифра - 1, последна цифра - 6
    # Залепяме първата и последната цифра → 16
    # Към началото на стойността на низа, който представя резултата, залепяме символа
    # който се получава от сбора на ASCII кода + последната цифра → 106 + 6 → 112 → p
    # Към края на стойността на низа, който представя резултата, залепяме символа, който се получава от разликата
    # на ASCII кода - първата цифра → 106 - 1 → 105 → i