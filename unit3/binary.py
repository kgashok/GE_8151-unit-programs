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
        print(f'searching_for: {token}, mid:{midpoint}, midvalue:{midvalue}')

        if midvalue == token:
            return True
        
        if token < midvalue:
            right = midpoint
        else:
            left = midpoint + 1

    return False


# Main Program
num_list = []
n = int(input("Enter the number of elements: "))
for i in range(0, n):
    item = input("Enter the item:")
    num_list.append(item)
search = input("Enter element to search: ")
ans = binary_search(num_list, search)
if ans:
    print("Element {0} Found".format(search))
else:
    print("Element {0} Not Found".format(search))