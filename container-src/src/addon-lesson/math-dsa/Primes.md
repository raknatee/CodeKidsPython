# Prime number between 1-100

:::output
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
:::


::: details Solution
```py
def is_prime(num):
    if num == 1:
        return False
    else:
        is_prime = True
        for i in range(2,num):
            if(num%i == 0):
                is_prime = False
                break
        return is_prime

for i in range(1,101):
    if is_prime(i):
        print(i, end=" ")
```
:::