# Args_Kwargs(function/method)

print("-----------------Example 1-------------------")


def args(name, *args):
    print(name)
    print(args)


args("Hello", 10, 20, 30, 40, 50, 60)


print("-----------------Example 2-------------------")


# example 2
def add(*args):
    total = 0
    for num in args:
        total += num
    print("Total", total)


add(10, 20, 30, 40, 50, 60)

print("-----------------Example 3-------------------")


def add(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")


add(10, 20, 30, 40, 50, 60, name="Hello", age=20)
