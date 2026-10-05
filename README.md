# Python DSA Practice

A collection of 37 data-structure and algorithm problems solved in Python, one folder per problem. Each folder holds a standalone solution plus its own tests, written with `unittest`, `pytest` or a simple print/assert script. The set ranges from number-theory basics (GCD, primes, factorial) to classic interview problems (4Sum, Merge k Sorted Lists, Longest Substring Without Repeating Characters), using techniques such as two pointers, sliding window, binary search, stacks, heaps, backtracking, recursion on trees and iterative dynamic programming.

## Features

- 37 self-contained problems, each in its own folder with a solution and tests
- Type hints and docstrings on many solutions
- Input validation on the number-theory helpers (raise `TypeError` / `ValueError` on bad input)
- No third-party runtime dependencies; only `pytest` is needed for the pytest-style tests

## Tech Stack

- Python 3
- `unittest` (standard library) and `pytest`

## Problems

### Arrays and Two Pointers

| Problem | Approach | Tests |
| ------- | -------- | ----- |
| [4Sum](4sum/) | Sort + two pointers, skipping duplicates | unittest |
| [Container With Most Water](containerwithmostwater/) | Two pointers | unittest |
| [Remove Element](remove-element/) | In-place overwrite with a write index | unittest |
| [Median of Two Sorted Arrays](median-arrays/) | Merge, sort and pick the middle | unittest |
| [Maximum Subarray Sum](largestnum/) | Brute force over all subarrays | pytest |

### Binary Search

| Problem | Approach | Tests |
| ------- | -------- | ----- |
| [Search Insert Position](searchinsertposition/) | Binary search | unittest |

### Strings

| Problem | Approach | Tests |
| ------- | -------- | ----- |
| [Longest Substring Without Repeating Characters](longestsubstring/) | Sliding window with a set | script |
| [Longest Palindromic Substring](longestpalindromestring/) | Check every substring | script |
| [Valid Parentheses](validparentheses/) | Stack | unittest |
| [Count and Say](countandsay/) | Iterative run-length encoding | unittest |
| [Zigzag Conversion](zigzag/) | Row-by-row simulation | assert script |
| [String to Integer (atoi)](stringtointeger/) | Single pass with sign and 32-bit clamping | script |
| [Palindrome Check](palindrome/) | Two pointers | pytest |
| [Reverse a String](reverse/) | Two-pointer swap | pytest |
| [Count Vowels](countvowels/) | Linear scan | pytest |

### Math and Number Theory

| Problem | Approach | Tests |
| ------- | -------- | ----- |
| [Add Three Numbers](add-num/) | Basic arithmetic | unittest |
| [Armstrong Number](armstrong/) | Sum of digits raised to the digit count | pytest |
| [Factorial](factorial/) | Iterative product | pytest |
| [FizzBuzz](fizzbuzz/) | Modulo checks | pytest |
| [GCD](gcd/) | Euclid's algorithm | pytest |
| [HCF](hcf/) | Euclid's algorithm | unittest |
| [LCM](lcm/) | Via GCD (Euclid) | pytest |
| [Prime Check](isprime/) | Trial division up to the square root | pytest |
| [Prime Factors](prime_factors/) | Trial division | pytest |
| [Perfect Number](perfect_number/) | Sum of proper divisors | pytest |
| [Sum of Digits](sumofdigits/) | Repeated modulo / integer division | pytest |
| [Happy Number](happynumber/) | Cycle detection with a set | unittest |
| [Reverse Integer](reverse-integer/) | Digit reversal with 32-bit overflow check | script |
| [Divide Two Integers](dividetwointegers/) | Bit-shift long division (no `*`, `/`, `%`) | unittest |
| [Integer to Roman](romantointeger/) | Greedy value/symbol table | unittest |

### Dynamic Programming and Sequences

| Problem | Approach | Tests |
| ------- | -------- | ----- |
| [Climbing Stairs](climbingstairs/) | Bottom-up DP with two variables | unittest |
| [Fibonacci](fibonacci/) | Iterative pair update | pytest |
| [Pascal's Triangle](Pascaltriangle/) | Build each row from the previous one | unittest |

### Backtracking

| Problem | Approach | Tests |
| ------- | -------- | ----- |
| [Combination Sum](combinationsum/) | Recursive backtracking with element reuse | unittest |

### Linked Lists and Heaps

| Problem | Approach | Tests |
| ------- | -------- | ----- |
| [Merge k Sorted Lists](mergeksorted/) | Min-heap (`heapq`) | unittest |

### Trees

| Problem | Approach | Tests |
| ------- | -------- | ----- |
| [Same Tree](sametree/) | Recursive comparison | unittest |
| [Symmetric Tree](symmetrictree/) | Recursive mirror check | unittest |

## Project Structure

```
.
├── <problem>/
│   ├── main.py | <problem>.py     # Solution
│   └── testcase.py | test_<problem>.py   # Tests for that solution
└── ...
```

Most interview-style problems use `main.py` + `testcase.py` (unittest or a print script); the number-theory and string helpers use `<problem>.py` + `test_<problem>.py` (pytest).

## Getting Started

### Prerequisites

- Python 3.9+
- `pytest` for the pytest-style tests

```bash
git clone https://github.com/Pankkaj64/python-dsa.git
cd python-dsa
pip install pytest
```

## Usage

Tests import the solution by module name (for example `from main import four_sum`), so run them from inside the problem's folder.

**pytest** (folders with `test_*.py`):

```bash
cd fibonacci
python -m pytest
```

**unittest** (folders with `testcase.py`):

```bash
cd 4sum
python -m unittest testcase
```

`add-num` uses `testcases.py` and `hcf` uses `hcftestcase.py`, so run `python -m unittest testcases` or `python -m unittest hcftestcase` there.

**Script-style tests** (`longestsubstring`, `longestpalindromestring`, `reverse-integer`, `stringtointeger`, `zigzag`) print results or run asserts:

```bash
cd zigzag
python testcase.py
```

Many pytest-style solutions also include a `__main__` demo, for example:

```bash
cd isprime
python isprime.py
```
