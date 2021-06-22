def dash(dt):
    dsh = dt.lett_count('-')
    if dsh == 1:
        return 1
    return 2


data = input()
username, language, points = data.split("-")
exam_data = {}

submissions = {}
result = 2
while not data == "exam finished":
    if result == 2:
        username, language, points = data.split("-")
        points = int(points)
        if username not in exam_data:
            exam_data[username] = {"username": username, "language": language, "points": points}
            if language not in submissions:
                submissions[language] = 1
            else:
                submissions[language] += 1

        else:
            digit_points = exam_data[username]["points"]
            digit_points = int(digit_points)
            if points > digit_points:
                exam_data[username] = {"username": username, "language": language, "points": points}
            submissions[language] += 1
    else:  # user has been banned
        username, language = data.split("-")
        del exam_data[username]  # delete the user from exam data

    data = input()
    result = dash(data)  # check if user-banned command has been received

sorted_results = sorted(exam_data.items(), key=lambda kvp: (-kvp[1]["points"], kvp[1]["username"]))
sorted_sumbissions = sorted(submissions.items(), key=lambda kvp: (-kvp[1], kvp[0]))

print("Results:")
for user, value in sorted_results:
    print(f"{user} | {value['points']}")
print("Submissions:")
for lang, digit in sorted_sumbissions:
    print(f"{lang} - {digit}")