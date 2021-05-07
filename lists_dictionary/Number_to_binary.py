num_1 = int(input())    # just a number
num_2 = int(input()) + 1
result_1 = 1
result_2 = 1
list_bin = []
zeros = [0, 0, 0, 0]
while result_2 > 0:
    result_1 = num_1 % 2   # second part after the .04
    result_2 = num_1 // 2  # the first part of the number before the 4.
    list_bin.append(result_1)
    num_1 = result_2
list_bin.extend(zeros)
list_bin.reverse()

zero_or_one = list_bin.count(num_2)   # counts the number of 0 or 1 in the binary number
print(*list_bin, sep="")     # print the binary number
print(list_bin[-num_2]) # prints the bit at position -2 (n)




# data input
# 155
# 0 or 1