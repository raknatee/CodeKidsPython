# While Loop
Computers are great at doing boring tasks without complaining. Programmers aren’t, but they are good at getting computers to do repetitive work for them—by using loops. **A loop runs the same block of code over and over again**. There are several different types of loop.

```py
print(0)
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
```

using while loop

```py
i = 0
while( i<10 ):
	print(i)
	i = i+1
```
## Using While Loop
- ```while``` loop always do the job when condition is ```True``` and always stop when condition is ```False```
```py
i = 0
while( i<10 ):
	print(i)
	i = i+1
```
::: details Debugging process
```py{1}
i = 0
while( i<10 ):
	print(i)
	i = i+1
```
Currently, ```i``` = 0
<hr class="line">

```py{2}
i = 0
while( i<10 ):
	print(i)
	i = i+1
```
```i=0```, ```i<10``` => ```while(True)```
<hr class="line">

```py{3}
i = 0
while( i<10 ):
	print(i)
	i = i+1
```
```i=0```, ```print(i)``` => ```print(0)```
<hr class="line">

```py{4}
i = 0
while( i<10 ):
	print(i)
	i = i+1
```
```i=0```, ```i=i+1``` => ```i=0+1``` => ```i=1```
<hr class="line">

keep going and **repeat** while loop
```py{2}
i = 0
while( i<10 ):
	print(i)
	i = i+1
```
```i=1```, ```i<10``` => ```while(True)```
<hr class="line">

```py{3}
i = 0
while( i<10 ):
	print(i)
	i = i+1
```
```i=1```, ```print(i)``` => ```print(1)```
<hr class="line">

```py{4}
i = 0
while( i<10 ):
	print(i)
	i = i+1
```
```i=1```, ```i=i+1``` => ```i=1+1``` => ```i=2```
<hr class="line">

keep going and **repeat** while loop
```py{2}
i = 0
while( i<10 ):
	print(i)
	i = i+1
```
```i=2```, ```i<10``` => ```while(True)```
<hr class="line">

```py{3}
i = 0
while( i<10 ):
	print(i)
	i = i+1
```
```i=2```, ```print(i)``` => ```print(2)```
<hr class="line">

```py{4}
i = 0
while( i<10 ):
	print(i)
	i = i+1
```
```i=2```, ```i=i+1``` => ```i=2+1``` => ```i=3```
<hr class="line">

keep going and **repeat** while loop...
skip to ```i=9```

```py{2}
i = 0
while( i<10 ):
	print(i)
	i = i+1
```
```i=9```, ```i<10``` => ```while(True)```
<hr class="line">

```py{3}
i = 0
while( i<10 ):
	print(i)
	i = i+1
```
```i=9```, ```print(i)``` => ```print(9)```
<hr class="line">

```py{4}
i = 0
while( i<10 ):
	print(i)
	i = i+1
```
```i=9```, ```i=i+1``` => ```i=9+1``` => ```i=10```
<hr class="line">

keep going and **repeat** while loop...
```py{2}
i = 0
while( i<10 ):
	print(i)
	i = i+1
```
```i=10```, ```i<10``` => ```while(False)```
<hr class="line">
:::


::: details output
:::output
0
1
2
3
4
5
6
7
8
9
:::


```py
i = 0
while( i<10 ):
	print(i)
	i = i+2
```
::: details output
:::output
0
2
4
6
8
:::

```py
i = 1
while( i<10 ):
	print(i)
	i = i*2
```

::: details output
:::output
1
2
4
8
:::


## Break and Continue
- If ```break``` is activated, the loop would be stopped.
- If ```continue``` is activated, the loop would be skipped. The current state will jump to the next state.

```py
i=0
while( i<10 ):
	if(i > 5):
		break
	print(i) 	
	i=i+1
```
::: output
0
1
2
3
4
5
:::

```py
i=0
while( i<10 ):
    i+=1
    if(i < 5):
        continue
    print(i)
```
::: output
5
6
7
8
9
10
:::

## Let's start coding together
- Note command

::: output
Hello!
add note or show note: <span class="pyinput"> today my plan is ... </span>
add note or show note: <span class="pyinput">and next ...</span>
add note or show note: <span class="pyinput">show</span>
['today my plan is ...', 'and next ...']
add note or show note: <span class="pyinput">sleep</span>
add note or show note: <span class="pyinput">show</span>
['today my plan is ...', 'and next ...', 'sleep']
add note or show note: <span class="pyinput">exit</span>

:::

::: details Solution
```py
print("Hello!")
data=[]
while(True):
    line=input("add note or show note: ")
    if(line=="show"):
        print(data)
    else:
        if(line=="exit"):
            break
        else:
            data.append(line)
```
:::

## ***Exercise Book*** 11.While Loop