
# find minimum of two numbers
# a and b are parameters''


def find_min(a, b):
    if a < b:
        return a
    return b


print("Enter two values :")
a = int(input())
b = int(input())
print("Minimum number is ", find_min(a, b))


# find minimum of three numbers
# a, b and c are parameters
def min_of_three(a, b, c):
    minVal = find_min(a, b)
    if c < minVal:
        return c
    return minVal


print("Enter three numbers: ")
a = int(input())
b = int(input())
c = int(input())

print("Minimum number is ", min_of_three(a, b, c))


# find minimum of a list
def min_of_list(aList):
    if not aList:
        return None
    elif len(aList) == 1:
        return aList[0]
    else:
        minVal = aList[0]
        for number in aList[1:]:
            if number < minVal:
                minVal = number
        return minVal


myList = []
limit = int(input("Enter the limit: "))
print("Enter the elements:\n")
for i in range(limit):
    element = int(input())
    myList.append(element)

print("Minimum of list is ", min_of_list(myList))
