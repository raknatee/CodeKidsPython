# Is that Prime number?

:::output
prime? : <span class="pyinput">1</span>
False
:::

:::output
prime? : <span class="pyinput">2</span>
True
:::

:::output
prime? : <span class="pyinput">3</span>
True
:::

:::output
prime? : <span class="pyinput">37</span>
True
:::

:::output
prime? : <span class="pyinput">45</span>
False
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

num = int(input("prime? :"))
print(is_prime(num))
```
:::