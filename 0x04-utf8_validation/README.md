# 0x04. UTF-8 Validation
# UTF-8 Validation

## Description
This project implements a UTF-8 validation algorithm in Python. The main task is to create a method that determines if a given data set represents a valid UTF-8 encoding by analyzing the byte patterns in the input data.

## Project Information
- **Algorithm Type**: Bitwise Operations
- **Programming Language**: Python
- **Project Directory**: 0x04-utf8_validation

## Concepts Covered
- Bitwise Operations in Python
- UTF-8 Encoding Scheme
- Data Representation
- List Manipulation
- Boolean Logic

## Prerequisites
Before tackling this project, make sure you understand:
- How UTF-8 characters are encoded into 1-4 bytes
- Python bitwise operators (AND, OR, XOR, NOT, shifts)
- Working with binary data in Python
- Basic list operations and comprehensions

## Project Requirements

### General
- All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3
- Code should follow PEP 8 style guide (version 1.7.x)
- All files must be executable
- All files should end with a newline
- First line of all files should be exactly `#!/usr/bin/python3`

### Editors Allowed
- vi
- vim
- emacs

## Tasks

### 0. UTF-8 Validation (mandatory)
Implement a method that validates UTF-8 encoding.

**Function Prototype:**
```python
def validUTF8(data)
```

**Parameters:**
- `data`: List of integers where each integer represents 1 byte of data

**Return Value:**
- `True` if data is a valid UTF-8 encoding
- `False` otherwise

**Constraints:**
- Handle only the 8 least significant bits of each integer
- UTF-8 characters can be 1 to 4 bytes long
- Input data set may contain multiple characters


## Resources
- [Python Bitwise Operators](https://wiki.python.org/moin/BitwiseOperators)
- [UTF-8 Wikipedia](https://en.wikipedia.org/wiki/UTF-8)
- [Characters, Symbols, and Unicode](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)


## License
Copyright © 2024 ALX, All rights reserved.
## Example :
    carrie@ubuntu:~/0x04-utf8_validation$ cat 0-main.py
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

    carrie@ubuntu:~/0x04-utf8_validation$
    carrie@ubuntu:~/0x04-utf8_validation$ ./0-main.py
    True
    True
    False
    carrie@ubuntu:~/0x04-utf8_validation$
