# UTF-8 Validation
This project focuses on a task to validate UTF-8 encoding.

## Task
Write a method that determines if a given data set represents a valid UTF-8 encoding.
* Prototype: `def validUTF8(data)`
* Return: `True` if data is a valid UTF-8 encoding, else return `False`
* A character in UTF-8 can be 1 to 4 bytes long
* The data set can contain multiple characters
* The data will be represented by a list of integers
* Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer

## Usage
1. Create a python file named `0-main.py`.
2. In the file paste the code below:
```python
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))
```
3. Run the program:
```sh
./0-main.py
```

## Output
```sh
True
True
False
```
You can play around with the data list to test the function.

## Resources
* [UTF-8](https://en.wikipedia.org/wiki/UTF-8)
* [Characters, Symbols, and the Unicode Miracle](https://www.youtube.com/watch?v=MijmeoH9LT4)

## License
This project is licensed under the [MIT License](../LICENSE).