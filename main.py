width = int(input('Width? '))
height = int(input('Height? '))
array1 = []
array2 = []
user_text = ''
cells = 0

for x in range(height):
    array1.append([])
    user_text = input('line ' + str(x+1) + ': ').upper()
    for y in range(width):
        if user_text[y] == 'O':
            array1[x].append(1)
        else:
            array1[x].append(0)
print(array1)


def print_array(array):
    for x in range(height):
        print_line = ''
        for y in range(width):
            if array[x][y] == 0:
                print_line += '   '
            else:
                print_line += '[ ]'
        print(print_line)


def clear_screen():
    for x in range(10):
        print('')


while 1:
    for x in range(height):
        for y in range(width):
            if array1[x-1][y-1] == 0:
                if x == 1:
                    if y == 1:
                        #right
                        if array1[x - 1][y] == 1:
                            cells += 1
                        #right down
                        if array1[x][y] == 1:
                            cells += 1
                        #down
                        if array1[x][y - 1] == 1:
                            cells += 1
                        if cells == 3:
                            array2[x-1][y-1] = 1
                        cells = 0
                    elif y == width:
                        #left
                        if array1[x - 1][y - 2] == 1:
                            cells += 1
                        #left down
                        if array1[x][y - 2] == 1:
                            cells += 1
                        # down
                        if array1[x][y - 1] == 1:
                            cells += 1
                        if cells == 3:
                            array2[x-1][y-1] = 1
                        cells = 0
                    else:
                        # right
                        if array1[x - 1][y] == 1:
                            cells += 1
                        # right down
                        if array1[x][y] == 1:
                            cells += 1
                        # down
                        if array1[x][y - 1] == 1:
                            cells += 1
                        # left down
                        if array1[x][y - 2] == 1:
                            cells += 1
                        # left
                        if array1[x - 1][y - 2] == 1:
                            cells += 1
                        if cells == 3:
                            array2[x - 1][y - 2] = 1
                        cells = 0
                elif x == height:
                    if y == 1:
                        #up
                        if array1[x - 2][y - 1] == 1:
                            cells += 1
                        #up right
                        if array1[x - 2][y] == 1:
                            cells += 1
                        #right
                        if array1



            else


print_array(array1)

