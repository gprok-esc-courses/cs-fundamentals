
# board = [
#     ['-', '-', '-'],
#     ['-', '-', '-'],
#     ['-', '-', '-']
# ]

# board = []
# for i in range(3):
#     d = []
#     for j in range(3):
#         d.append('-')
#     board.append(d)

def display_board(b):
    """
    Display the Tic Tac Toe board  
    b: The board to be displayed
    """
    for r in range(3):
        for c in range(3):
            print(b[r][c], end=' ')
        print()

def play():
    """
    Ask user to play, row and col and return the result
    """
    row = int(input("Row: "))
    col = int(input("Col: "))
    return row, col

board = [['-'] * 3 for i in range(3)]
player = 'X'

while True:
    display_board(board)
    r, c = play()
    # if position is empty
    if board[r][c] == '-':
        # update board
        board[r][c] = player
        # change player
        player = 'X' if player == 'O' else 'O'
        # Check for winner
        # If no winner, check for Tie
    else:
        # error
        print("Error: not empty position")
