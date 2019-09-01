width = int(input('Width? '))
height = int(input('Height? '))
array1 = []
array2 = []
user_text = ''
living_cells = 0

array2 = []
for x in range(height):
    array2.append([])
    for y in range(width):
        array2[x].append(0)

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
    print('--------------------')
    input()


while 1:
    clear_screen()
    print_array(array1)
    for x in range(height):
        for y in range(width):
            # top left
            if x != 0 and y != 0:
                if array1[x - 1][y - 1] == 1:
                    living_cells += 1
            # top
            if x != 0:
                if array1[x - 1][y] == 1:
                    living_cells += 1
            # top right
            if x != 0 and y != width - 1:
                if array1[x - 1][y + 1] == 1:
                    living_cells += 1
            # right
            if y != width - 1:
                if array1[x][y + 1] == 1:
                    living_cells += 1
            # bottom right
            if x != height - 1 and y != width - 1:
                if array1[x + 1][y + 1] == 1:
                    living_cells += 1
            # bottom
            if x != height - 1:
                if array1[x + 1][y] == 1:
                    living_cells += 1
            # bottom left
            if x != height - 1 and y != 0:
                if array1[x + 1][y - 1] == 1:
                    living_cells += 1
            # left
            if y != 0:
                if array1[x][y - 1] == 1:
                    living_cells += 1
            if array1[x][y] == 1:
                if living_cells == 2 or living_cells == 3:
                    array2[x][y] = 1
                else:
                    array2[x][y] = 0
            else:
                if living_cells == 3:
                    array2[x][y] = 1
                else:
                    array2[x][y] = 0
            living_cells = 0
    for i in range(height):
        for j in range(width):
            array1[i][j] = array2[i][j]


