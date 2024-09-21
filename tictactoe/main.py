play = True
while play:
    board = [" "for _ in range(9)]
    def print_board():
        row1 = f"| {board[0]} | {board[1]} | {board[2]} |"
        row2 = f"| {board[3]} | {board[4]} | {board[5]} |"
        row3 = f"| {board[6]} | {board[7]} | {board[8]} |"
        print()
        print(row1)
        print(row2)
        print(row3)
        print()
        
    def player_turn(move):    
        print(f"Your turn {move}")
        while True:
            try:
                choice = int(input("Enter your move from (1-9) ").strip())
                if 1 <= choice <= 9:
                    if board[choice-1] == " ":
                        board[choice-1] = move
                        break
                    else:
                        print("The space is already taken")
                        print_board()
                else:
                    print("Please enter number between 1 and 9")
                    print_board()
            except ValueError:
                print("Invalid input. Please enter number between 1 and 9")

    def is_victor(move):
        return(board[0]==move and board[1]==move and board[2]==move) or  \
            (board[3]==move and board[4]==move and board[5]==move) or  \
            (board[6]==move and board[7]==move and board[8]==move) or  \
            (board[0]==move and board[3]==move and board[6]==move) or  \
            (board[1]==move and board[4]==move and board[7]==move) or  \
            (board[2]==move and board[5]==move and board[8]==move) or  \
            (board[0]==move and board[4]==move and board[8]==move) or  \
            (board[2]==move and board[4]==move and board[6]==move)

        
    def is_draw():
        return " " not in board
        
    while True:
        print_board()
        player_turn("X")
        print_board()
        if is_victor("X"):
            print("X won the Game")
            break
        elif is_draw():
            print("It's a draw")
            break
        
        player_turn("O")
        print_board()
        if is_victor("O"):
            print("O won the Game")
            break
        elif is_draw():
            print("It's a draw")
            break
        
    print("Thanks for playing the game")
    play_again= input("Do you want to play more (y/n)").upper()
    play = True if play_again =="Y" else False
