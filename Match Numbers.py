import re
text = input()
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

matched_text = [el.group() for el in re.finditer(pattern, text)]
print(*matched_text)