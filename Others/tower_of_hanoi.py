#Tower of Hanoi solution (Recursion)
def hanoi(disk, start='Pole 2', end='Pole 1', middle='Pole 3'):
    if disk > 0:
        hanoi(disk - 1, start, middle, end)
        print('Move disk %d from %s to %s' % (disk, start, end)) # Move the N disk
        hanoi(disk - 1, middle, end, start)

hanoi(input('How many disks you wanna play? '))



