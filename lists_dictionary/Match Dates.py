import re
text = input()
pattern = r"\b(?P<Day>\d{2})(?P<separator>\(-|/|.)(?P<Month>[A-z][a-z]{2})(?P=separator)(?P<Year>\d{4})\b"

matched_text = [obj.groupdict() for obj in re.finditer(pattern, text)]

# print 1 variant
#for data in matched_text:
# print(f"Day: {data['Day']}, Month: {data['Month']}, Year: {data['Year']}")

# SECOND VARIANT TO PRINT, joining on a new row
print('\n'.join([f"Day: {data['Day']}, Month: {data['Month']}, Year: {data['Year']}" for data in matched_text]))
