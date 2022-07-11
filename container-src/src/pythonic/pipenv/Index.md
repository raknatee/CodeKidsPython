---
sidebarDepth: 0
---
# Python: Python Package Manager - pipenv

## What is Environment in Computer ?
The **Environment** is the thing that defined why two rooms are different. Why would you choose to work at Library over your bedroom (or someone might choose otherwise). Why is your phone different from another phone. In UNIX, it is the same concept. Start from what package is installed, which version?. These are a part of **Environment**.

[Reference: AIT - Software Architecture Design](https://chaklam-silpasuwanchai.github.io/Software-Architecture/lab01/basic-terminal.html)

## What is pipenv ?

::: tip pipenv
[References: https://pipenv.pypa.io/en/latest/](https://pipenv.pypa.io/en/latest/)

Pipenv is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world. Windows is a first-class citizen, in our world.

It automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your Pipfile as you install/uninstall packages. It also generates the ever-important Pipfile.lock, which is used to produce deterministic builds.
:::

## Installation

::: warning
You might install Python3 FIRST!

Secondly, please check the Python environment variable path **For Windows**.
:::

### For UNIX family (MacOS, Ubuntu and Linux Distribution)
```sh
pip3 install pipenv
```

### For Windows 
```sh
pip install pipenv
```

## Tutorial #1

### project structure

#### Creates project directory
```
+-- root-path
|    +-- project-1
```

#### Creates .venv directory
```{3}
+-- root-path
|    +-- project-1
|       +-- .venv
```

#### Creates environment

```sh
cd /.../root-path/project-1
pipenv install
```
#### project structure
```
+-- root-path
|    +-- project-1
|       +-- .venv
|       +-- Pipfile
|       +-- Pipfile.lock
```

```sh
pipenv install requests==2.28.1
```

```sh
cat Pipfile
```

output
```
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
requests = "==2.28.1"

[dev-packages]

[requires]
python_version = "3.10"
```

#### Test Package

```{6}
+-- root-path
|    +-- project-1
|       +-- .venv
|       +-- Pipfile
|       +-- Pipfile.lock
|       +-- main.py
```

main.py

```py
import requests
print(requests.__version__)
```

```sh
pipenv run python main.py
```

output
```
2.28.1
```

## Tutorial #2

```{7-8}
+-- root-path
|    +-- project-1
|       +-- .venv
|       +-- Pipfile
|       +-- Pipfile.lock
|       +-- main.py
|    +-- project-2
|       +-- .venv
```

```sh
cd /.../root-path/project-2
pipenv install numpy==1.23.1
```

```{11}
+-- root-path
|    +-- project-1
|       +-- .venv
|       +-- Pipfile
|       +-- Pipfile.lock
|       +-- main.py
|    +-- project-2
|       +-- .venv
|       +-- Pipfile
|       +-- Pipfile.lock
|       +-- main.py
```

main.py
```py
import numpy
print(numpy.__version__)
```

```sh
pipenv run python main.py
```

output
```
1.23.1
```

main.py
```py{4-5}
import numpy
print(numpy.__version__)

import requests
print(requests.__version__)
```

```sh
pipenv run python main.py
```

output

```
  File "/.../root-path/project-2/main.py", line 4, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'
```