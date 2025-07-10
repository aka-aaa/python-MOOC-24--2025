# Sudoku Grid Validator 🧩

This Python script checks whether a given 9x9 Sudoku grid is valid.  
It ensures that each row, column, and 3x3 block contains unique numbers from 1 to 9 (zeros are ignored).

## Features

- `row_correct`: Validates a single row
- `column_correct`: Validates a single column
- `block_correct`: Validates a 3x3 subgrid
- `sudoku_grid_correct`: Validates the entire grid

## Example Sudoku Grid Input

```python
sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
