# Game Board Winner Checker

This Python function determines which player has more markers on a 2D game board.

## Function

**who_won(game_board)**

- Takes a 2D list where:
    - `0` = empty square
    - `1` = marker from Player 1
    - `2` = marker from Player 2

- Returns:
    - `1` if Player 1 has more markers
    - `2` if Player 2 has more markers
    - `0` if it's a tie

## Example

```python
game_board = [
    [1, 2, 1],
    [0, 1, 2],
    [2, 0, 0]
]

print(who_won(game_board))  # Output: 1
