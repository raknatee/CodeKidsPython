# Fibonacci Number

$$ F_0 = 0, F_1 = 1$$

$$ F_n = F_{n-1} + F_{n-2}$$

```
n   => 0  1  2  3  4  5  6   7   8   9  10  11   12
F_n => 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
```
:::output
Enter n: <span class="pyinput">6</span>
8
:::

::: details Solution
```py
def fibonacci(n):
    if(n==0):
        return 0
    else:
        if(n==1):
            return 1
        else:
            before_two_time=0
            before_one_time=1
            now = before_one_time + before_two_time
            for i in range(2,n+1):
                now= before_one_time + before_two_time
                before_two_time = before_one_time
                before_one_time = now
            return now
n=int(input("Enter n: "))
print(fibonacci(n))
```
:::