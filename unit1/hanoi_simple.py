#global variable to count number of steps
c = 0
tower = ['', 'red  ', 'green', 'blue ']

def move_tower(height, fromPole, toPole, withPole, init=0):
    '''A recursive function which implements the solution
    to the Hanoi Puzzle

    @author kgashok
    @param height is a integer 
    @param fromPole is a string 
    @param toPole is a string 
    @param withPole is a string

    @return nothing

    >>> move_tower(3, 'Start', 'Dest', 'Middle')
    Step 1 : moving Disk red   from Start to Dest
    Step 2 : moving Disk green from Start to Middle
    Step 3 : moving Disk red   from Dest to Middle
    Step 4 : moving Disk blue  from Start to Dest
    Step 5 : moving Disk red   from Middle to Start
    Step 6 : moving Disk green from Middle to Dest
    Step 7 : moving Disk red   from Start to Dest

    '''

    # Terminal case
    if height == 1:
        move_disk(height, fromPole, toPole)
    else:
        move_tower(height - 1, fromPole, withPole, toPole)
        move_disk(height, fromPole, toPole)
        move_tower(height - 1, withPole, toPole, fromPole)


def move_disk(disk, fp, tp):
    '''move_disk does the equivalent of a move 
    by printing the disk (named in the tower list)
    being moved, from the fp pole to the tp pole
    
    @author kgashok
    @param disk is a integer 
    @param fp is a string 
    @param tp is a string 
 
    @return nothing'''

    global c
    c += 1
    print("Step", c, ": moving Disk", tower[disk], "from", fp, "to", tp)


move_tower(3, "Start", "Dest", "Middle")

if __name__ == "__main__":
    c = 0 # hack, needs to be fixed
    import doctest
    doctest.testmod()