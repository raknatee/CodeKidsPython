# Casting

## How to get Type of some variables

- uses function ```type(?)```
```py
a = 10
print(type(a))

a = 10.0
print(type(a)) 

a = "10"
print(type(a))
```
::: output
<class 'int'>
<class 'float'>
<class 'str'>
:::

## Casting
- Example 1
```py
a = str(10)
print(type(a))

a = str(10.0)
print(type(a)) 

a = int("10")
print(type(a))

a = float("10")
print(type(a))
```
::: details output
::: output
<class 'str'>
<class 'str'>
<class 'int'>
<class 'float'>
:::

- Example 2
```py
a = 10
a = str(a)
print(type(a))
```
::: details output
::: output
<class 'str'>
:::

- Example 3
```py
a = 10
b = str(a)
print(type(a))
print(type(b))
```
::: details output
::: output
<class 'int'>
<class 'str'>
:::

- Example 4
```py
a = 4
a = str(a)
b = "5"
print(a+b)
print(type(a))
print(type(b))
```
::: details output
::: output
45
<class 'str'>
<class 'str'>
:::

- Example 5
```py
a = 4
b = "5"
b = int(b)
print(a+b)
print(type(a))
print(type(b))
```
::: details output
::: output
9
<class 'int'>
<class 'int'>
:::

- Example 6
```py
a = 4
b = "5"
print(str(a)+b)
print(type(a))
print(type(b))
```
::: details output
::: output
45
<class 'int'>
<class 'str'>
:::

- Example 7
```py
a = 4
b = "5"
print(a+int(b))
print(type(a))
print(type(b))
```
::: details output
::: output
9
<class 'int'>
<class 'str'>
:::





