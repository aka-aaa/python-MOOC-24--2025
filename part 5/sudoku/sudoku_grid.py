def row_correct(sudoku: list, row_no: int):
    row_list = []
    for i in sudoku[row_no]:
        if i in row_list and i!= 0:
            return False
        row_list.append(i)
    return True


def column_correct(sudoku: list, column_no: int):
    column_list = []
    for row in sudoku:
        number = row[column_no]
        if number != 0 and number in column_list:
            return False
        column_list.append(number)
    return True 

def block_correct(sudoku: list, row_no: int, column_no: int):
    block_list = []
    for i in range(row_no,row_no+3):
        for j in range(column_no,column_no+3):
            number = sudoku[i][j]
            if number != 0 and number in block_list:
                return False
            block_list.append(number)
    return True

def sudoku_grid_correct(sudoku: list):
    for row_no in range(9):
        if not row_correct(sudoku, row_no):
            return False
    for column_no in range(9):
        if not column_correct(sudoku, column_no):
            return False 
    for row_points in [0, 3, 6]:
        for column_points in [0, 3, 6]:
            if not block_correct(sudoku, row_points, column_points):
                return False
    
    return True
