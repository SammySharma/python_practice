# recursion Addition
# parameterize
def recursion_add(i: int, sum: int) -> int:
    if i < 1:
        print(sum)
        return
    recursion_add(i - 1, sum + i)


recursion_add(20, 0)

print("------------------------------------------")
# function where it return the values


def add(n: int) -> int:
    if n == 1:
        return 1
    return n + add(n - 1)


print(add(5))

# -------------------------------------------------------------------------------------------#
"""Factorial Example using both
1. Parameterize
"""
print("------------------------------------------")


def factor(i: int, factorial: int) -> None:
    if i < 1:
        print(factorial)
        return
    factor(i - 1, factorial * i)


factor(5, 1)
print("------------------------------------------")


def factor2(i):
    if i == 1 or i == 0:
        return 1
    return i * factor2(i - 1)


print(factor2(5))

print("------------------------------------------")


def power(b: int, p: int) -> int:
    if type(p) != int or p < 0:
        raise Exception("Invalid Values!")

    if p == 0:
        return 1
    elif p == 1:
        return b
    return power(b, p - 1) * b


print(power(5, 3))
print(power(5, 1))

print("------------------------------------------")


def ispalindrome(s: str, i) -> None:
    if i >= len(s) // 2:
        return True
    if s[i] != s[len(s) - i - 1]:
        return False
    return ispalindrome(s, i + 1)


print(ispalindrome("aer", 0))

print("------------------------------------------")


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(7))

for i in range(7):
    print(fib(i))
