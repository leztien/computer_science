mapping = {1: 'X', -1: 'O', 0: ' '}



def display(board):
    bar = "  " + '-' * 7

    print()
    print("   1 2 3 ")
    print(bar)
    for idx,letter in zip(range(0,7,3), "ABC"):
        line = '|'.join([mapping[i] for i in board[idx:idx +3 ]])
        line = f'{letter} |' + line + '|'
        print(line)
        print(bar)
    print()



def get_user_input(player):
    """
    Decodes the user's input into a list index
    Returns the index of the 'board' list
    """

    msg = f"\nPlayer {mapping[player]}, please make your move!\n "

    # validate user's input
    while True:
        user_input = s = input(msg)

        checks = (len(s) == 2, 
                  s[0].lower() in "abc", 
                  s[-1] in "123")

        if not all(checks):
            print("Your input must be in this format: A1\n")
        else:
            break

    row, column = user_input.lower()
    return {"a":0, "b":3, "c":6}[row] + int(column) - 1



def update(board, index, player):
    """
    It updates the board and returns true if i was successful and returns false if not
    """

    #checking wether cell is empty
    if board[index] != 0: 
        return False
    
    #updating the board
    board[index] = player
    return True



def check_winner(board):
    """
    Checks the 'board' list for a winner.
    Returns 1 or -1 if there's a winner
    otherwise returns None
    """
    # Check the rows
    for i in range(0, 7, 3):
        section = board[i: i+3]
        if abs(sum(section)) == 3:
            return section[0]

    # Check the column s
    for j in (0, 1, 2):
        section = board[j: j+7: 3]
        if abs(sum(section)) == 3:
            return section[0]

    # Check the diagonals
    for t in [(0,4,8), (2,4,6)]:
        section = [board[ix] for ix in t]
        if abs(sum(section)) == 3:
            return section[0]
