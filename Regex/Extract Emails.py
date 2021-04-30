import re
text = input()
pattern = r'(?<=\s)(?P<user>[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+)@(?P<host>[a-zA-Z0-9]+[\-]?[a-zA-Z0-9]+)(?P<extension>(\.[a-zA-Z0-9]+)+)'


valid_link = [el.group() for el in re.finditer(pattern, text)]
if valid_link:
    print(*valid_link, sep="\n")