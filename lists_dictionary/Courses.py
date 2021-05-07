data = input()
courses = {}

while not data == "end":
    course, student = data.split(" : ")
    if course not in courses:
        courses[course] = [student]
    else:
        courses[course].append(student)

    data = input()

sorted_students = sorted(courses.items(), key=lambda kvp: -len(kvp[1]))
for cour, nam in sorted_students:
    print(f"{cour}: {len(nam)}")
    for el in range(len(nam)):
        print(f"-- {sorted(nam)[el]}")