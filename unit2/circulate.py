#!/usr/bin/env python3


def circulate(a, b, c):
    """circulate between three variables, three times

    @author kgashok
    @param a is a integer
    @param b is a integer
    @param c is a integer

    @return nothing

    >>> circulate(1, 2, 3)
    2 3 1
    3 1 2
    1 2 3
    """
    i = 3
    while i:
        t = a
        a = b
        b = c
        c = t
        print(a, b, c)
        i -= 1


print("Enter 3 values")
a, b, c = input().split()
print()
circulate(a, b, c)


def circulate_list(alist):
    """circulate 'n' elements in a list, n times

    @author kgashok
    @param alist contains the 'n' elements

    @return nothing
    """
    i = len(alist)
    while i:
        first = alist.pop(0)
        alist.append(first)
        print(*alist, sep=", ")
        i -= 1


alist = input("enter multiple values\n").split()
print()
circulate_list(alist)


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    pass
