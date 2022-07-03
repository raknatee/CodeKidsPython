# Python: String's Method
- In this lesson, we will learn about what we can do on ```string```.

## in
```py
a = "HelloWorld"
print("Hello" in a)
print("he" in a)
```
:::output
True
False
:::

## split
- ```return``` the ```list``` of ```string``` which are splited.

```py
a = "   Hello 1 2 3     5    6 7    9 10 0"
print(a.split())

b = "Hello,1,2,3,5,9"
print(b.split(","))

c = "1-2-3-4-5-6    -7"
print(c.split("-"))
```
:::output
['Hello', '1', '2', '3', '5', '6', '7', '9', '10', '0']
['Hello', '1', '2', '3', '5', '9']
['1', '2', '3', '4', '5', '6    ', '7']
:::

## replace
- ```return``` new string which is replaced by some strings.
```py
a = "100000000000"
print(a.replace("0",""))

b = "HelloWorld"
print(b.replace("World","Hello2"))

c = "1-2-3-4-5-6-7"
print(c.replace("-"," "))
```
:::output
1
HelloHello2
1 2 3 4 5 6 7
:::

## strip
- ```return``` new string which is removed the whitespaces and tabs from head and tail.
```py
a = "    Hello World        "
print(a.strip())
```
::: output
Hello World
:::