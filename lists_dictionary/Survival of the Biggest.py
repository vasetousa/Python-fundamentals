start_list = []
min_numbers_list = []
numbers_as_string = input().split(" ")
string_len = len(numbers_as_string)     # lenght of string

n = int(input())   # how many numbers from the list to remove, use in last cycle

for i in range(string_len):     # this list accepts the numbers as integers
    num = int(numbers_as_string[i])
    start_list.append(num)


for _ in range(n):     # this list contains only the min "n" numbers
    minn = min(start_list)
    start_list.remove(minn)
    min_numbers_list.append(minn)


print(start_list)