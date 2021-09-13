# Tower of Hanoi

# one disk is tower A, destination is tower B, intermediate is tower C
print("Tower of Hanoi - with one disk")
source = 'A'
destination = 'B'
print("Move top disk from ", source, " to ", destination)
print()

# Two disk is at tower A, destination is tower B, intermediate in tower C
print("Tower of Hanoi - with 2 disk")
source = 'A'
destination = 'B'
temp = 'C'
print("Move top disk from ", source, " to ", temp)
print("Move top disk from ", source, " to ", destination)
print("Move top disk from ", temp, " to ", destination)
print()


# In a recursive way

def tower_of_hanoi(n, fromTower, toTower, tempTower):
    '''
    @author sdnandhu
    '''
    if n == 1:
        print("Move top disc from ", fromTower, " to ", toTower)
    else:
        # Move n-1 disks from source to temp
        tower_of_hanoi(n - 1, fromTower, tempTower, toTower)
        # Move top disk from source to destination
        print("Move top disc from ", fromTower, " to ", toTower)
        # Move n-1 disks from temp to the destination
        tower_of_hanoi(n - 1, tempTower, toTower, fromTower)


n = int(input("Enter number of disks:"))
tower_of_hanoi(n, 'A', 'B', 'C')
