students = int(input())
lectures = int(input())
course_bonus = int(input())
scores_bonus = []
attendance_list = []

for at in range(students):  # "at" is the attendances
    student_attendances = input()
    total_bonus = int(student_attendances) / lectures * (5 + course_bonus)
    scores_bonus.append(total_bonus)
    attendance_list.append(student_attendances)
attendance_list = [int(el) for el in attendance_list]
if scores_bonus != []:
    max_bonus = round(max(scores_bonus))
else:
    max_bonus = 0
if attendance_list != []:
    max_attendance = round(max(attendance_list))
else:
    max_attendance = 0

print(f"Max Bonus: {max_bonus}.")
print(f"The student has attended {max_attendance} lectures.")

# 5
# 25
# 30
# 12
# 19
# 7
# 16
# 20