# GCD function
def gcd(x, y):
    rem = x % y
    if(rem == 0):
        return y
    else:
        return gcd(y, rem)


# Main program
n1 = int(input("Enter number1:"))
n2 = int(input("Enter number2:"))
print("Greatest Common Divisor of ", n1, "and", n2, "=", gcd(n1, n2))
