# Minimum Number In a List
## Table of Contents
- [Problem Statement](#problem-statement)
- [Python Code](#python-code)
- [Sample Output](#Sample-Output)
- [Replit Link](#replit-link)
- [PythonTutor Link](#pythontutor-link)

# Problem Statement

<div align="justify"> The problem is to find the minimum element in the given list of elements. Finding minimum in a list of elements can be achieved in different ways. One way is to sort the list of elements in ascending order and get the first element as minimum. Another method is to compare each element with other. As an initial step, first element of the list is considered as minimum element. And in each iteration, each element in the list is compared with the minimum. If the element in the list is less than the minimum then swap both elements else compare with the next element in the list. These steps are continued until the end of the list and finally print the
minimum </div>

---

## Python Code
~~~python
#find minimum of two numbers
# a and b are parameters''


def find_min(a, b):
    if a < b:
        return a
    return b


print("Enter two values :")
a = int(input())
b = int(input())
print("Minimum number is ", find_min(a, b))
~~~

~~~python
#find minimum of three numbers

def find_min(a, b):
    if a < b:
        return a
    return b

# a, b and c are parameters
def min_of_three(a, b, c):
    minVal = find_min(a, b)
    if c < minVal:
        return c
    return minVal


print("Enter three numbers: ")
a = int(input())
b = int(input())
c = int(input())

print("Minimum number is ", min_of_three(a, b, c))
~~~


~~~python
# find minimum of a list
def min_of_list(aList):
    if not aList:
        return None
    minVal = aList[0]
    for number in aList[1:]:
        if number < minVal:
            minVal = number
    return minVal


myList = []
limit = int(input("Enter the limit: "))
print("Enter the elements:\n")
for i in range(limit):
    element = int(input())
    myList.append(element)

print("Minimum of list is ", min_of_list(myList))
~~~

## Sample Output
<img src="./img/OPMinNumber.JPG" style="width:400px;"/>

## Replit Link
https://cutt.ly/MinimumNumberInAList

<img src="./img/MinNumRepl.png" style="width:100px;"/>


## PythonTutor Link

https://cutt.ly/MinimumNumberInAListVisualize

<img src="./img/MinNumInAListVisual.png" style="width:100px;"/>
