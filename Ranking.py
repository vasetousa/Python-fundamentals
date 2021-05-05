END_OF_CONTESTS = "end of contests"
END_OF_SUBMISSIONS = "end of submissions"
contests = {}
string = ''
valid_users_contest_data = {}
total_points = {}

low_points = False
while True:
    string = input()
    if string == END_OF_CONTESTS:
        break
    string1, pass2 = string.split(":")
    contests[string1] = pass2
while True:
    string = input()
    if string == END_OF_SUBMISSIONS:
        break
    contest, password, username, points = string.split("=>")
    points = int(points)
    if contest in contests:
        pass_from_contests = contests.get(contest)
        if password == pass_from_contests:

            # check if contests is in the list, if the name is the same and if the points are more than the points in the dict
            if username in valid_users_contest_data:
                for key, dict_values in valid_users_contest_data.copy().items():
                    for key2, dict_values_2 in dict_values.copy().items():
                        if key == username:
                            if key2 == contest:
                                if points > dict_values_2:
                                    valid_users_contest_data[key].update({contest: points})
                                else:
                                    low_points = True
                            else:
                                valid_users_contest_data[username].update({contest: points})
            else:
                valid_users_contest_data[username] = {contest: points}

            if username not in total_points:
                total_points[username] = points
            else:
                if not low_points:
                    total_points[username] += points
                low_points = False

sorted_numbers = sorted(total_points.items(), key=lambda kvp: -kvp[1])
sorted_users = sorted(valid_users_contest_data[username].items(), key=lambda kvp: -kvp[1], kvp[0])

print(f"Best candidate is {sorted_numbers[0][0]} with total {sorted_numbers[0][1]} points.")
print("Ranking")

for key, dict_values in valid_users_contest_data.items():
    for contest_from_dict, value in dict_values.items():
        pass
print()
