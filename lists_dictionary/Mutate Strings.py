string1 = input()
string2 = input()
str = len(string1)
count1 = 0
result1 = ""
result2 = ""
result = ""
mut_words = string1
for i in range(1, str+1):    # mutated words count
    count1 += 1
    for p1 in range(count1):     # letters print from word 2
        result2 += string2[p1]
    for p2 in range(count1, str):     # letters print from word 1
        result1 += string1[p2]
    result = result2 + result1
    if not result == mut_words:
        print(result)
    mut_words = result
    result1 = ""
    result2 = ""

