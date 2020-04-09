# a helper function for the mergesort function
# function to merge already sorted lists


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
