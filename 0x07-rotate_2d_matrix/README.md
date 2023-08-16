# Rotate 2D Matrix
Given an `n` x `n` 2D matrix, rotate the matrix by 90 degrees clockwise.
- Prototype: `def rotate_2d_matrix(matrix):`
- Do not return anything. The matrix must be edited in-place.
- You can assume the matrix will have 2 dimensions and will not be empty.

## Requirements
[![ubuntu](https://img.shields.io/badge/ubuntu-20.04_LTS-orange.svg?style=flat)](https://www.ubuntu.com/download/desktop)
[![python](https://img.shields.io/badge/python3-3.8.10-yellow.svg)](https://www.python.org/downloads/release/python-3810/)
[![style](https://img.shields.io/badge/pycodestyle-2.8.0-blue.svg)](https://pypi.org/project/pycodestyle/)

## Example
```python
>>> matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
>>> rotate_2d_matrix(matrix)
>>> print(matrix)
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

## Example Usage (with file)
### 1. Create a file named main_0.py with the following contents:
```bash
$ cat main_0.py
#!/usr/bin/env python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

```
### 2. Run the file:
```bash
$ ./main_0.py
[[7, 4, 1],
[8, 5, 2],
[9, 6, 3]]
```

## License
This project is licensed under the [MIT License](../LICENSE).
