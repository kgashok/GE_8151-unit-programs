#!/usr/bin/env python3

print("Enter two values to swap")
a = int(input())
b = int(input())

# using a temporary variable
t = a
a = b
b = t

print("Value of a is {a} and\nValue of b is {b}".format(a=a, b=b))

def swap():
    global a, b
    print("Swap function called")
    a, b = b, a
    
swap()  # go back to their original values
print("Value of a is {a} and\nValue of b is {b}".format(a=a, b=b))


