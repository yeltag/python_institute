from random import randrange


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print(f"""+-------+-------+-------+

|       |       |       |

|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |

|       |       |       |

+-------+-------+-------+

|       |       |       |

|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |

|       |       |       |

+-------+-------+-------+

|       |       |       |

|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |

|       |       |       |

+-------+-------+-------+""")



def enter_move(board):
    #stop_game = False
    while True:
        try:
            #while not stop_game:
             corr_move = False
             while corr_move == False:
                user_move = int(input("Enter your move:"))
                list = make_list_of_free_fields(board)
                for free_field in range(len(list)):
                    if board[list[free_field][0]][list[free_field][1]] == user_move:
                        corr_move = True
                        board[list[free_field][0]][list[free_field][1]]="O"
                        display_board(board)
                        stop_game = victory_for(board,"O")
                        if  stop_game:
                            exit()
                        draw_move(board)

        except ValueError:
            print ("Wrong move. Enter an integer number for free field.")



# The function accepts the board's current status, asks the user about their move,
# checks the input, and updates the board according to the user's decision.

def make_list_of_free_fields(board):
    list_of_free_fields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != "X" and board[i][j] != "O":
                list_of_free_fields.append((i,j))
    return list_of_free_fields

# The function browses the board and builds a list of all the free squares;
# the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board, sign):

    list = make_list_of_free_fields(board)
    if ((board[0][0] == board [0][1] == board [0][2] == sign) or\
            (board[1][0] == board [1][1] == board [1][2] == sign) or\
            (board[2][0] == board [2][1] == board [2][2] == sign) or\
            (board[0][0] == board [1][1] == board [2][2] == sign) or
            (board[0][2] == board [1][1] == board [2][0] == sign) or\
            (board[0][0] == board [1][0] == board [2][0] == sign) or\
            (board[0][1] == board [1][1] == board [2][1] == sign)) or\
            (board[0][2] == board [1][2] == board [2][2] == sign):
        print ("You won!" if sign == "O" else "You lost!")
        return  True

    elif list == []:
        print ("The game ends with a tie")
        return  True
    else:
        return  False


# The function analyzes the board's status in order to check if
# the player using 'O's or 'X's has won the game


def draw_move(board):
    list = make_list_of_free_fields(board)
    move = randrange(len(list))
    board[list[move][0]][list[move][1]]="X"
    display_board(board)
    stop_game = victory_for(board,"X")
    if stop_game:
        exit()
    enter_move(board)
# The function draws the computer's move and updates the board.


board = [[1,2,3],[4,"X",6],[7,8,9]]

display_board(board)
enter_move(board)