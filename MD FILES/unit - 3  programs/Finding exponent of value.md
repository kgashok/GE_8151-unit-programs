# Exponent of a value
<img src="./img/ExponentOfNumber.gif" style="width:400px;" class="center"/>


## Table of Contents

- [Problem Statement](#problem-statement)
- [Python Code](#python-code)
- [Sample Output](#Sample-Output)
- [Replit Link](#replit-link)
- [PythonTutor Link](#pythontutor-link)


## Problem Statement
**<div align="justify"> <p> When you multiply a by itself, it's easy to write it down as a × a. However, when you have to multiply a by itself, let's say, forty five times, you need to write a very long line, which is inconvenient. You can use a shorter notation instead, called exponent (power).**</div></p>

- <div align="justify"> <p> Remember that exponent can be used only when multiplying a number or a variable by itself. Then, instead of writing your number 45 times in a row, you can simply write a<sup>45</sup></div></p>

- <div align="justify"> <p> The superscript, in this case 45, indicates the number of multipliers in the function, and it's called an exponent, and a is called a base. </div></p>




## Python Code

```python
# importing math module for pow()
import math
b = int(input("Enter a base value: "))
e = int(input("Enter an exponent value: "))
if(e == 1):
    print("Exponentiation of", b, "to the power", e, "is=", b)
else:
    print("Exponentiation of", b, "to the power", e, "is=", math.pow(b, e))

```

## Sample Output
<img src="./img/OPExponentOfAValue.JPG" style="width:400px;" class="center"/>

## Replit Link
https://tinyurl.com/ExponentOfANumber

## PythonTutor Link

https://tinyurl.com/KiTEExpValueVisualize

