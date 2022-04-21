# Function

- Function is a group of many commands.
- We had used a lot of function before this lesson. For example, 
    
    ```len``` ```print``` ```range``` and more.

## How to define our own function

- uses ```def``` keyword following with the name of function

```py
def introduce():
    print("Hi, My name is CodeKids. I am 4 years old.")
```
:::output
:::
- Does not have any output? Why? We need to **call** them.

```py
def introduce():
    print("Hi, My name is CodeKids. I am 4 years old.")
introduce()
```
:::output
Hi, My name is CodeKids. I am 4 years old.
:::

## Function argument(s)

```py
def introduce(name, age):
    print(f"Hi, My name is {name}. I am {age} years old.")

introduce("CodeKids",4)
introduce("CodeKit",5)
```
:::output
Hi, My name is CodeKids. I am 4 years old.
Hi, My name is CodeKit. I am 5 years old.
:::

## return keyword

- ```return``` keyword is used for return some value back to somebody who make a call to particular function.
- Moreover, if the ```return``` is executed, the function would **stop** itself.

```py
def my_plus(a, b):
    return a+b

data = my_plus(3, 4)
print(data)

data2 = my_plus("3", "4")
print(data2)
```
:::output
7
34
:::

::: details Debugging process
```py{4}
def my_plus(a, b):
    return a+b

data = my_plus(3, 4)
print(data)
```
<hr class="line">

```py{1}
def my_plus(a, b):
    return a+b

data = my_plus(3, 4)
print(data)
```
```my_plus(a, b)``` => ```my_plus(3, 4)``` => ```a=3```, ```b=4```
<hr class="line">

```py{2}
def my_plus(a, b):
    return a+b

data = my_plus(3, 4)
print(data)
```
```a=3```, ```b=4``` => ```return a+b``` => ```return 3+4``` => ```return 7```

<hr class="line">

```py{4}
def my_plus(a, b):
    return a+b

data = my_plus(3, 4)
print(data)
```
Therefore, ```my_plus(3, 4)``` == ```7``` => ```data = my_plus(3, 4)``` => ```data = 7```
<hr class="line">

:::

```py
def my_plus(a, b):
    print("HelloWorldddddddd")
    return a+b

data = my_plus(3, 4)
print(data)

data2 = my_plus("3", "4")
print(data2)
```
:::output
HelloWorldddddddd
7
HelloWorldddddddd
34
:::

```py
def my_plus(a, b):
    return a+b
    print("HelloWorldddddddd")

data = my_plus(3, 4)
print(data)

data2 = my_plus("3", "4")
print(data2)
```
:::output
7
34
:::