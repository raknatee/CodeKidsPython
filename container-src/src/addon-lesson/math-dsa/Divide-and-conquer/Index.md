# Divide-and-conquer algorithms

Divide-and-conquer algorithms are naturally implemented as recursive procedures. In that case, the partial sub-problems leading to the one currently being solved are automatically stored in the procedure call stack. A recursive function is a function that calls itself within its definition.

::: tip ref
[wikipedia](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm#:~:text=A%20divide%2Dand%2Dconquer%20algorithm,solution%20to%20the%20original%20problem.)
:::

## Definition

### Iterative case

$$T(N) = N' + T(N-1)$$

### Base case

$$T(1) = C$$