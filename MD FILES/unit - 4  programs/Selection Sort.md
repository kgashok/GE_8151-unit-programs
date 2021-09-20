# Selection Sort

<img src="./img/selectionsort.gif" style="width:400px;" class="center"/>

## Table of Contents

- [Problem Statement](#problem-statement)
- [Python Code](#python-code)
- [Sample Output](#Sample-Output)
- [Replit Link](#replit-link)
- [PythonTutor Link](#pythontutor-link)


## Problem Statement

<div align="justify"> <p> The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array. </div></p>

* The subarray which is already sorted. 
* Remaining subarray which is unsorted.

<div align="justify"> <p>In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray. </div></p>




## Python Code

```python
from random import shuffle
from doctest import testmod


def selectsort(lst):
    '''implements the selection sort
    @param lst unsorted list of numbers
    @returns sorted list of numbers
    >>> selectsort([6, 4, 7, 8, 5, 1, 2, 3])
    inter [1, 4, 7, 8, 5, 6, 2, 3]
    inter [1, 2, 7, 8, 5, 6, 4, 3]
    inter [1, 2, 3, 8, 5, 6, 4, 7]
    inter [1, 2, 3, 4, 5, 6, 8, 7]
    inter [1, 2, 3, 4, 5, 6, 8, 7]
    inter [1, 2, 3, 4, 5, 6, 8, 7]
    inter [1, 2, 3, 4, 5, 6, 7, 8]
    [1, 2, 3, 4, 5, 6, 7, 8]
    '''
    def index_of_minimum(i):
        '''return the index of the minimum value
        in the subarray lst[i:]
        @param i index from where the sublist starts
        @returns the index of the minimum value
        '''
        return lst.index(min(lst[i:]), i)

    def swap(x, y):
        '''swaps list elements at index x and y
        @param x an index value
        @param y an index value
        '''
        if x != y:
            lst[x], lst[y] = lst[y], lst[x]

    # Step 0 iterate from 0 to n-1
    for i in range(0, len(lst) - 1):
        # Step 1 select a minimum
        mdx = index_of_minimum(i)
        # Step 2 swap if required
        swap(i, mdx)
        print("inter", lst)
    return lst


# doctstring testing
testmod(name="selectsort", verbose=True)

# driver program
lst = list(range(1, 9))
shuffle(lst)
print(selectsort(lst))

```

## Sample Output
<img src="./img/OPSelectSort.PNG" style="width:400px;" class="center"/>

## Replit Link
https://tinyurl.com/SelectionSortReplit

## PythonTutor Link

http://tiny.cc/SelectSortVisualize
