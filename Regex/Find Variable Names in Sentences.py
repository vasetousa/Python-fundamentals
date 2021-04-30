import re
text = input()
pattern = r"(^_|(?<=\s_))[A-Za-z]+($|(?=\s))\b"

match = [m.group() for m in re.finditer(pattern, text)]

print(",".join(match))