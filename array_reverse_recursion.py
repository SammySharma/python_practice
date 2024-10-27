# reverse_array_using_recursion
"""
list L=[3,4,5,7,11,21,128,82,2,5]
"""


def reverse_array(l: list, start, end) -> list:
    if start >= end:
        return
    l[start], l[end] = l[end], l[start]
    reverse_array(l, start + 1, end - 1)


my_list = [3, 4, 5, 7, 11, 21, 128, 82, 2, 5]
print(my_list)
reverse_array(my_list, 0, len(my_list) - 1)
print(my_list)
