#importing math module for pow()
import math
b=int(input("Enter a base value: "))
e=int(input("Enter an exponent value: "))
if(e==1):
    print ("Exponentiation of",b,"to the power",e,"is=",b)
else:
    print("Exponentiation of",b,"to the power",e,"is=",math.pow(b,e))