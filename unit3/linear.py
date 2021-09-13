# Linear Search function
def linearsearch(num_list, search):
    ''' In this type of search, a sequential search is made over
    all items one by one. Every item is checked and if a
    match is found then that particular item is returned, 
    otherwise the search continues till the end of the 
    data collection.
    
    @author KAMALATHANGARAJAN
    '''
    found = False
    for i in num_list:
        if search == i:
            found = True
            print("Element found")
            break
    if not found:
        print("Element not found")


# Main Program
num_list = []
n = int(input("Enter number of items of num_list: "))
print("Enter ", n, "values:")
for i in range(0, n):
    item = int(input(" "))
    num_list.append(item)
search = int(input("Element to be searched: "))
linearsearch(num_list, search)
