# def palindrome_words(element):  # check if the input string == same reversed string
#     if element == element[::-1]:  # [::-1] reverses the string
#         return True
#     return False
#
# string = input().split()  # string with words
# word = input()  # the palindrome we need to search for
# count = 0  # count of palindromes found
# palind_list = []
#
# for i in string:
#     is_palindrome = palindrome_words(i)
#     if is_palindrome:
#         palind_list.append(i)
#         if i == word:
#             count += 1
#
# print(palind_list)
# print(f"Found palindrome {count} times")

# second variant with comprehension ony 5 rows code

# words = input().split()  # string with words
# searched_pal = input()  # the palindrome we need to search for
# all_palindromes = [word for word in words if word == word[::-1]]
# print(all_palindromes)
# print(f"Found palindrome {words.count(searched_pal)} times")

# third variant with only 4 rows

all_palindromes = [word for word in input().split() if word == word[::-1]]  # searching directly while the input
searched_pal = input()  # the palindrome we need to search for
print(all_palindromes)
print(f"Found palindrome {all_palindromes.count(searched_pal)} times")

# Input data

# wow father mom wow shirt stats
# wow