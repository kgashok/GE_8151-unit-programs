# Merge Sort

<img src="./img/mergesort.gif" style="width:400px;" class="center"/>

## Table of Contents

- [Problem Statement](#problem-statement)
- [Python Code](#python-code)
- [Sample Output](#Sample-Output)
- [Replit Link](#replit-link)
- [PythonTutor Link](#pythontutor-link)


## Problem Statement

<div align="justify"> <p> Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one. See the following C implementation for details.  </div></p>

<img src="./img/mergesortsteps.png" style="width:400px;" class="center"/>

```
MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:  
             middle m = l+ (r-l)/2
     2. Call mergeSort for first half:   
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)
```



## Python Code

```python
def merge(A, B):
    C = []
    while A and B:
        candidate = (A if A[0] < B[0] else B).pop(0)
        C.append(candidate)

    # pick up the residual elements in A or B
    return C + A + B


def mergesort(ulist):
    if len(ulist) <= 1:
        return ulist

    mid = len(ulist) // 2

    leftA = ulist[:mid]
    rightB = ulist[mid:]

    sortedA = mergesort(leftA)
    sortedB = mergesort(rightB)

    slist = merge(sortedA, sortedB)
    return slist

alist = [6, 2, 1, 5, 8, 7, 4, 3]
print("Unsorted: ",alist)
print("Sorted: ",mergesort(alist))
```

## Sample Output
<img src="./img/OPMergeSort.PNG" style="width:400px;" class="center"/>

## Replit Link
https://tinyurl.com/MergeSortReplit

## PythonTutor Link

http://tiny.cc/MergeSortVisualize