# Boolean

- Can be only ```True``` or ```False```
```py
bool1 = True
bool2 = False
```

## Logical operators

| Symbol | Meaning |
| --|---|
| == | equal
|!=| not equal
|<| less than
|>| greater than
|<=| less than or equal
|>= | greater than or equal

## Gate

### And Gate
```py
True  and True   == True
True  and False  == False
False and True   == False
False and False  == False
```

### Or Gate
```py
True  or True   == True
True  or False  == True
False or True   == True
False or False  == False
```

### Not Gate
```py
not True  == False
not False == True
```

***

## True or False ?

```py
1 < 3
5 < 2
3 == 3
```
::: details Solution
<span class="green">1 < 3</span><br>
<span class="red">5 < 2</span><br>
<span class="green">3 == 3</span><br>
:::

```py
3 != 3
4 > 10
1 <= 3
```
::: details Solution
<span class="red">3 != 3</span><br>
<span class="red">4 > 10</span><br>
<span class="green">1 <= 3</span><br>
:::

```py
5 <= 5
99 != 99
4 >= 4
```
::: details Solution
<span class="green">5 <= 5</span><br>
<span class="red">99 != 99</span><br>
<span class="green">4 >= 4</span><br>
:::

```py
"Hello" == "hello"
3 == "3"
"Hi" == "Hi"
"Hehe" != "Hehe"
```
::: details Solution
<span class="red">"Hello" == "hello"</span><br>
<span class="red">3 == "3"</span><br>
<span class="green">"Hi" == "Hi"</span><br>
<span class="red">"Hehe" != "Hehe"</span><br>
:::

## Let's practice together

```py
a = 5 > 3
print(a)
```
::: details output
:::output
True
:::

```py
a = 5 > 3
print(a and a>10)
```
::: details output
:::output
False
:::

```py
a = 5 > 3
b = 200 - 5 < 100
print(a or b)
```
::: details output
:::output
True
:::

```py
a = 5 > 3
b = a < 100
print(a or b)
```
::: details output
:::output
True
:::

```py
a = 5 > 3
b = a > 100
print(a and b)
```
::: details output
:::output
False
:::

```py
a = 10 < 5
b = 20 > 5
print(a and b and not b)
```
::: details output
:::output
False
:::


```py
a = 10 
b = 20
bool1 = a > 5
bool2 = b > a
print( (bool1 or bool2) and not bool2)

```
::: details output
:::output
False
:::


```py
a = 10 
b = 20
bool1 = a > 5
bool2 = b > a
print(bool1 or bool2 and not bool2)
```
::: details output
:::output
True
:::


::: warning why?
[short-circuit operator](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)

```or``` : This is a short-circuit operator, so it only evaluates the second argument if the first one is false.

```and```: This is a short-circuit operator, so it only evaluates the second argument if the first one is true.
:::




## ***Exercise Book*** 08.Boolean

