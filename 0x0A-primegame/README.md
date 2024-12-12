# 0x0A. Prime Game

## Description

**Prime Game** is a competitive game that challenges players to strategically remove prime numbers and their multiples from a set of consecutive integers. This project is designed to enhance your understanding of algorithms, prime numbers, and game theory while solving a Python-based problem.

Maria and Ben are the players. Given a set of integers from `1` to `n`, they take turns picking a prime number, removing it, and all its multiples. The player unable to make a move loses. The goal is to determine the overall winner after `x` rounds of the game.

---

## Learning Objectives

### Key Concepts:
- **Prime Numbers**:
  - Understanding and identifying prime numbers.
  - Efficient algorithms for finding prime numbers in a range.

- **Sieve of Eratosthenes**:
  - Optimized technique to compute prime numbers up to a given limit.

- **Game Theory**:
  - Principles of strategic decision-making.
  - Understanding win conditions and optimal play strategies.

- **Dynamic Programming/Memoization**:
  - Optimizing calculations using previously computed results.

- **Python Programming**:
  - Using loops, conditions, lists, and arrays.
  - Adhering to Python’s PEP8 guidelines.

---

## Requirements

- **Environment**:
  - OS: Ubuntu 20.04 LTS
  - Python version: 3.4.3
  
- **General**:
  - Files must end with a new line.
  - First line: `#!/usr/bin/python3`.
  - Code must be PEP 8 compliant.
  - All files must be executable.

- **Repository Setup**:
  - GitHub repository: `alx-interview`
  - Directory: `0x0A-primegame`
  - File: `0-prime_game.py`

---

## Usage

### Prototype:
```python
def isWinner(x, nums):
    """
    Determines the winner of the Prime Game after x rounds.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers (n) for each round.

    Returns:
        str: Name of the player who won the most rounds ('Maria' or 'Ben').
        None: If there's no overall winner.
    """
```

### Example:
```bash
$ cat main_0.py
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

$ ./main_0.py
Winner: Ben
```

---

## Tasks

### 0. Prime Game
- **Objective**: Implement the function `isWinner(x, nums)` to determine the winner after `x` rounds.
- **Constraints**:
  - `x` and `n` will not exceed `10,000`.
  - No package imports allowed.

#### Example:
Given:
```python
x = 3
nums = [4, 5, 1]
```

**Results**:
1. Round 1 (`n = 4`): Ben wins.
2. Round 2 (`n = 5`): Maria wins.
3. Round 3 (`n = 1`): Ben wins.

Final winner: **Ben**.

---

## Resources

### Prime Numbers and Algorithms:
- [Khan Academy: Prime Numbers](https://www.khanacademy.org)
- [Sieve of Eratosthenes in Python](https://www.geeksforgeeks.org)

### Game Theory:
- [Game Theory Basics](https://www.investopedia.com)

### Dynamic Programming:
- [What is Dynamic Programming](https://realpython.com)

### Python Documentation:
- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)

---

## Author
**Martin Nyemba**
