# Type hints in Python

#%%
# Basic type hints for variables, function parameters, and return values
age: int = 25

def greet(name: str) -> str:
    return f"Hello, {name}!"

print(age)
print(greet("Alice"))

#%%
# The -> syntax specifies the expected return type
def add_numbers(x: int, y: int) -> int:
    return x + y

print(add_numbers(3, 5))

#%%
# Optional allows None; List and Tuple describe collection contents
from typing import Optional, List, Tuple

def get_user(id: int) -> Optional[str]:
    return None if id == 0 else "User"

def sum_numbers(numbers: List[int]) -> int:
    return sum(numbers)

def get_name_and_age() -> Tuple[str, int]:
    return ("Abc", 25)

print(get_user(1))
print(sum_numbers([1, 2, 3]))
print(get_name_and_age())

#%%
# Without type hints, invalid argument types may only fail at runtime
def factorial_no_hints(i):
    if i < 0:
        return None
    if i == 0:
        return 1
    return i * factorial_no_hints(i - 1)

print(factorial_no_hints(4))

#%%
# These calls cause runtime errors:
print(factorial_no_hints("4"))
#%%
print(factorial_no_hints(5.01))

#%%
# Type hints document expected types, but Python does not enforce them automatically
def factorial(i: int) -> Optional[int]:
    if not isinstance(i, int):
        return None
    if i < 0:
        return None
    if i == 0:
        return 1
    return i * factorial(i - 1)

print(factorial(5))
print(factorial(5.01))  # Returns None because of the explicit isinstance check

#%%
# Type hints alone do not prevent incorrect calls at runtime
def multiply(x: int, y: int) -> int:
    return x * y

print(multiply(3, 4))
print(multiply("3", 4))  # Runs in Python despite violating the type hint

#%%
# Use mypy for static type checking
# Install in a terminal:
# pip install mypy
#
# Then check this file without executing it:
# mypy type_hints.py
#
# A type checker can flag calls such as:
# multiply("3", 4)
