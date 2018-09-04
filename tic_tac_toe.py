#Make are tic-tac-toe game
print("Welcome to tic-tac-toe.")
gameBoard = [] #[["1,1", "1,2", "1,3"], ["2,1", "2,2", "2,3"], ["3,1", "3,2", "3,3"]]

playersTurn = 0

def check_player(num):
    if num % 2 == 0:
        return "X's"
    else:
        return "O's"


def insert_tic(player, x, y):
    tic = " "
    turn = check_player(player)

    if turn == "X's":
        tic = " X "
    else: tic = " O "
    gameBoard[x-1][y-1] = tic

    return gameBoard


def check_tic(list):
    tic = gameBoard[list[0]-1][list[1]-1]

    if tic == ' X ' or tic == ' O ':
        return 1
    else:
        return 0


def choose_tic():
    print(check_player(playersTurn) + "'s turn")

    while True:
        coords = input("Where do you want to set your piece? 'x,y': ")
        coords = coords.split(",")

        #check if the input is a legal move
        try:
            coords = [int(coord) for coord in coords]
        except ValueError:
            print("Oops! seems like those numbers are off. Try again...")
            continue

        test = 0
        for coord in coords:
            if coord > len(gameBoard) or coord <= 0:
                print("Number was out of bounds. Try again...")
                test = 1
        if test == 1:
            continue

        #If the move is legal, we stop the loop
        break

    return coords


def condition_win(list):
    xs = 0
    os = 0
    for y in list:
        if y == ' X ':
            xs += 1
        if y == ' O ':
            os += 1

    if xs == len(list) or os == len(list):
        return 1


def test_win():
    win = 0

    while True:
        #testing rows
        for x in gameBoard:
            win = condition_win(x)
            if win == 1:
                return 1
        if win == 1:
            break

        #testing columns
        for i in range(len(gameBoard)):
            test = []
            for x in gameBoard:
                test.append(x[i])

            win = condition_win(test)
            if win == 1:
                return 1
                break

        #testing diagonal
        x_test2 = []
        y_test2 = []
        for i in range(len(gameBoard)):
            x_test = gameBoard[i]
            x_test2.append(x_test[i])
            #print(x_test2)

            y_test = gameBoard[i]
            y_test2.append(y_test[-(i+1)])
            #print(y_test2)
        win = condition_win(x_test2)
        if win == 1:
            return 1
            break
        win = condition_win(y_test2)
        if win == 1:
            return 1
            break

        return 0
        break


def print_board():
    for tac in gameBoard:
        print(tac)


def create_board(size):
    board = []
    for i in range(size):
        board.append([])
        for j in range (size):
            board[i].append(str(i+1) + "," + str(j+1))

    return board


#create the game
while True:
    try:
        size = int(input("What size should the game be? (3-5): "))
    except ValueError:
        print("Oops! seems like thats not a number. Try again...")
        continue
    if size < 3 or size > 5:
        print("Oops! seems like those numbers are off. Try again...")
        continue

    gameBoard = create_board(size)
    break

#play game
while True:
    tic = []
    print_board()

    run = 1
    while run == 1:
        tic = choose_tic()
        run = check_tic(tic)
        if run == 1:
            print("That place is taken, try again:")

    insert_tic(playersTurn, tic[0], tic[1])

    win_condition = test_win()
    if win_condition == 1:
        print("The game is over. " + check_player(playersTurn) + " has won!")
        print_board()
        break

    playersTurn += 1
    if playersTurn == len(gameBoard)**2:
        print("The game is over. No winners!")
        print_board()
        break


