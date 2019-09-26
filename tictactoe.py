# import only system from os
from os import system, name


def clear_screen():
    ''' 
    makes a call to the system to clear
    the console screen for windows or mac/linux
    '''

    _ = system('cls') if name == 'nt' else system('clear')


def create_board():
    '''
    creates an empty board
    '''
    board = [["  -  " for i in range(3)] for i in range(3)]
    return board


def display_board(board):
    '''
    print the given board with line breaks
    '''
    for row in board:
        for square in row:
            print(square, end='')
        print()
        print()


def play_letter(board, position, player, played_positions):
    '''
    puts a letter on the board and returns the modified board
    '''

    # translate position to x,y grid values
    position_translation = {
        1: (0, 0), 2: (1, 0), 3: (2, 0),
        4: (0, 1), 5: (1, 1), 6: (2, 1),
        7: (0, 2), 8: (1, 2), 9: (2, 2)
    }

    # set row and column based on translation
    row = position_translation[position][0]
    col = position_translation[position][1]

    played_coords = (row, col)

    # add to played_positions, return if already played
    if played_coords in played_positions:
        return
    else:
        played_positions.append(played_coords)

    # set the marker depending on who the player is
    board[col][row] = '  x  ' if player == 1 else '  o  '

    return board


def swap(player):
    '''
    toggles player 1 or 2 based on previous value
    '''
    return 2 if player == 1 else 1


def check_win(board):
    '''
    checks for a win in row/col/diag
    if a win is found, prints winner
    '''

    found = False

    # check row win
    for row in board:
        if len(set(row)) == 1:
            print(row[0] + ' wins!')
            found = True
            return

    # check column win
    for column in zip(*board):
        if len(set(column)) == 1:
            print(column[0] + ' wins!')
            found = True
            return

    # check diagonal win
    if (board[1][1] == board[0][0] and board[1][1] == board[2][2])\
            or (board[1][1] == board[0][2] and board[1][1] == board[2][0]):
        print(board[1][1] + ' wins!')
        found = True
        return

    print('Sorry! Nobody won!')


if __name__ == "__main__":
    play = input('Do you want to play?')
    player1 = input('Want to be X or O?')
    player2 = 'o' if player1 == 'x' else 'x'
    played_positions = []
    player = 1

    board = create_board() if play.lower() == 'yes' or 'y' else exit

    while len(played_positions) < 9:
        clear_screen()
        display_board(board)
        position = int(input('Which square do you want to play in? (1-9)'))
        play_letter(board, position, player, played_positions)
        clear_screen()
        display_board(board)
        player = swap(player)

    if len(played_positions) == 9:
        check_win(board)
