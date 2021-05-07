number_of_rows = int(input()) * 2
data_students_list = []
data_students_dict = {}

# creating list of data
for el in range(1, number_of_rows+1):
    data = input()
    data_students_list.append(data)

for el in range(0, len(data_students_list), 2):
    num = data_students_list[el+1]
    num = float(num)
    name = data_students_list[el]
    if name not in data_students_dict:
        data_students_dict[name] = [num]
    else:
        data_students_dict[name].append(num)
final_dictionary = {}
for el in data_students_dict.copy():
    len_scores = len(data_students_dict[el])
    if len_scores > 1:
        score1 = data_students_dict[el][0]
        score2 = data_students_dict[el][1]
        score = (score1 + score2) / 2
    else:
        score = data_students_dict[el][0]
    if score <= 4.50:
        data_students_dict.pop(el)

print()