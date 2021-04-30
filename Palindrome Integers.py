def palindrome_numbers(element):    # check if the input string == same reversed string, a.e "number"
    if element == element[::-1]:  # [::-1] reverses the string
        return True
    return False


number_string = input().split(", ")

for num_as_string in number_string:
    is_palindrome = palindrome_numbers(num_as_string)   # assigning bool True/False from the function
    if is_palindrome:   # according to the value True or False, print the result
        print(True)
    else:
        print(False)