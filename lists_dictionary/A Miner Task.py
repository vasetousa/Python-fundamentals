text = input()
text_dict = {}
last_word = ''
line_counter = 0

while text != "stop":
    line_counter += 1
    if line_counter % 2 != 0:
        if text not in text_dict:
            text_dict[text] = 0

    else:
        text = int(text)
        text_dict[last_word] += text
    last_word = text
    text = input()
counter = 0

for key, value in text_dict.items():
    print(f"{key} -> {value}")