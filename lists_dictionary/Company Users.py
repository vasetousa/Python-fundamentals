company_name_and_ID = input()
company = {}

while not company_name_and_ID == 'End':
    data = company_name_and_ID.split(" -> ")
    name = data[0]
    employee_id = data[1]
    if name not in company:
        company[name] = [employee_id]

    else:
        if employee_id not in company[name]:
            company[name].append(employee_id)
    company_name_and_ID = input()
ordered_dict = dict(sorted(company.items(), key=lambda kvp: kvp[0]))
counter = 0
for name, id in ordered_dict.items():
    print(f"{name}")
    for index in id:
        print(f"-- {index}")

# SoftUni -> AA12345
# SoftUni -> CC12344
# Lenovo -> XX23456
# SoftUni -> AA12345
# Movement -> DD11111
# End