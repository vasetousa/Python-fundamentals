#
#
# s = "Count, the number of spaces"
# print(s.count(' '))
#
#
# word = "Hello My World"
# print(word.count('l'))  # count how many times l is in the string
#
#
# print(word.find("H"))  # find the word H in the string
#
# print(word.index("World"))  # find the letters World in the string
#
#
#
# word = "Hello World"
#
# print(word[0])  #get one char of the word
# print(word[0:1])     #get one char of the word (same as above)
# print(word[0:3])     #get the first three char
# print(word[:3])     #get the first three char
# print(word[-3:])     #get the last three char
# print(word[3:])  #get all but the three first char
# print(word[:-3])    #get all but the three last character
#
# word = "Hello World"
#
# # word[start:end]     # items start through end-1
# # word[start:]    # items start through the rest of the list
# # word[:end]   # items from the beginning through end-1
# # word[:]     # a copy of the whole list
#
# print("." * 10) # print 10 dots
#
# a = word.replace("Hello", "Goodbye")    # replace the word "Hello" with the one "Goodbye"
# 'Goodbye World'
#
# print(a)
#
#
#
# some_text = "a b c d"
# list = some_text.split(' ')
# print(some_text); print(list)
#
# back_to_str = ''.join(list)
# print(back_to_str)
#
# nums = [1, 2, 3]
#
# for index in range(0, len(nums)):       # index could be any other name
#     print(index)


# list_happiness = [int(el) for el in input().split()]  # direct list of integers with comprehension
# list_happiness = list(map(lambda el: int(el), input().split()))  # direct list of integers with map and lambda
# list_happiness = list(int, input().split()))  # direct list of integers with reference to "int"

# print(','.join(str(x) for x in list_of_ints))
# ', '.join(map(str, myList))


# creating the data and saving it in a list
# line = input()
# while line != "Stop":
#     sender, receiver, content = line.split()
#     email = Email(sender, receiver, content) !!!
#     emails.append(email)
#     line = input()

# SORTING DICTIONARY some_dict = {"a": 1, "b": 11, "c": 20}

# print(sorted(some_dict.items(), key=lambda kvp: [1], reverse=True))
# print(sorted(some_dict.items(), key=lambda kvp: -kvp[1]))   # sorting by value same as above DESCENDING
# (-KVP is integer of float)

# print(sorted(dict.items(), key=lambda kvp: kvp[1], reversed=True))   # sorting by value
# (when value is not an integer or float) same as above DESCENDING (-kvp)
# when strings only, no Digits in the dictionaries, use:
# a = sorted(dict.items(), key=lambda kvp: kvp[1], reversed=True)


# printing result (dictionary)
# for key, values in synonyms.items():    # same as above print, but using ".items()"
#     print(f"{key} - {', '.join(values)}")


# A = [[1, 4, 5, 12],
#      [-5, 8, 9, 0],
#      [-6, 7, 11, 19]]
#
# print("A =", A)
# print("A[1] =", A[1])  # 2nd row
# print("A[1][2] =", A[1][2])  # 3rd element of 2nd row
# print("A[0][-1] =", A[0][-1])  # Last element of 1st Row
#
# column = []  # empty list
# for row in A:
#     column.append(row[2])
#
# print("3rd column =", column)
