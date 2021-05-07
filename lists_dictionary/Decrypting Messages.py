key = int(input())
lines_n = int(input())

message_list_strings = []
message_list_integers = []
message_list_back_to_strings = []

for i in range(1, lines_n+1):
    n = input()     # character
    message_list_strings.append(n)
    message_list_integers.append(ord(n))
for e in message_list_integers:
    sum = e + key
    message_list_back_to_strings.append(chr(sum))
for _ in message_list_back_to_strings:
    print(_, end="")


