import re

text = input()
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?(&|(?=\s))"

matched_numbers = re.finditer(pattern, text)

valid_numbers = [matched_object.group() for matched_object in re.finditer(pattern, text)]
print(*valid_numbers)
