# Python: Import and Modules

## project structure
```
+-- learn-how-to-import
|    +-- main.py
|    +-- my_code.py
```

### Keyword: **import**

my_code.py

<<< @/src/.vuepress/public/AdvancedDrawing/lesson01-python-importing/my_code.py

main.py

```py
import my_code

print(my_code.number)
my_code.add(5)
```

::: details output
```
10
15
```
:::

### Keyword: **from** **import**


main.py
```py
from my_code import number, add

print(number)
add(20)
```

::: details outout
```
10
30
```
:::

### Python Modules

### project structure
```{2,3,4}
+-- lesson-01
|    +-- other_code
     |    +-- __init__.py  
     |    +-- code_a.py  
|    +-- main.py
|    +-- my_code.py
```

./other_code/\_\_init\_\_.py (2 underscores + init + 2 underscores)

```py
```

./other_code/code_a.py

<<< @/src/.vuepress/public/AdvancedDrawing/lesson01-python-importing/other_code/code_a.py


main.py
```py
from other_code import code_a

code_a.say_hello("CodeKids")
print(code_a.a)


from other_code.code_a import say_hello

say_hello("CodeKids")
```

::: details output
```
Hi, my name is CodeKids
10
Hi, my name is CodeKids
```
:::

