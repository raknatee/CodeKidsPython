# File Handling

## Lesson Learn

- There are two types of files in computer.
    - **Binary File**: .exe .bin .xlsm (from Microsoft Excel) .docx (from Microsoft Word) .pdf .jpg
    - **Text File**: .txt .csv .py and more

- Therefore, we will learn how to handle **Text File** in Python.

## Open file for reading

### project structure
```
+-- some-folder
|    +-- text.txt
|    +-- main.py
```

text.txt
```
Hello
World
1234
```

main.py
```py
with open("text.txt","r") as read_file:
    while True:
        data_eachline = read_file.readline()
        if data_eachline == "":
            break
        print(data_eachline)
```
:::output
Hello

World

1234
:::

or 

main.py
```py
all_data = None
with open("text.txt","r") as read_file:
    all_data = read_file.readlines()       
print(all_data)
```
:::output
['Hello\n', 'World\n', '1234']
:::

## Open file for writing

### project structure
```
+-- some-folder-2
|    +-- main.py
```

```py
with open("new-file.txt","w") as write_file:
    write_file.write("Hello")
    write_file.write("World\n")
    write_file.write("555")

```
:::output
:::

```
+-- some-folder-2
|    +-- main.py
|    +-- new-file.txt
```

open new-file.txt
```
HelloWorld
555
```