string = input()
string = list(string)
digits = [num for num in string if num.isdigit()]
non_digits = [letter for letter in string if not letter.isdigit()]
take_list = []
skip_list = []
main_message = []
len_digits = len(digits)
len_digits_for_exit = len(digits) // 2
for take in range(0, len_digits, 2):
    take_list.append(digits[take])
for skip in range(1, len_digits + 1, 2):
    skip_list.append(digits[skip])
# Start re-creating the encrypted message
take_count = 0
skip_count = 0
#start = 0
while non_digits:
    if len_digits_for_exit == take_count:
        break
    end = int(take_list[take_count])
    end2 = int(skip_list[skip_count])
    result = non_digits[:end]
    main_message += result
    del non_digits[:end]
    del non_digits[:end2]
    take_count += 1
    skip_count += 1
    result = []

print(''.join(main_message))


# data input
#   this forbidden mess of an age rating 0127504740
#   O{1ne1T2021wf312o13Th111xreve!!@!
