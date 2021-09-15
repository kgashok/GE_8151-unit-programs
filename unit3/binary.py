# Binary search function
def binary_search(alist, token):
    '''implements the binary search algorithm to search for 
    'token' in the 'alist'

    @author kgashok
    @param alist is a list of numbers
    @param token is an integer

    @return True if found else False 

    '''
    left = 0
    right = len(alist)
    print()
    while left < right:
        midpoint = (left + right) // 2
        midvalue = alist[midpoint]
        print(f'search for: {token} at mid:{midpoint}, midvalue: {midvalue}')

        if midvalue == token:
            return True

        if token < midvalue:
            right = midpoint
        else:
            left = midpoint + 1

    return False


# Main Program
import random
num_list = []
n = int(input("Enter the number of elements: "))
if n == 0: 
    num_list = sorted([random.randint(1, 100) for _ in range (10)])
    num_list.sort()
    print(num_list)
else:
    for i in range(0, n):
        item = input("Enter the item:")
        num_list.append(int(item))

search = int(input("Enter element to search: "))
ans = binary_search(num_list, search)
if ans:
    print("Element {0} Found".format(search))
else:
    print("Element {0} Not Found".format(search))
