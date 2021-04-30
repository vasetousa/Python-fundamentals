substrings = input().split(", ")
words = input().split(", ")

result = [word for word in substrings for el in words if word in el]

print(sorted(set(result), key=result.index))


# result = []
# for word in substrings:
#     for el in words:
#         if word in el:
#             result.append(word)
# print(result)

# data input
# arp, live, strong
# lively, alive, harp, sharp, armstrong