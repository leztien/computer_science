
"""
a basic algorithm for the Tic Tac Toe game
"""


from itertools import cycle
from utilities import display, get_user_input, update, check_winner, mapping


def play():

    # initialize an empty board (board is a list)
    board = [0] * 9

    # display empty board
    display(board)

    # the playing loop
    for move, player in zip(range(1,10), cycle([1,-1])):

        while True:
            index = get_user_input(player)

            if update(board, index, player):
                break
            else:
                print("The cell you've selected is taken")


        display(board)

        # check for the winner only after move 5
        if move < 5:
            continue
        
        # check winner
        winner = check_winner(board)

        if winner:
            print("The winner is", mapping[winner])
            break
    else:
        print("DRAW")

    print("The game is over")



if __name__ == '__main__':
    play()
