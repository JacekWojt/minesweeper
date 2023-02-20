array = [['-', '#', '-', '#', '#', '-'],
         ['-', '#', '-', '-', '-', '#'],
         ['-', '-', '#', '-', '-', '-'],
         ['-', '#', '#', '-', '-', '#'],
         ['-', '#', '#', '-', '-', '#']]
print('Original array:')
for x in range(len(array)):
    print(array[x])
max_rows = len(array)
max_columns = len(array[0])
new_array = [[None] * max_columns for _ in range(max_rows)]
#Calculation of top left corner
def top_left_corner(tlc):
    if tlc[0][0] == "#":
        mineNo = "#"
    else:
        mineNo = 0
        if tlc[0][1] == "#":
            mineNo += 1
        if tlc[1][1] == "#":
            mineNo += 1
        if tlc[1][0] == "#":
            mineNo += 1
    new_array[0][0] = str(mineNo)
#Calculation of top right corner
def top_right_corner(trc):
    if trc[0][max_columns - 1] == "#":
        mineNo = "#"
    else:
        mineNo = 0
        if trc[0][max_columns - 2] == "#":
            mineNo += 1
        if trc[1][max_columns - 2] == "#":
            mineNo += 1
        if trc[1][max_columns - 1] == "#":
            mineNo += 1
    new_array[0][max_columns - 1] = str(mineNo)
#Calculation of bottom left corner
def bottom_left_corner(blc):    
    if blc[max_rows - 1][0] == "#":
        mineNo = "#"
    else:
        mineNo = 0
        if blc[max_rows - 2][0] == "#":
            mineNo += 1
        if blc[max_rows - 2][1] == "#":
            mineNo += 1
        if blc[max_rows - 1][1] == "#":
            mineNo += 1
    new_array[max_rows - 1][0] = str(mineNo)
#Calculation of bottom right corner
def bottom_right_corner(brc):
    if brc[max_rows - 1][max_columns - 1] == "#":
        mineNo = "#"
    else:
        mineNo = 0
        if brc[max_rows - 2][max_columns - 1] == "#":
            mineNo += 1
        if brc[max_rows - 2][max_columns - 2] == "#":
            mineNo += 1
        if brc[max_rows - 1][max_columns - 2] == "#":
            mineNo += 1
    new_array[max_rows - 1][max_columns - 1] = str(mineNo)
#Calculation of top side
def top_side(ts):    
    for x in range(1, max_columns - 1):
        if ts[0][x] == "#":
            mineNo = "#"
        else:
            mineNo = 0
            if ts[0][x - 1] == "#":
                mineNo += 1
            if ts[1][x - 1] == "#":
                mineNo += 1
            if ts[1][x] == "#":
                mineNo += 1
            if ts[1][x + 1] == "#":
                mineNo += 1
            if ts[0][x + 1] == "#":
                mineNo += 1
        new_array[0][x] = str(mineNo)
#Calculation of bottom side
def bottom_side(bs):    
    for x in range(1, max_columns - 1):        
        if bs[max_rows - 1][x] == "#":
            mineNo = "#"
        else:
            mineNo = 0
            if bs[max_rows - 1][x - 1] == "#":
                mineNo += 1
            if bs[max_rows - 2][x - 1] == "#":
                mineNo += 1
            if bs[max_rows - 2][x] == "#":
                mineNo += 1
            if bs[max_rows - 2][x + 1] == "#":
                mineNo += 1
            if bs[max_rows - 1][x + 1] == "#":
                mineNo += 1
        new_array[max_rows - 1][x] = str(mineNo)
#Calculation of left side
def left_side(ls):    
    for x in range(1, max_rows - 1):        
        if ls[x][0] == "#":
            mineNo = "#"
        else:
            mineNo = 0
            if ls[x - 1][0] == "#":
                mineNo += 1
            if ls[x - 1][1] == "#":
                mineNo += 1
            if ls[x][1] == "#":
                mineNo += 1
            if ls[x + 1][1] == "#":
                mineNo += 1
            if ls[x + 1][0] == "#":
                mineNo += 1
        new_array[x][0] = str(mineNo)
#Calculation of right side
def right_side(rs):    
    for x in range(1, max_rows - 1):        
        if rs[x][max_columns - 1] == "#":
            mineNo = "#"
        else:
            mineNo = 0
            if rs[x - 1][max_columns - 1] == "#":
                mineNo += 1
            if rs[x - 1][max_columns - 2] == "#":
                mineNo += 1
            if rs[x][max_columns - 2] == "#":
                mineNo += 1
            if rs[x + 1][max_columns - 2] == "#":
                mineNo += 1
            if rs[x + 1][max_columns - 1] == "#":
                mineNo += 1
        new_array[x][max_columns - 1] = str(mineNo)
#Calculation of insde
def inside(ins):
    for x in range (1, max_rows - 1):   
        for y in range(1, max_columns - 1):
            if ins[x][y] == "#":
                mineNo = "#"
            else:
                mineNo = 0
                if ins[x - 1][y - 1] == "#":
                    mineNo += 1
                if ins[x - 1][y] == "#":
                    mineNo += 1
                if ins[x - 1][y + 1] == "#":
                    mineNo += 1
                if ins[x][y + 1] == "#":
                    mineNo += 1
                if ins[x + 1][y + 1] == "#":
                    mineNo += 1
                if ins[x + 1][y] == "#":
                    mineNo += 1
                if ins[x + 1][y - 1] == "#":
                    mineNo += 1
                if ins[x][y - 1] == "#":
                    mineNo += 1
            new_array[x][y] = str(mineNo)
#Minesweeper takes a grid of # and - and convert it.
def minesweeper(array_list):
    top_left_corner(array_list)
    top_right_corner(array_list)
    bottom_left_corner(array_list)
    bottom_right_corner(array_list)
    top_side(array_list)
    bottom_side(array_list)
    left_side(array_list)
    right_side(array_list)
    inside(array_list)
    print('Converted array: ')
    for x in range(len(new_array)):
        print(new_array[x])

minesweeper(array)
