board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

def display_board(b):
    """
    prints out board in properly formatted string
    we want seperation for each 3x3 square in board
    results in 9 seperated squares
    """

    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print(" - - - - - - - - - - - - - -")
        for j in range(len(b[0])):
            if j%3 == 0:
                print(" | ", end="")

            if j == 8:
                print(b[i][j], end = "")
                print(" |", end="\n")
            else:
                print(str(b[i][j]) + " ", end = "")

def emptySpot(b):
    """
    finds next empty spot in board
    iterates through whole board
    """
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i, j)
            
    return None

def checkNum(b, row, col, num):
    """
    checks if integer is valid in a certain spot
    according to sudoku rules
    """


    for i in range(0, len(b)):
            if num == b[i][col] and col != i:
                return False
   
    for i in range(0, len(b)):
            if num == b[row][i]:
                return False 

    #checking if value is repeated in box
    startRow = row // 3
    startCol = col // 3

    endRow = startRow * 3 + 3
    endCol = startCol * 3 + 3

    for i in range(startRow * 3, endRow):
         for j in range(startCol * 3, endCol):
              if num == b[i][j]:
                return False

    return True

def solve(b):
    """
    solves board using other functions
    """
    if emptySpot(b):
        row,col = emptySpot(b)
    else:
        return True
    
    for i in range(1,10):
        if checkNum(b, row, col, i):
            b[row][col] = i
    
            if solve(b):
                return True
            
            b[row][col] = 0
            
        
    return False

solve(board)


    


