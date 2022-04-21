# First Exercises

## Find a sum until enter 0

:::output
Enter number: <span class="pyinput">55</span>
Enter number: <span class="pyinput">66</span>
Enter number: <span class="pyinput">754</span>
Enter number: <span class="pyinput">0</span>
875.0
:::

::: details Solutions
```py
sum=0
while(True):
    income=input("Enter number: ")
    if(income == "0"):
        break
    else:
        sum+=float(income)
print(sum)
```
or
```py
data=[]
while(True):
    income=input("Enter number: ")
    if(income== "0" ):
        sum=0
        for number in data:
            sum+=number
        print(sum)
        break
    else:
        data.append(float(income))
```
:::

## Find a sum average until enter "done"

:::output
Enter a command: <span class="pyinput">12</span>
Enter a command: <span class="pyinput">31</span>
Enter a command: <span class="pyinput">done</span>
avg: 21.5
:::

:::output
Enter a command: <span class="pyinput">534</span>
Enter a command: <span class="pyinput">87</span>
Enter a command: <span class="pyinput">23</span>
Enter a command: <span class="pyinput">33</span>
Enter a command: <span class="pyinput">done</span>
avg: 169.25
:::

::: details Solution
```py
sum=0
n=0
while(True):
    data=input("Enter Number: ")
    if(data!="done"):
        sum+=float(data)
        n+=1
    else:
        break
print(f"avg : {sum/n}")
```
:::

## Find max value

:::output
Enter a command: <span class="pyinput">12</span>
Enter a command: <span class="pyinput">31</span>
Enter a command: <span class="pyinput">done</span>
max: 31.0
:::

:::output
Enter a command: <span class="pyinput">-12</span>
Enter a command: <span class="pyinput">60</span>
Enter a command: <span class="pyinput">0</span>
Enter a command: <span class="pyinput">5</span>
Enter a command: <span class="pyinput">done</span>
max: 60
:::

:::output
Enter a command: <span class="pyinput">-12</span>
Enter a command: <span class="pyinput">-5</span>
Enter a command: <span class="pyinput">-20</span>
Enter a command: <span class="pyinput">-4</span>
Enter a command: <span class="pyinput">done</span>
max: -4.0
:::

::: details Solution
```py
current_max = None
while True:
    data = input("Enter a command: ")
    if(data == "done"):
        break
    data = float(data)
    if(current_max is None):
        current_max = data
    if(data > current_max):
        current_max = data
print(f"max: {current_max}")
```
:::