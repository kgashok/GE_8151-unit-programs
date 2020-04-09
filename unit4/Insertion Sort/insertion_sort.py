def insertionsort(alist):
    '''insertionsort algorithm implemented
    using insort function
    '''
    for i in range(1, len(alist)):
        key = alist[i]
        insort(alist, key, i)
        print("inter", alist)
    return alist


def insort(alist, key, j):
    '''insort inserts 'key' into the
    sorted alist[:j] so that it remains sorted
    'j' is the current index of 'key' in alist
    '''
    while j > 0 and alist[j - 1] > key:
        alist[j] = alist[j - 1]
        j -= 1
    alist[j] = key
