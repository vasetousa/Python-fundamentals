text = input()
text_dict = {}

for el in range(len(text)):
    x = text[el]
    if x != " ":
        if x not in text_dict:
            text_dict[x] = 0
            text_dict[x] += 1
        else:
            text_dict[x] += 1

for key, value in text_dict.items():
    print(f"{key} -> {value}")