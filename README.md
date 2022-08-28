# Building Reasoning Capacity Using Data Structures and Algorithms

These are practice questions on Data Structures and Algorithms. A question and its solution are separated.

- Example of a question filename: `python/create_phone_number.py`
- Example of an answer filename: `python/create_phone_number_solution.py`

### Question

```python
# python/create_phone_number.py

"""
Write a function that accepts an array of 10 integers (between 0 and 9),
that returns a string of those numbers in the form of a a phone number


Example

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

Returns:

(123) 456-7890 or (000) 000-0000

The retuned format MUST abide to the order shown above.
Remember the space after the closing parenthesis
"""


def create_phone_number(n):
    pass

```

### Solution

```python
# python/create_phone_number_solution.py

def create_phone_number(n):
    number_list = [str(x) for x in n]
    str_number_list = ''.join(number_list)
    part1 = str_number_list[0:3]
    part2 = str_number_list[3:6]
    part3 = str_number_list[6:]
    return f'({part1}) {part2}-{part3}'

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

# Output

(123) 456-7890
```