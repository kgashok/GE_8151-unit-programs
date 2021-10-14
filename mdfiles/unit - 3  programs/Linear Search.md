# Linear Search
<img src="./img/linearsearch.gif" style="width:400px;" class="center"/>

## Table of Contents

- [Problem Statement](#problem-statement)
- [Python Code](#python-code)
- [Sample Output](#Sample-Output)
- [Replit Link](#replit-link)
- [PythonTutor Link](#pythontutor-link)


## Problem Statement

<div align="justify"> <p> A linear search or sequential search is a method for finding an element within a list. It sequentially checks each element of the list until a match is found or the whole list has been searched. A linear search runs in at worst linear time and makes at most n comparisons, where n is the length of the list. If each element is equally likely to be searched, then linear search has an average case of 
n+1/2 comparisons, but the average case can be affected if the search probabilities for each element vary.  </div></p>




## Python Code

```python
# Linear Search function
def linearsearch(num_list, search):
    found = False
    for i in num_list:
        if search == i:
            found = True
            print("Element found")
            break
    if not found:
        print("Element not found")


# Main Program
num_list = []
n = int(input("Enter number of items of num_list: "))
print("Enter ", n, "values:")
for i in range(0, n):
    item = int(input(" "))
    num_list.append(item)
search = int(input("Element to be searched: "))
linearsearch(num_list, search)

```
## Sample Output
<img src="./img/OPLinearSearch.JPG" style="width:400px;" class="center"/>

## Replit Link
https://tinyurl.com/LinearSearchKiTE

## PythonTutor Link

https://tinyurl.com/LinearSearchVisualize


