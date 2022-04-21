# Fibonacci Series

$$ F_0 = 0, F_1 = 1$$

$$ F_n = F_{n-1} + F_{n-2}$$

```
n   => 0  1  2  3  4  5  6   7   8   9  10  11   12
F_n => 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
```
:::output
Enter n: <span class="pyinput">6</span>
0 1 1 2 3 5 8
:::

:::output
Enter n: <span class="pyinput">20</span>
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
:::

::: details Solution
```py
def print_fibonacci_series(n):

    before_two_time=0
    before_one_time=1
    now = before_one_time + before_two_time
    for i in range(n+1):
        if i==0:
            print(0, end=" ")
        if i==1:
            print(1, end=" ")
        if i>=2:
            print(now, end=" ")
            before_two_time = before_one_time
            before_one_time = now
            now = before_two_time +before_one_time
n=int(input("Enter n: "))
print_fibonacci_series(n)
```
:::