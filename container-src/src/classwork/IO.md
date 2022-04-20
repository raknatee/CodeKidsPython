# I/O (Input/Output)

- ```input()``` function allows user to type the text from the keyboard to your Python process!

```py
a = input()
print(a)
```
::: output
<span class="pyinput">CodeKids!</span>
CodeKids!
:::

## What is your name?
```py
name = input("What is your name?: ")
print("Nice to meet you!, " + name)
```
:::output
What is your name?: <span class="pyinput">CodeKids</span>
Nice to meet you!, CodeKids
:::

## Exercise Time!

- Find the sum of two numbers.
:::output
First Number: <span class="pyinput">10</span>
Second Number: <span class="pyinput">5</span>
Answer: 15.0
:::

::: details Solution
```py
a = input("First Number: ")
b = input("Second Number: ")
print("Answer: " + str(float(a)+float(b)) )
```
or
```py
a = float(input("First Number: "))
b = float(input("Second Number: "))
print("Answer: " + str(a+b) )
```
:::