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
print(power(5, 0))
print(power(5, 2.5))
