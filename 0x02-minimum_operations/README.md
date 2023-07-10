# 0x02. Minimum Operations

This project focuses on solving the minimum operations problem using text editing operations. The goal is to calculate the fewest number of operations needed to result in exactly n occurrences of the character 'H' in a text file.

## Tasks

### Task 0: Minimum Operations

Write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

- Prototype: `def minOperations(n)`
- Returns an integer
- If `n` is impossible to achieve, return `0`

## Usage

To use the function `minOperations(n)`, follow these steps:

1. Import the function:

```python
from minoperations import minOperations
```
2. Call the function with the desired value of `n`:

```python
n = 4
print(minOperations(n))
```
3. The function will return the fewest number of operations needed to result in exactly `n` H characters in the file.

### Example Usage

```python
n = 4
print(minOperations(n))  # 4

n = 12
print(minOperations(n))  # 7

n = 9

# Steps:
# H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
# Number of operations: 6

result = minOperations(n)
print(result)  # Output: 6

```

## License

This project is licensed under the [MIT License](../LICENSE).
