# Making Change
This project is about making change for a given amount of money.

## Requirements
[![Ubuntu](https://img.shields.io/badge/Ubuntu-14.04_LTS-orange)](https://www.ubuntu.com/download/desktop)
[![Python](https://img.shields.io/badge/Python-3.4.3-blue)](https://www.python.org/downloads/release/python-343/)
[![Style](https://img.shields.io/badge/Style-Pep8-lightgrey)](https://www.python.org/dev/peps/pep-0008/)

## Task
### 0. Change comes from within
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount `total`.

- Prototype: `def makeChange(coins, total)`
- Return: fewest number of coins needed to meet `total`
    - If `total` is `0` or less, return `0`
    - If `total` cannot be met by any number of coins you have, return `-1`
- `coins` is a list of the values of the coins in your possession
- The value of a coin will always be an integer greater than `0`
- You can assume you have an infinite number of each denomination of coin in the list
- Your solution’s runtime will be evaluated in this task

## Examples
### Example 1
```python
>>> coins = [1, 2, 25, 10, 5]
>>> print(makeChange(coins, 10))
1
>>> print(makeChange(coins, 11))
2
>>> print(makeChange(coins, 20))
2
>>> print(makeChange(coins, 25))
1
```
### Example 2
```python
>>> print(makeChange([1, 2, 25], 37))
7
>>> print(makeChange([1256, 54, 48, 16, 102], 1453))
-1
```

## License
This project is licensed under the [MIT License](../LICENSE).
