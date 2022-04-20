# None Value

In Python, there is one value **None**. That means, this variable does not contain anything. Just nothing...

```py
a = None
```

Therefore, we can assign something later. 

For example
```py
a = None
print(a)
print(a is None)
if a is None:
    a = 10
print(a)
```
::: details output
::: output
None
True
10
:::


::: danger
For checking **None**, please use those keywords.
- **is** 
- **is not**
::: 
