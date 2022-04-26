# Sorting algorithms
- There are many sorting sorting algorithms. For example, [Bubble sort](https://en.wikipedia.org/wiki/Bubble_sort), [Merge sort](https://en.wikipedia.org/wiki/Merge_sort), [Insertion sort](https://en.wikipedia.org/wiki/Insertion_sort), [Quicksort](https://en.wikipedia.org/wiki/Quicksort), etc.

# Bubble sort

## Swapping in Python

```py
a = 30
b = 90
print(a)
print(b)
```
:::output
30
90
:::

```py
a = 30
b = 90
a,b = b,a
print(a)
print(b)
```

:::output
90
30
:::

## Bubble sort algorithm

### Initialize

![img](./BubbleSort-Img/loop1/Picture1.svg)


::: details 1st Iteration

![img](./BubbleSort-Img/loop1/Picture2.svg)

```
if 5 > 9 then Swap
```

![img](./BubbleSort-Img/loop1/Picture3.svg)

```
if 9 > 3 then Swap
```

![img](./BubbleSort-Img/loop1/Picture4.svg)

```
Swap
```

![img](./BubbleSort-Img/loop1/Picture5.svg)

```
if 9 > 1 then Swap
```

![img](./BubbleSort-Img/loop1/Picture6.svg)
```
Stop
```
:::

![img](./BubbleSort-Img/loop2/1.svg)

::: details 2nd Iteration

![img](./BubbleSort-Img/loop2/2.svg)
```
if 5 > 3 then Swap
```
![img](./BubbleSort-Img/loop2/3.svg)
```
Swap
```
![img](./BubbleSort-Img/loop2/4.svg)

```
if 5 > 1 then Swap
```


![img](./BubbleSort-Img/loop2/5.svg)
```
Swap
```

![img](./BubbleSort-Img/loop2/6.svg)
```
Stop
```

:::

```
keep repecting to 4th Iteration
```

### Finalize

![img](./BubbleSort-Img/loop4/final.svg)

## Python Implementation

```py
arr = [564, 11, 300, 0, -90, 60, 60]

def bubble_sort(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]

bubble_sort(arr)
print(arr)
```

:::output
[-90, 0, 11, 60, 60, 300, 564]
:::