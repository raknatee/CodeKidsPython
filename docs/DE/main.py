employees = {}
salary_data = None
with open("salary.txt", "r") as salary_file:
    salary_data = salary_file.readlines()

for each_record in salary_data:
    split_data = each_record.split("=")
    name = split_data[0]
    money = float(split_data[1])
    if name not in employees:
        employees[name] = 0

    employees[name] = employees[name] + money

print(employees)