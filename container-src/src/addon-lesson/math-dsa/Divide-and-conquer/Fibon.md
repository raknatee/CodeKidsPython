# Divide-and-conquer algorithm: Fibonacci number

## Fibonacci number
```
n   => 0  1  2  3  4  5  6   7   8   9  10  11   12
F_n => 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
```

### General formula

$$ F_0 = 0, F_1 = 1$$

$$ F_n = F_{n-1} + F_{n-2}$$



## Divide-and-conquer

### Iterative case

#### General formula

$$F(N) = F(N-1) + F(N-2)$$

#### Example


$$F(5) = F(4) + F(3)$$


```mermaid
graph TB
    A(("F(5) = F(4) + F(3)"))-->B(("F(4) = F(3) + F(2)"))
    A-->C(("F(3) = F(2) + F(1)"))
    B-->D(("F(3) = F(2) + F(1)"))
    B-->E(("F(2) = F(1) + F(0)"))
    C-->F(("F(2) = F(1) + F(0)"))
    C-->G(("F(1) = 1"))
    D-->H(("F(2) = F(1) + F(0)"))
    D-->I(("F(1) = 1"))
    E-->J(("F(1) = 1"))
    E-->K(("F(0) = 0"))
    F-->L(("F(1) = 1"))
    F-->M(("F(0) = 0"))
    H-->N(("F(1) = 1"))
    H-->O(("F(0) = 0"))
   
```

### Base case

$$F(0) = 0,F(1) = 1$$

## Coding

```py
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(12))
```

:::output
144
:::