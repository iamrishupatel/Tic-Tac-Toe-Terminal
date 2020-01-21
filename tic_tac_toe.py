#board and display board /done
#take input from user /done
#update the board /done
#check for a win /done
#check for board if it is full /done
#main function

def get_board():
    board = [
            ["-","-","-"],
            ["-","-","-"],
            ["-","-","-"],
        ]

    return board

def display_board(game_board):
    for i in range(3):
        print(game_board[i])

def player_turn(game_board,player):
    print("\n"+player+"'s turn")
    pos = int(input("Enter Your Move(1-9)>>> "))
    if not  0 < pos < 10 :
        print("Please Enter a valid position.")
        player_turn(game_board,player)
    else:
        return update_board(game_board,player,pos)
        

def update_board(game_board,player,pos):
    if 0 < pos < 4:
        if game_board[0][pos-1] != "-":
            player_turn(game_board,player)
        else:
            game_board[0][pos-1] = player
    
    elif 3 < pos < 7:
        if game_board[1][pos-4] != "-":
            player_turn(game_board,player)
        else:
            game_board[1][pos-4] = player
    
    elif 6 < pos <10:
        if game_board[2][pos-7] != "-":
            player_turn(game_board,player)
        else:
            game_board[2][pos-7] = player

def check_win(game_board):
    #horizontal win
    for i in range(3):
        if game_board[i][0] == game_board[i][1] == game_board [i][2] == "X":
            return "X wins"
        elif game_board[i][0] == game_board[i][1] == game_board [i][2] == "O":
            return "O wins"
    #vertical win
    for i in range(3):
        if game_board[0][i] == game_board[1][i]  == game_board[2][i] == "X":
            return "X wins"
        elif game_board[0][i] == game_board[1][i]  == game_board[2][i] == "O":
            return "O wins"

    #diagonal win
    if game_board[0][0] == game_board[1][1] == game_board[2][2] == "X":
        return "X wins"
    elif game_board[0][0] == game_board[1][1] == game_board[2][2] == "O":
        return "O wins"
    elif game_board[0][2] == game_board[1][1] == game_board[2][0] == "X":
        return "X wins"
    elif game_board[0][2] == game_board[1][1] == game_board[2][0] == "O":
        return "O wins"
    
    return False


def is_board_full(game_board):
    if "-" in game_board[0]:
        return False
    elif "-" in game_board[1]:
        return False
    elif "-" in game_board[2]:
        return False
    else:
        return True


def main():
    my_board = get_board()
    while True:
        display_board(my_board)
        if check_win(my_board) != False:
            print(check_win(my_board))
            break
        
        if is_board_full(my_board):
            print("Game Over")
            break
        
        player_turn(my_board,"X")
        display_board(my_board)
        if check_win(my_board) != False:
            print(check_win(my_board))
            break
    
        if is_board_full(my_board):
            print("Game Over")
            break

        player_turn(my_board,"O")
        


if __name__ == "__main__":
    main()

