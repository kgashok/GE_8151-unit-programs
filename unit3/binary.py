# Binary search function
def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if(item < alist[midpoint]):
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


# Main Program
num_list = []
n = int(input("Enter the number of elements"))
for i in range(0, n):
    item = input("Enter the item:")
    num_list.append(item)
search = input("Enter element to search: ")
ans = binarySearch(num_list, search)
if(ans):
    print("Element Found")
else:
    print("Element not Found")
