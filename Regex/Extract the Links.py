import re
pattern = r'(?P<subdomain>w{3})\.(?P<domain>([a-zA-Z0-9-]+))(?P<extension>(\.[a-z]+)+)\b'

text = input()
while text:
    valid_link = [el.group() for el in re.finditer(pattern, text)]
    if valid_link:
        print(*valid_link, sep="\n")
    text = input()
