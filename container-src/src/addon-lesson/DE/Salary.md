# How much salary for your employee(s)?

<a href="/DE/salary.txt" download>Click here for download salary.txt</a>

```txt
Jessie=150
Zak=400
Chester=100
Jim=200
Chester=145
Alexander=200
...
Chester=100
Alexander=260
Zak=400
Chester=150
Jessie=170
```

## Read a file

```py
employees = {}
salary_data = None
with open("salary.txt", "r") as salary_file:
    salary_data = salary_file.readlines()

print(salary_data)
```

:::output
['Jessie=150\n', 'Zak=400\n', 'Chester=100\n', 'Jim=200\n', 'Chester=145\n', 
'Alexander=200\n', 'Zak=400\n', 'Alexander=100\n', 'Jessie=200\n', 'Chester=100\n', 
'Alexander=400\n', 'Jim=212\n', 'Paul=150\n', 'Alexander=90\n', 'Jim=190\n', 
'Chester=200\n', 'Alexander=150\n', 'Paul=30\n', 'Jessie=152\n', 'Zak=400\n', 
'Alexander=200\n', 'Paul=160\n', 'Zak=400\n', 'Paul=115\n', 'Jessie=140\n', 
'Paul=180\n', 'Jim=220\n', 'Paul=100\n', 'Jessie=30\n', 'Alexander=50\n', 
'Zak=400\n', 'Jim=150\n', 'Paul=90\n', 'Jim=20\n', 'Chester=180\n', 
'Jim=55\n', 'Alexander=120\n', 'Jessie=90\n', 'Paul=70\n', 'Zak=400\n', 
'Chester=90\n', 'Jim=100\n', 'Alexander=100\n', 'Jessie=160\n', 'Paul=130\n',
'Chester=100\n', 'Alexander=260\n', 'Zak=400\n', 'Chester=150\n', 'Jessie=170']
:::

## Calculate

```py{6-15}
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
```
:::output
{'Jessie': 1092.0, 'Zak': 2800.0, 
'Chester': 1065.0, 'Jim': 1147.0, 
'Alexander': 1670.0, 'Paul': 1025.0}
:::