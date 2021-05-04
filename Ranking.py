END_OF_CONTESTS = "end of contests"
END_OF_SUBMISSIONS = "end of submissions"
contests = {}
string = ''
users_dict_counter = 1
valid_users_contest_data = {'contest': "", 'name': "", 'points': 0}
total_points = {}

not_in_dict = False
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
            for ke, va in valid_users_contest_data.copy().items():
                for contest_from_dict, value in va.copy().items():
                    if contest_from_dict == contest:
                        for username_from_dict, points_from_dict in value.copy().items():
                            if username_from_dict == username:
                                not_in_dict = True
                                if points > points_from_dict:
                                    valid_users_contest_data[ke] = {contest_from_dict:{username: points}}
                            else:
                                not_in_dict = False
            users_dict_counter += 1
            if not not_in_dict:
                valid_users_contest_data[users_dict_counter] = {contest: {username: points}}
                if username not in total_points:
                    total_points[username] = points
                else:
                    total_points[username] += points
                not_in_dict = False

sorted_numbers = sorted(total_points.items(), key=lambda kvp: -kvp[1])
# sorted_users = sorted(valid_users_contest_data.items(), key=lambda kvp: -kvp[1])

print(f"Best candidate is {sorted_numbers[0][0]} with total {sorted_numbers[0][1]} points.")
print("Ranking")

for ke, va in valid_users_contest_data.items():
    for contest_from_dict, value in va.items():
        for username_from_dict, points_from_dict in value.items():
            username = username_from_dict
            print(username)
            if username == username_from_dict:
                print(contest_from_dict)
print()

