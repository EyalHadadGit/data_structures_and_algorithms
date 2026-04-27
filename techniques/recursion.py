# 1. divide & conquer recursion
def factorial(num: int) -> int:
    if num < 0:
        raise ValueError("Negative input not allowed")
    if num == 0:
        return 1
    return num * factorial(num - 1)

# 2. euclid recursion
def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)

# 3. string recursion
def reverse(string: str, index: int = 0) -> str:
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    if len(string) == 0:
        return ""
    if len(string) - 1 == index:
        return string[index]
    return reverse(string, index + 1) + string[index]

# 4. structure recursion
def flatten(arr: list) -> list:
    if not isinstance(arr, list):
        return [arr]
    if len(arr) == 0:
        return []
    if isinstance(arr[0], list):
        return flatten(arr[0]) + flatten(arr[1:])
    return [arr[0]] + flatten(arr[1:])

# 5. tree-style recursion pattern (fixed even-sum logic)
def nested_even_sum(d):
    if isinstance(d, dict):
        return sum(nested_even_sum(v) for v in d.values())
    if isinstance(d, int):
        return d if d % 2 == 0 else 0
    return 0