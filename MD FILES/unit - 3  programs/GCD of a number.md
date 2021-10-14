# Finding GCD of a Number
<img src="./img/GCD.jpg" style="width:400px;" class="center"/>

## Table of Contents
- [Problem Statement](#problem-statement)
- [Python Code](#python-code)
- [Sample Output](#Sample-Output)
- [Replit Link](#replit-link)
- [PythonTutor Link](#pythontutor-link)

## Problem Statement
<div align="justify"> <p> The GCD is a mathematical term for the Greatest Common Divisor of two or more numbers. It is the Greatest common divisor that completely divides two or more numbers without leaving any remainder. Therefore, it is also known as the Highest Common Factor (HCF) of two numbers. For example, the GCD of two numbers, 20 and 28, is 4 because both 20 and 28 are completely divisible by 1, 2, 4 (the remainder is 0), and the largest positive number among the factors 1, 2, and 4 is 4. Similarly, the GCD of two numbers, 24 and 60, is 12. </div></p>



## Python Code
```python
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

```
## Sample Output
<img src="./img/OPGCD.JPG" style="width:400px;" class="center"/>

## Replit Link
https://tinyurl.com/GCDReplit

## PythonTutor Link

https://tinyurl.com/GCDVisualize

