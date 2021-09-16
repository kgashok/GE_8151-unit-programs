# Binary search function
import random


def bsearch_slice(alist, token):
    '''binary search using the intuitive slice operator
    @author kgashok
    @param alist is a list of numbers
    @param token is an integer

    @return True if found else False 

    '''
    while alist:
        print(f'{alist}', end=":: ")
        midpoint = len(alist) // 2
        midvalue = alist[midpoint]
        
        print(f'search for: {token} at mid:{midpoint}, midvalue: {midvalue}')

        if token == midvalue:
            return True

        alist = alist[:midpoint] if token < midvalue else \
            alist[midpoint+1:]

    return False


def binary_search(alist, token):
    '''implements the binary search algorithm to search for 
    an integer in a list of numbers

    @author kgashok
    @param alist is a list of numbers
    @param token is an integer

    @return index or -1 if not found 

    '''
    left = 0
    right = len(alist)
    print("alist: {0}, search for {1}".format(alist, token))

    while left < right:
        midpoint = (left + right) // 2
        midvalue = alist[midpoint]

        # print(f'search for: {token} at mid:{midpoint}, midvalue: {midvalue}')
        if midvalue == token:
            return midpoint

        if token < midvalue:
            right = midpoint
        else:
            left = midpoint + 1

    return -1


# Main Program
num_list = []
n = int(input("Enter the number of elements: "))
if n == 0:
    num_list = sorted([random.randint(1, 100) for _ in range(10)])
    num_list.sort()
    print(num_list)
else:
    for i in range(0, n):
        item = input("Enter the item:")
        num_list.append(int(item))

search = int(input("Enter element to search: "))
print("****Binary Search using Slice")
ans = bsearch_slice(num_list, search)
if ans:
    print("Element {0} Found".format(search))
else:
    print("Element {0} not found!".format(search))

print("****Binary Search using indexes")
ans = binary_search(num_list, search)
if ans != -1:
    print("Element {0} Found at index {1}".format(search, ans))
else:
    print("Element {0} not found!".format(search))
