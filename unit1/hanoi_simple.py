c = 0


def move_tower(height, fromPole, toPole, withPole):
    '''A recursive function which implements the solution
    to the Hanoi Puzzle
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
    being moved, from the fp pole to the tp pole'''

    global c
    c += 1
    print("Step", c, ": moving Disk", tower[disk], "from", fp, "to", tp)


tower = ['', 'red  ', 'green', 'blue ']
move_tower(3, "Start", "Dest", "Middle")
