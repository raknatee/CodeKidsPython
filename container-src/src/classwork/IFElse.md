# If and Else

## If

- ```if``` will take action when condition is ```True```.

```py
if True:
    print("1")
```
::: details output
::: output
1
:::

```py
if False:
    print("1")
```
::: details output
::: output
:::

### Let's practice together

```py
a = 10
b = 20
if(a<b):
    print(1)
```
::: details output
::: output
1
:::


```py
a = 10
b = 20
if(a<b and b>100 and a<0):
    print(1)
```
::: details output
::: output

:::

```py
a = 10
b = 20
if(a<b and b<100):
    print(1)
    if(a < 0):
        print(2)
```
::: details output
::: output
1
:::

```py
a = 10
b = 20
if(a<b and b<100):
    print(1)
    if(a < 0):
        print(2)
    if(a > 0):
        print(3)
        if a == 10:
            print(4)
    if(a-10 == 0):
        print(5)
```
::: details output
::: output
1
3
4
5
:::

```py
a = 10
b = 20
if(not a>b):
    print(1)
```
::: details output
::: output
1
:::

```py
a = 10
b = 20
if(not (a>b) ):
    print(1)
```
::: details output
::: output
1
:::

### Let's start coding together
- To be given score. Then show the grade.

| Grade | Score |
| --|---|
| A | [80, 100] |
| B | [70, 80) |
| C | [60, 70)
| D | [50, 60)
| F | [0, 50)  


::: output
score: <span class="pyinput">99</span>
get A
:::

::: output
score: <span class="pyinput">50</span>
get D
:::

::: output
score: <span class="pyinput">72</span>
get B
:::

::: output
score: <span class="pyinput">49</span>
get F
:::

::: details Solution
```py
score=float(input("score: "))
if(score>=80 and score<=100):
    print("get A")
if(score>=70 and score<80):
    print("get B")
if(score>=60 and score<70):
    print("get C")
if(score>=50 and score<60):
    print("get D")
if(score>=0 and score<50):
    print("get F")
```
:::

### Let's start coding together (2)

- do the simple calculator

::: output
Number1: <span class="pyinput">5</span>
(+ - * /): <span class="pyinput">+</span>
Number2: <span class="pyinput">3</span>
8.0
:::

::: output
Number1: <span class="pyinput">5</span>
(+ - * /): <span class="pyinput">*</span>
Number2: <span class="pyinput">5</span>
25.0
:::

::: output
Number1: <span class="pyinput">9</span>
(+ - * /): <span class="pyinput">-</span>
Number2: <span class="pyinput">9</span>
0.0
:::

::: output
Number1: <span class="pyinput">9</span>
(+ - * /): <span class="pyinput">/</span>
Number2: <span class="pyinput">2</span>
4.5
:::

::: details Solution
```py
n1=float(input("Number1 : "))
op=input("(+ - * /): ")
n2=float(input("Number2 : "))
if(op=="+"):
    print(n1+n2)
if(op=="-"):
    print(n1-n2)
if(op=="*"):
    print(n1*n2)
if(op=="/"):
    print(n1/n2)
```
:::

### Let's start coding together (3)
- compare between two numbers
::: output
Enter first number: <span class="pyinput">50</span>
Enter second number: <span class="pyinput">1</span>
50.0 > 1.0
:::

::: output
Enter first number: <span class="pyinput">1</span>
Enter second number: <span class="pyinput">8</span>
1.0 < 8.0
:::

::: output
Enter first number: <span class="pyinput">5</span>
Enter second number: <span class="pyinput">5</span>
5.0 == 5.0
:::

::: details Solution
```py
a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
if(a<b):
    print(f"{a} < {b}")
if(a>b):
    print(f"{a} > {b}")
if(a==b):
    print(f"{a} == {b}")
```
:::

## Else
- ```else``` will take action if ```if``` statement which matchs with itself, is ```False```.
```py
if False:
    print("1")
else:
    print("2")
```
:::output
2
:::

### Let's practice together

```py
a = 10
b = 20
if(a<b):
    print(1)
else:
    print(2)
```
::: details output
::: output
1
:::

```py
a = 10
b = 20
if(not a<b):
    print(1)
else:
    print(2)
    if(a<b):
        print(3)
        if(a<0):
            print(4)
        else:
            print(5)
    else:
        print(6)
```
::: details output
::: output
2
3
5
:::