![img](./logo.png)

# ClassWorks
 
## Requirement

::: warning Recommended local Installation
1. [Python](https://www.python.org/) ( recommands Python Version 3.10 ++)
    - IDLE for Python IDE (alreadys installed with Python)
2. (Optional) IDE (For example, [VS Code](https://code.visualstudio.com/))
:::

1. [HelloWorld (print)](./classwork/HelloWorld.md)
1. [Variable, Type of Variable, Operator](./classwork/Variable/Variable.md)
1. [None value](./classwork/NoneValue.md)
1. [Casting](./classwork/Casting.md)
1. [I/O](./classwork/IO.md)
1. [f-Strings](./classwork/FString.md)
1. [1st Exercises](./classwork/FirstEx/FirstEx.md)
1. [Boolean](./classwork/Boolean/Boolean.md)
1. [If and Else](./classwork/IFElse.md)
1. [List and List's method](./classwork/List/List.md)
1. [Loop: While loop](./classwork/WhileLoop/WhileLoop.md)
1. [Loop: For loop](./classwork/ForLoop/ForLoop.md)
1. [2nd Exercises](./classwork/SecondEx/SecondEx.md)
1. [Function](./classwork/Function.md)
1. [Nested List (List in List)](./classwork/ListInList.md)
1. [Dictionary](./classwork/Dict.md)
1. [Data container (Dictionary for data/object representation)](./classwork/DataContainer.md)

# Python-AddOn

## Advanced Drawing

### Requirement

::: warning Recommended local Installation
1. [Python](https://www.python.org/)
2. IDE (For example, [VS Code](https://code.visualstudio.com/))
:::

- [Python: Import and Modules](./addon-lesson/AdvancedDrawing/import.md)

### Workshop

- [I AM IRONMAN](./addon-lesson/AdvancedDrawing/IAmIronman-1.md) -> [I AM IRONMAN with animation](./addon-lesson/AdvancedDrawing/IAmIronman-2.md)

- [Multiple Turtles: Bloody Moon](./addon-lesson/AdvancedDrawing/BloodyMoon.md)

## Math Problems & Data structures and Algorithms

### Workshop
- [Is that Prime number?](./addon-lesson/math-dsa/Prime.md) -> [Prime number between 1-100](./addon-lesson/math-dsa/Primes.md)
- [Fibonacci Number](./addon-lesson/math-dsa/fibon.md) -> [Fibonacci Series](./addon-lesson/math-dsa/fibon-s.md)
- [Data Structure: Stack]
- [Data Structure: Quene]
- [Bubble sort](./addon-lesson/math-dsa/BubbleSort.md)
- [Pyramid]
- Divide-and-conquer algorithm 
    - [Fibonacci number] -> [Sum] -> [Binary Search]

## Microcontroller (ESP32)
### Requirement

::: warning Recommended local Installation
1. [Thonny](https://thonny.org/)
2. [Hardware List]
:::

- [Understand ESP32 and Micropython]

### Workshop
- [Basic LED Electric Circuit]


## Junior Data Engineer

### Requirement

::: warning Recommended local Installation
1. [Python](https://www.python.org/)
2. IDE (For example, [VS Code](https://code.visualstudio.com/))
:::

- [Python: String's method](./addon-lesson/DE/String.md)
- [Python: File Handling](./addon-lesson/DE/File.md)

### Workshop
- [How much salary for your employee(s)?](./addon-lesson/DE/Salary.md)
- [Word Count](./addon-lesson/DE/WordCount.md)


## Junior Data Scientist

### Requirement
There are many ways to do this workshop. You can use Cloud servies or install locally.

::: warning Recommended Cloud service
1. [Google Colab](https://colab.research.google.com/)
:::

::: warning Recommended local Installation
1. [Python](https://www.python.org/)
2. IDE (For example, [VS Code](https://code.visualstudio.com/))
3. (Optional) Environment manager: [Docker](./addon-lesson/DS/env/Docker/Index.md) or **pipenv**
 - If you decided to use **Docker**, you can skip 4th step.
4. Dependencies

- Global ```pip``` for Windows

```sh
pip install "numpy==1.22.3"
pip install "pandas==1.4.2"
pip install "matplotlib==3.5.1"
pip install "ipykernel==6.13.0"
```

- Global ```pip``` for MacOSX and Linux Distributions

```sh
pip3 install "numpy==1.22.3"
pip3 install "pandas==1.4.2"
pip3 install "matplotlib==3.5.1"
pip3 install "ipykernel==6.13.0"
```

- Locally install for project using ```pipenv```
```sh
# Windows
pip install pipenv
# MacOSX and Linux Distributions
pip3 install pipenv
```

!!!!!!!! Please prepare **your project folder** before doing this. !!!!!!!!
```sh
pipenv install --python 3.10
pipenv install "numpy==1.22.3"
pipenv install "pandas==1.4.2"
pipenv install "matplotlib==3.5.1"
pipenv install "ipykernel==6.13.0"
```
You might see those files in your project folder.

```
+-- your-project-folder
|    +-- Pipfile		
|    +-- Pipfile.lock
```

:::

- [Basic Graph with Matplotlib](./addon-lesson/DS/BasicGraph.md)

### Workshop
- [How satisfied are you? (Data Distribution)](./addon-lesson/DS/DataDis.md)
- [I know the future! (Linear Regression with Normal Equation)](./addon-lesson/DS/LR_with_NE.md)