# 0x00. Pascal's Triangle

## Algorithm | Python

## Resources

- [What is Pascal’s Triangle](https://en.wikipedia.org/wiki/Pascal's_triangle)
- [Pascal’s Triangle - Numberphile](https://www.youtube.com/watch?v=0E4DqU1H8g0)
- [What are Python Algorithms](https://en.wikipedia.org/wiki/Algorithm)

### Additional Resources

- Mock Technical Interview

## Must Know

To successfully complete this project, I should revise the following Python concepts:

### Lists and List Comprehensions

- Understand how to create, access, modify, and iterate over lists.
- Utilize list comprehensions for concise and readable code, especially for generating rows of Pascal’s Triangle.

### Functions

- Know how to define and call functions.
- Pass parameters and return values, particularly how to return a list of lists representing Pascal’s Triangle.

### Loops

- Use `for` and `while` loops to iterate through sequences.
- Nested loops may be necessary for generating each row and calculating the values of Pascal’s Triangle.

### Conditional Statements

- Apply `if`, `elif`, and `else` conditions to implement logic based on the position within Pascal’s Triangle (e.g., the edges of the triangle always being 1).

### Recursion (Optional)

- Understanding recursion can provide an alternative approach to generating Pascal’s Triangle.
- Recognize base cases and recursive cases for a function that generates the triangle’s rows.

### Arithmetic Operations

- Perform addition, a fundamental operation for calculating each element of Pascal’s Triangle as the sum of the two elements directly above it.

### Indexing and Slicing

- Access elements and slices of lists, crucial for identifying and summing the correct elements.

### Memory Management

- Be mindful of how lists are stored and copied, especially when creating new rows based on previous values.

### Error and Exception Handling (Optional)

- Use `try-except` blocks as needed to handle potential errors, such as invalid input types.

### Efficiency and Optimization

- Consider the time and space complexity of different approaches to generating Pascal’s Triangle.
- Evaluate and apply optimizations to improve performance.

## Task

### 0. Pascal's Triangle

**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)

Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing Pascal’s triangle of `n`:

- Returns an empty list if `n <= 0`.
- Assume `n` will always be an integer.

### Example

```bash
guillaume@ubuntu:~/0x00$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

guillaume@ubuntu:~/0x00$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
guillaume@ubuntu:~/0x00$
```

## Repository

- **GitHub Repository:** [alx-interview](https://github.com/martinnyemba/alx-interview)  
- **Directory:** `0x00-pascal_triangle`  
- **File:** `0-pascal_triangle.py`  

---

Copyright © 2024 ALX, All rights reserved.
