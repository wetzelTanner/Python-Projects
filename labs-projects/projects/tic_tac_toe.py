####################################################################
# Author: Tanner Wetzel
# Date Finished: 11/12/2021
# Description: A program that will display a tic tac toe board and 
#              allows a user to play based on positional input
####################################################################

def create_board():
    '''
    This function creates an empty game board represented
    in a nested list for the Tic Tac Toe game.

    Args: None. This function takes no input.

    Return:
        A 3*3 nested list (2D) that contains all spaces ' '
    '''
    board = [[' ',' ',' '],
             [' ',' ',' '],
             [' ',' ',' ']]
    return board


def display_board(board_mat):
    '''
    This function takes a nested list that represents the current
    game board and displays the contents from the board.

    Args:
        board_mat: a nested list (2D) that contains 'X's, 'O's or
                   spaces ' 's.

    Return: None (it just prints). 
    '''
    print('   0 1 2')  # The column indices of the board
    print('  ------')  # The horizontal line
    
    for i in range(len(board_mat)):
        print(str(i) + '|', end = ' ')
        for j in range(len(board_mat[0])): 
            print(board_mat[i][j], end = ' ')
        print()


def play_a_turn(board_mat, player_token):
    '''
    This function prompts a player for entering a position, then
    checks if the position is available. If not, prints an error
    message and re-prompt; if yes, place the player's token (either
    'X' or 'O') at the designated position on the board.

    In this program, you can assume "placing a token at an occupied
    place" is the ONLY possible input error the program users will
    make.
   
    Args:
        board_mat: the nested list for the current game board.
        player_token: the string that represents a player, 'X' or 'O'

    Return:
        None. All the changes can be made to the argument board_mat,
        so no need to return anything.
    '''
    move = input(player_token + " enter a position: ")
    move_lst = move.split()
    move_lst[0] = int(move_lst[0])
    move_lst[1] = int(move_lst[1])
    while board_mat[move_lst[0]][move_lst[1]] not in ' ':
        print('Error: place already taken!')
        move = input(player_token + " enter a position: ")
        move_lst = move.split()
        move_lst[0] = int(move_lst[0])
        move_lst[1] = int(move_lst[1])
    board_mat[move_lst[0]][move_lst[1]] = player_token


def check_winner(board_mat): 
    '''
    This function takes in the nested list that represents the current
    game board and returns a string that represents the winner. The 
    returned string can be an empty string '', or 'X', or 'O', or 'draw'.

    Args:
        board_mat: the nested list that represents the current game board

    Return:
        A string that represents the winner. Can only be one of the following:
        1) Empty string '': game is not over, and no one is winning yet.
        2) 'X': Player X is the winner
        3) 'O': Player O is the winner
        4) 'draw': all positions on the board are taken but no one is winning.
   
    Steps:
        1. Check the winner row by row
        2. Check the winner column by column
        3. Check the winner on two diagonals
        4. Check if it is a draw
        5. Return the winner string. 
    '''
    winner = '' # The default winner is empty

    # Creates a loop to check winner
    for _ in range(len(board_mat)):
        # Checks rows for X or O winner
        if board_mat[0] == ['O','O','O'] or board_mat[1] == ['O','O','O'] or board_mat[2] == ['O','O','O']:
            winner = 'The winner is: O'
        elif board_mat[0] == ['X','X','X'] or board_mat[1] == ['X','X','X'] or board_mat[2] == ['X','X','X']:
            winner = 'The winner is: X'

        # Checks columns for X winner
        elif board_mat[0][0] == 'X' and board_mat[1][0] == 'X' and board_mat[2][0] == 'X':
            winner = 'The winner is: X'
        elif board_mat[0][1] == 'X' and board_mat[1][1] == 'X' and board_mat[2][1] == 'X':
            winner = 'The winner is: X'
        elif board_mat[0][2] == 'X' and board_mat[1][2] == 'X' and board_mat[2][2] == 'X':
            winner = 'The winner is: X'

        # Checks columns for O winner
        elif board_mat[0][0] == 'O' and board_mat[1][0] == 'O' and board_mat[2][0] == 'O':
            winner = 'The winner is: O'
        elif board_mat[0][1] == 'O' and board_mat[1][1] == 'O' and board_mat[2][1] == 'O':
            winner = 'The winner is: O'
        elif board_mat[0][2] == 'O' and board_mat[1][2] == 'O' and board_mat[2][2] == 'O':
            winner = 'The winner is: O'

        # Checks diagonals for X winner
        elif board_mat[0][0] == 'X' and board_mat[1][1] == 'X' and board_mat[2][2] == 'X':
            winner = 'The winner is: X'
        elif board_mat[0][2] == 'X' and board_mat[1][1] == 'X' and board_mat[2][0] == 'X':
            winner = 'The winner is: X'

        # Checks diagonals for O winner
        elif board_mat[0][0] == 'O' and board_mat[1][1] == 'O' and board_mat[2][2] == 'O':
            winner = 'The winner is: O'
        elif board_mat[0][2] == 'O' and board_mat[1][1] == 'O' and board_mat[2][0] == 'O':
            winner = 'The winner is: O'
        
        # Checks for a draw
        elif ' ' not in board_mat[0] and ' ' not in board_mat[1] and ' ' not in board_mat[2]:
            winner = 'The game is a draw!'

        # Returns empty string if no winner is found
        else:
            winner = ''
        
    return winner
    
    
# greeting message
print('***** Welcome to the tic-tac-toe game *****')

# assingns the return of the create_board function to a variable
board1 = create_board()
 
# creates a counter to add up turns
turn_count = 0

# creates a while loop to check for a winner, display the current board, and allow the user to input a position
while check_winner(board1) == '':
    display_board(board1)
    if turn_count % 2 == 0:
        play_a_turn(board1,'X')
    else:
        play_a_turn(board1, 'O')
    turn_count += 1
# displays the final board with winner
display_board(board1)
# prints the winner
print(check_winner(board1))