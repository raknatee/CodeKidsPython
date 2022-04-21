# Dictionary
Normally, when we want to store the data in ```list``` and use **index** for data access.

However, ```dict``` is similar to ```list``` but it uses **key** insteads of **index**.

::: tip
```list``` uses index (number) for data access.

```dict``` uses key (string) for data access.
:::

## Review List

```python
a_list = ["Hello", 1, 2, "World"]
a_list[0]
a_list[1]
a_list[2]
a_list[3]
```

## Using Dict
```py
dict_a = {"word":"Hello","number":1}
dict_b = {"k1":1,
          "k2":2}
```

### data access
```py
dict_a = {"word":"Hello","number":1}
dict_b = {"k1":1,
          "k2":2}

print(dict_a["word"])
print(dict_a["number"])
dict_b["k2"] = dict_a["number"] + dict_b["k2"]
print(dict_b)
```
:::output
Hello
1
{'k1': 1, 'k2': 3}
:::

```py
dict_a = {"k1":1,
          "k2":50,
          "k3":"Hello"}

for k in dict_a:
    print(f"key is {k}, value is {dict_a[k]}")
```
:::output
key is k1, value is 1
key is k2, value is 50
key is k3, value is Hello
:::

### add new key and value
```py
dict_a = {"k1":1,
          "k2":50,
          "k3":"Hello"}
dict_a["k4"] = "World"
print(dict_a)
```
:::output
{'k1': 1, 'k2': 50, 'k3': 'Hello', 'k4': 'World'}
:::

### del
```py
dict_a = {"k1":1,
          "k2":50,
          "k3":"Hello"}
dict_a["k4"] = "World"
del dict_a["k2"] 
print(dict_a)
```
:::output
{'k1': 1, 'k3': 'Hello', 'k4': 'World'}
:::

### in
- ```in``` is used for checking the **key**.
```py
dict_a = {"k1":1,
          "k2":50,
          "k3":"Hello"}
print("k1" in dict_a)
print("Hello" in dict_a)
```

:::output
True
False
:::