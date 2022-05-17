# 1. Print

code
```py
print("1")
print("2", end=" ")
print("3", end="!")
print("4", end="")
print(5)
```

output
```
1
2 3!45
```

# 2. Variable

code 
```py
a = 3
b = 4
c = (a**2 + b**2)**(0.5)
print(c)
```
output
```
5.0
```

# 3. None
```py
a = None
b = 5
if(a is None):
    a = 0
if(b is not None):
    b = None
print(a)
print(b)
```
```
0
None
```

# 4. Casting
```py
a = "10.5"
a = int(a)
print(a)
```

```
Traceback (most recent call last):
  File "<string>", line 2, in <module>
ValueError: invalid literal for int() with base 10: '10.5'
```

# 6. f-Strings

```py
a = 10
b = 20
print("a is {a}. b is {b}.")
a = 5
b = 11
print(f"a is {a}. b is {b}.")
```
```
a is {a}. b is {b}.
a is 5. b is 11.
```

# 8. Boolean

```py
print(10 < 20 < 100)
print(10 < 100 < 20)
```
```
True
False
```

# 9. If and Else

```py
print(1)
if(10 < 20):
    print(2)
if(0.5 > 1):
    print(3)
else:
    print(4)
```
```
1
2
4
```

# 10. List

```py
a = list(range(10))
print(a)
del a[5]
print(5 in a)
print(5 in a)
print(6 in a)
```
```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
False
False
True
```

# 11. While Loop

```py
i = 0
data = 0
while(True):
    print(f"{i} {data}")
    data = 2 ** i
    if(data > 2**8):
        break
    i = i + 1

print(f"{i} {data}")
```
```
0 0
1 1
2 2
3 4
4 8
5 16
6 32
7 64
8 128
9 256
9 512
```

# 12. For Loop
```py
for i in range(1,3):
    for j in range(1,i+1):
        print(j)
```
```
1
1
2
```

# 14. Function
```py
a = 10
b = 5


def my_func_1(a):
    return a+1


def my_func_2(b):
    return a+1

print(my_func_1(b))
print(my_func_2(b))
```
```
6
11
```