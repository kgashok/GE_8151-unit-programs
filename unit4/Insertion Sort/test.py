from random import shuffle
alist = list(range(11, 19))
shuffle(alist)
print("Unsorted", alist)
print("Sorted", insertionsort(alist))
