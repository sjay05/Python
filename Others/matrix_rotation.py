array = [
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4]
]

list_of_spirals = []
def spiral(array, row, column,):
    record1 = row
    record2 = column
    if len(list_of_spirals) == len(array)*len(array[0]):
        return list_of_spirals

    # temp = 0
    # if row == 0:
    #     temp = len(array)
    # else:
    #     temp = len(array) - (2*row)

    while column < len(array[row])-(2*row):
        if column == len(array[row]):
            break
        else:
            list_of_spirals.append(array[row][column])
            column += 1

    column -= 1

    while row < len(array)-(2*row):
        list_of_spirals.append(array[row][column])
        row += 1

    row -= 1

    while column > 0:
        if column == row:
            column -= 1
        else:
            list_of_spirals.append(array[row][column])
            column -= 1

    while row > 0:
        list_of_spirals.append(array[row][column])
        row -= 1

    spiral(array, row+1, column+1)

spiral(array, 0, 0)