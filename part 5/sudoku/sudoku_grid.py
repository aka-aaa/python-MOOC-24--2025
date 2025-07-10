    """Checks that a given row has no duplicate numbers (1–9), ignoring zeros."""
def row_correct(sudoku: list, row_no: int):
    row_list = []
    for i in sudoku[row_no]:
        if i in row_list and i!= 0:
            return False
        row_list.append(i)
    return True

    """Checks that a given column has no duplicate numbers (1–9), ignoring zeros."""
def column_correct(sudoku: list, column_no: int):
    column_list = []
    for row in sudoku:
        number = row[column_no]
        if number != 0 and number in column_list:
            return False
        column_list.append(number)
    return True 
    
    """Checks that the 3x3 block starting at (row_no, column_no) has no duplicates."""
def block_correct(sudoku: list, row_no: int, column_no: int):
    block_list = []
    for i in range(row_no,row_no+3):
        for j in range(column_no,column_no+3):
            number = sudoku[i][j]
            if number != 0 and number in block_list:
                return False
            block_list.append(number)
    return True

    """Checks if the entire Sudoku grid is valid."""
def sudoku_grid_correct(sudoku: list):
        # Check all rows
    for row_no in range(9):
        if not row_correct(sudoku, row_no):
            return False
        # Check all columns
    for column_no in range(9):
        if not column_correct(sudoku, column_no):
            return False 
        # Check all 3x3 blocks
    for row_points in [0, 3, 6]:
        for column_points in [0, 3, 6]:
            if not block_correct(sudoku, row_points, column_points):
                return False
    
    return True
