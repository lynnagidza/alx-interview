# Island Perimeter
This project is about finding the perimeter of an island represented by a grid.

## Requirements
[![Ubuntu](https://img.shields.io/badge/Ubuntu-14.04_LTS-orange)](https://www.ubuntu.com/download/desktop)
[![Python](https://img.shields.io/badge/Python-3.4.3-blue)](https://www.python.org/downloads/release/python-343/)
[![Style](https://img.shields.io/badge/Style-Pep8-lightgrey)](https://www.python.org/dev/peps/pep-0008/)

## Tasks
### 0. Island Perimeter
Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in `grid`:

- `grid` is a list of list of integers:
    - 0 represents water
    - 1 represents land
    - Each cell is square, with a side length of 1
    - Cells are connected horizontally/vertically (not diagonally).
    - `grid` is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing).
- The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).

## Example
```python
>>> grid = [[0, 0, 0, 0, 0, 0],
...         [0, 1, 0, 0, 0, 0],
...         [0, 1, 0, 0, 0, 0],
...         [0, 1, 1, 1, 0, 0],
...         [0, 0, 0, 0, 0, 0]]
>>> island_perimeter(grid)
12
```

## Example Usage
- Create a file called 0-main.py
- Copy the following into `0-main.py`:
```python
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))

```
- Run the file from your terminal:
```bash
./0-main.py
```
- If your output looks like this, then you are on the right track!
```bash
12
```

## License
This project is licensed under the [MIT License](../LICENSE).
