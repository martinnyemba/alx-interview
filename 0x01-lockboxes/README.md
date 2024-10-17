# 0x01. Lockboxes

## Algorithm | Python

### Must Know

To efficiently determine if all boxes can be opened, I will need a solid understanding of several key concepts:

### Concepts Needed

- **Lists and List Manipulation**
  - Understanding how to work with lists, including accessing elements, iterating over lists, and dynamically modifying lists.
  - [Python Lists (Python Official Documentation)]

- **Graph Theory Basics**
  - Knowledge of graph theory, especially traversal algorithms like Depth-First Search (DFS) or Breadth-First Search (BFS), as the boxes and keys can be thought of as nodes and edges in a graph.
  - [Graph Theory (Khan Academy)]

- **Algorithmic Complexity**
  - Understanding the time and space complexity of the solution helps in writing efficient algorithms.
  - [Big O Notation (GeeksforGeeks)]

- **Recursion**
  - Some solutions might require a recursive approach to traverse through the boxes and keys.
  - [Recursion in Python (Real Python)]

- **Queue and Stack**
  - Knowing how to use queues and stacks is crucial for implementing BFS or DFS algorithms.
  - [Python Queue and Stack (GeeksforGeeks)]

- **Set Operations**
  - Using sets for tracking visited boxes and available keys can optimize the search process.
  - [Python Sets (Python Official Documentation)]

By reviewing these concepts and utilizing the resources provided, I will be well-equipped to develop an efficient solution for this project.

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

### 0. Lockboxes


You have `n` locked boxes, each numbered sequentially from `0` to `n - 1`. Each box may contain keys to other boxes. Write a method to determine if all the boxes can be opened.

#### Prototype

```python
def canUnlockAll(boxes):
```

- **Input:** `boxes` is a list of lists.
- A key with the same number as a box opens that box.
- It can be assumed all keys will be positive integers.
- There can be keys that do not correspond to any box.
- The first box, `boxes[0]`, is unlocked.
- **Return:** `True` if all boxes can be opened; otherwise, return `False`.

### Example

```python
carrie@ubuntu:~/0x01-lockboxes$ cat main_0.py
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # False

carrie@ubuntu:~/0x01-lockboxes$ ./main_0.py
True
True
False
```

## Repository

- **GitHub Repository:** alx-interview
- **Directory:** `0x01-lockboxes`  
- **File:** `0-lockboxes.py`
