# Function to add items of the list
def add(numlst):
    sum = 0
    for i in numlst:
        sum = sum + i
    return sum


# Main Program
number_list = []
n = int(input("Enter the number of items of number_list: "))
print("Enter ", n, " values:")
for i in range(0, n):
    x = int(input(" "))
    number_list.append(x)
print("The sum of elements in the list:", add(number_list))
