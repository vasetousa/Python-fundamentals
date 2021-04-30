import re
string = input()
pattern = r"((@|@)|(#|#))+(?P<color>[a-z]{3,})((@|@)|(#|#))+\W+(?P<count>[0-9]+)/+"
info = {}

valid_eggs = [eggs.groupdict() for eggs in re.finditer(pattern, string)]

for key in valid_eggs:

    print(f"You found {key['count']} {key['color']} eggs!")
