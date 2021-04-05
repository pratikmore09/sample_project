board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# " Backtracking Algorithm " here.....
def solve(bo):
    #print(bo)
    find = find_empty(bo)
    if not find:
         return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False

# 3rd function valid(bo, num, pos) :
# find valid number has given to the board or not
# need to check 3 things entire row, entire col and square itself
#        |  <-- this entire coloumn
#        |
#--------6------------  <-- this entire row
#        |
#        |
# and square value now it is 6 so
# we have to check if 6 is already present
# in current row or coloumn!
def valid(bo, num, pos):
     # check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    #check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True




#1st function [ print_board(bo) ]to print board to better visualization:
def print_board(bo):

    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(bo[i][j])
                else:
                    print(str(bo[i][j]) + " ", end="")


print("***********BEFORE SOLVING SUDOKU *****************")
print()
print_board(board)

# 1st function :  find_empty() which will loop through the board and if it finds empty positions
# or space then it will return that position
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # return row and col



    return None


solve(board)
print()
print("*********** Result after solving sudoku *****************")
print("changes has been done and check webhook process.....")
print_board(board)