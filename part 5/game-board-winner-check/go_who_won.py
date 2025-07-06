def who_won(game_board: list):     
    """
    Determines which player has more markers on the game board.

    Args:
        game_board (list): 2D list representing the board. 
                           Cells contain 0 (empty), 1 (player 1), or 2 (player 2).

    Returns:
        int: 1 if player 1 has more markers,
             2 if player 2 has more markers,
             0 if both have the same number of markers.
    """
    player_1 = 0
    player_2 = 0
    equal = 0
    for i in range (len(game_board)):
        for j in range (len(game_board[i])):
            if game_board[i][j] == 1:
                player_1 += 1
            elif game_board[i][j] == 2:
                player_2 +=1
    if player_1 > player_2:
        return 1
    elif player_2 > player_1:
        return 2
    elif player_1 == player_2:
        return 0
    

