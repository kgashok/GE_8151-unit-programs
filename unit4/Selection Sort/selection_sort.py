def selectionsort(alist):
    n = len(alist)
    for i in range(n - 1):
        unsorted = alist[i:]
        smallest = min(unsorted)
        min_i = alist.index(smallest, i)
        alist[i], alist[min_i] = alist[min_i], alist[i]
        print("intermediary", alist)
    return alist


# Improved Version of Selection Sort
def selectsort(alist):
    n = len(alist)
    for i in range(n - 1):
        unsorted = alist[i:]
        (minval, min_i) = min((v, i)
                              for i, v in enumerate(unsorted))
        alist[i], alist[min_i + i] = alist[min_i + i], alist[i]
        print("intermediary", alist)
    return alist
