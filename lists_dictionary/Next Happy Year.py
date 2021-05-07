year = int(input()) + 1

while True:
    year_str = str(year)
    if len(year_str) == len(set(year_str)):     # compare the len in both strings and if they are same,
        # the yeah is unique
        print(year)
        break
    year += 1
