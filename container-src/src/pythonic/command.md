# Computer: Basic Commands

## pwd
return current directory

```sh
pwd
```


## ls
list all file and directory in current directory
```sh
ls
```

## cd

Changes Directory

    - ./ => refer to current directory
    - ../ => refer to previous directory


```sh
pwd
```

output
```
/.../
```

```sh
ls
```

output
```
code.py text_file.txt folder-1 folder-2
```

```sh
cd ./folder-1
pwd
```

output
```
/.../folder-1
```

```sh
cd ../
pwd
```

output

```
/.../
```

## cat
shows content of file

```sh
ls
```

output
```
code.py text_file.txt folder-1 folder-2
```

```sh
cat ./code.py
```

output
```
print("HelloWorld")
```

## Running Python Script with command line

```sh
ls
```

output
```
code.py text_file.txt folder-1 folder-2
```

```sh
cat ./code.py
```

output
```
print("HelloWorld")
```

### Runs the Python Script
```sh
python3.10 main.py
```

output
```
HelloWorld
```