# 0x02. Minimum Operations

## Algorithm | Python

**Weight:** 1

## Concepts Needed

To effectively tackle the "Minimum Operations" problem, I will familiarize myself with the following concepts:

### Dynamic Programming

- Understanding dynamic programming will help in breaking down the problem into simpler subproblems and building up the solution.
- [Dynamic Programming (GeeksforGeeks)](https://www.geeksforgeeks.org/fundamentals-of-algorithms/#dynamic-programming)

### Prime Factorization

- Knowing how to perform prime factorization is crucial since the problem can be reduced to finding the sum of the prime factors of the target number `n`.
- [Prime Factorization (Khan Academy)](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86a7d3b6b4c0f6e62f4e9f2f9)

### Code Optimization

- Approaching problems from an optimization perspective is useful for finding the most efficient solution.
- [How to optimize Python code](https://realpython.com/python-optimization/)

### Greedy Algorithms

- The problem can also be approached with greedy algorithms, choosing the best option at each step.
- [Greedy Algorithms (GeeksforGeeks)](https://www.geeksforgeeks.org/greedy-algorithms/)

### Basic Python Programming

- Proficiency in Python, including loops, conditionals, and functions, is necessary to implement the solution.
- [Python Functions (Python Official Documentation)](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

By studying these concepts and utilizing the provided resources, I will be equipped to effectively solve the "Minimum Operations" problem, applying both mathematical reasoning and programming skills.

## Additional Resources

- Mock Technical Interview

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All my files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3).
- All my files should end with a new line.
- The first line of all my files should be exactly `#!/usr/bin/python3`.
- A `README.md` file, at the root of the folder of the project, is mandatory.
- My code should be documented.
- My code should use PEP 8 style (version 1.7.x).
- All my files must be executable.

## Task

### 0. Minimum Operations

**Mandatory**  
Write a method that calculates the fewest number of operations needed to result in exactly `n` `H` characters in a text file, where the only operations allowed are "Copy All" and "Paste".

#### Prototype

```python
def minOperations(n):
```

- **Returns:** An integer representing the minimum number of operations.
- If `n` is impossible to achieve, return `0`.

### Example

```python
n = 9

H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
```

### Sample Code for Testing

```python
carrie@ubuntu:~/0x02-minoperations$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

carrie@ubuntu:~/0x02-minoperations$ ./0-main.py
Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
```

## Repository

- **GitHub Repository:** [alx-interview](https://github.com/martinnyemba/alx-interview)  
- **Directory:** `0x02-minimum_operations`  
- **File:** `0-minoperations.py`
