# Divide-and-conquer algorithm: Summation

## Sum

### General formula

$$sum(N) = 1 + 2 + 3 + ... + N$$

### Example

$$sum(10) = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10$$

## Divide-and-conquer

### Iterative case

#### General formula

$$sum(N) = N + sum(N-1)$$

#### Example


$$sum(10) = 10 + sum(9)$$
$$sum(9)  = 9 + sum(8)$$
$$sum(8)  = 8 + sum(7)$$
$$sum(7)  = 7 + sum(6)$$
$$sum(6)  = 6 + sum(5)$$
$$sum(5)  = 5 + sum(4)$$
$$sum(4)  = 4 + sum(3)$$
$$sum(3)  = 3 + sum(2)$$
$$sum(2)  = 2 + sum(1)$$

### Base case

$$sum(1) = 1$$

## Coding

```py
def find_sum(n):

    if n == 1:
        return 1
    else:
        return n + find_sum(n-1)

print(find_sum(10))
```

:::output
55
:::