board = []
for i in range(9):
    board.append(' ')

def drawBoard():
    print(f'''
        {board[0]} | {board[1]} | {board[2]}
       ---|---|---
        {board[3]} | {board[4]} | {board[5]}
       ---|---|---
        {board[6]} | {board[7]} | {board[8]}
        ''')

def playerInput(player):
    while True:
        pos = int(input(f"{player}: "))
        pos = pos - 1
        if ( 0 <= pos < 10 and board[pos] == ' '):
            return pos
        else:
            print("spot already taken!!")
            continue

def checkWinner(playerOne, playerTwo):
    
    if ( board[0] == board[1] == board[2] == 'x' or
        board[3] == board[4] == board[5] == 'x' or
        board[6] == board[7] == board[8] == 'x' or
        board[0] == board[3] == board[6] == 'x' or
        board[1] == board[4] == board[7] == 'x' or
        board[2] == board[5] == board[8] == 'x' or
        board[0] == board[4] == board[8] == 'x' or
        board[2] == board[4] == board[6] == 'x' ):
        print (f"Winner is {playerOne}🥳")
        quit("Thank you for playing🙇🏻")
    
    elif ( board[0] == board[1] == board[2] == 'o' or
        board[3] == board[4] == board[5] == 'o' or
        board[6] == board[7] == board[8] == 'o' or
        board[0] == board[3] == board[6] == 'o' or
        board[1] == board[4] == board[7] == 'o' or
        board[2] == board[5] == board[8] == 'o' or
        board[0] == board[4] == board[8] == 'o' or
        board[2] == board[4] == board[6] == 'o'):
        print (f"Winner is {playerTwo}🥳")
        quit("Thank you for playing🙇🏻")

def main():
    print("Tic-Tac-toe")
    p1 = input("Enter the name of player one : ")
    p2 = input("Enter the name of player two : ")
    print('''
        1 | 2 | 3
       ---|---|---
        4 | 5 | 6
       ---|---|---
        7 | 8 | 9
        ''')
    print(f'''
Sign of {p1} : x
Sign of {p2} : o
''')
    input("Enter any key to start the game...")
    drawBoard()

    for i in range(9):

        if i%2 == 0:
            loc = playerInput(p1)
            board[loc] = 'x'
        else:
            loc = playerInput(p2)
            board[loc] = 'o'
        drawBoard()
        checkWinner(p1,p2)
    print("It was Tie🥲")

main()