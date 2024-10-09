import random, copy

# Function to print the Tic Tac Toe board
def drawBoard(board):
    # Print the board in a 3x3 grid format
    print(board['top-L'] + '|'+ board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|'+ board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|'+ board['low-M'] + '|' + board['low-R'])

# Function to let the player choose between 'X' and 'O'
def inputPlayerLetter():
    letter = ""  # Initialize letter as empty
    while not (letter == 'X' or letter == 'O'):  # Loop until player chooses 'X' or 'O'
        print('Do you want to be X or O?')
        letter = input().upper()  # Get player's choice and convert to uppercase
    if letter == 'X':
        return ['X', 'O']  # Return player as 'X', computer as 'O'
    else:
        return ['O', 'X']  # Return player as 'O', computer as 'X'

# Function to randomly decide who goes first
def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'  # Computer goes first
    else:
        return 'player'  # Player goes first

# Function to ask if the player wants to play again
def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')  # Return True if player types 'yes'

# Function to make a move on the board
def makeMove(board, letter, move):
    board[move] = letter  # Assign the move to the given letter ('X' or 'O')

# Function to check if a player has won
def isWinner(bo, le):
    # Check all possible winning combinations (rows, columns, diagonals)
    return ((bo['top-L'] == le and bo['top-M'] == le and bo['top-R'] == le) or
            (bo['mid-L'] == le and bo['mid-M'] == le and bo['mid-R'] == le) or
            (bo['low-L'] == le and bo['low-M'] == le and bo['low-R'] == le) or
            (bo['top-L'] == le and bo['mid-L'] == le and bo['low-L'] == le) or
            (bo['top-M'] == le and bo['mid-M'] == le and bo['low-M'] == le) or
            (bo['top-R'] == le and bo['mid-R'] == le and bo['low-R'] == le) or
            (bo['top-L'] == le and bo['mid-M'] == le and bo['low-R'] == le) or
            (bo['top-R'] == le and bo['mid-M'] == le and bo['low-L'] == le))

# Function to check if a space on the board is free
def isSpaceFree(board, move):
    return board[move] == ' '  # Return True if the space is empty

# Function to get the player's move
def getPlayerMove(board):
    move = ''  # Initialize move as empty
    # Loop until a valid move is made (must be a free space on the board)
    while move not in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split() or not isSpaceFree(board, move):
        print('What is your next move? (top-L, top-M, top-R, mid-L, mid-M, mid-R, low-L, low-M, low-R)')
        move = input()
    return move  # Return the player's valid move

# Function to randomly choose a move from a list of moves
def chooseRandomMoveFromList(board, movesList):
    possibleMoves = [move for move in movesList if isSpaceFree(board, move)]  # List of available moves
    if possibleMoves:
        return random.choice(possibleMoves)  # Choose a random move if available
    else:
        return None  # Return None if no moves are available

# Function for the computer to decide its move using a basic strategy
def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'  # Assign player's letter based on the computer's letter
    else:
        playerLetter = 'X'

    # Step 1: Check if computer can win in the next move
    for i in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split():
        dupe = copy.copy(board)  # Duplicate the board for testing
        if isSpaceFree(dupe, i):
            makeMove(dupe, computerLetter, i)
            if isWinner(dupe, computerLetter):
                return i  # Return winning move

    # Step 2: Check if player can win on their next move, and block them
    for i in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split():
        dupe = copy.copy(board)
        if isSpaceFree(dupe, i):
            makeMove(dupe, playerLetter, i)
            if isWinner(dupe, playerLetter):
                return i  # Block player's winning move

    # Step 3: Aggressive strategy to create a winning opportunity
    for i in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split():
        if isSpaceFree(board, i):
            dupe = copy.copy(board)
            makeMove(dupe, computerLetter, i)
            winning_moves = 0
            for j in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split():
                dupe2 = copy.copy(dupe)
                if isSpaceFree(dupe2, j):
                    makeMove(dupe2, computerLetter, j)
                    if isWinner(dupe2, computerLetter):
                        winning_moves += 1
            if winning_moves >= 2:  # Choose move that creates 2 winning chances
                return i

    # Step 4: Try to take one of the corners
    move = chooseRandomMoveFromList(board, ['top-L', 'top-R', 'low-L', 'low-R'])
    if move:
        return move

    # Step 5: Try to take the center
    if isSpaceFree(board, 'mid-M'):
        return 'mid-M'

    # Step 6: Take a random side move
    return chooseRandomMoveFromList(board, ['top-M', 'low-M', 'mid-L', 'mid-R'])

# Function to check if the board is full (i.e., no more moves)
def isBoardFull(board):
    return all(board[move] != ' ' for move in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split())

print('Welcome to Tic Tac Toe!')

# Main game loop
while True:
    # Reset the board before starting a new game
    theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

    playerLetter, computerLetter = inputPlayerLetter()  # Player chooses letter
    turn = whoGoesFirst()  # Randomly decide who goes first
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    # Game loop for turns between player and computer
    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)  # Show the current board
            move = getPlayerMove(theBoard)  # Get the player's move
            makeMove(theBoard, playerLetter, move)

            # Check if the player has won
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print("Hooray! You have won the game!")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is a tie!")  # Game ends in a tie
                    break
                else:
                    turn = 'computer'  # Switch to computer's turn

        else:
            move = getComputerMove(theBoard, computerLetter)  # Computer decides move
            makeMove(theBoard, computerLetter, move)

            # Check if the computer has won
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')  # Game ends in a tie
                    break
                else:
                    turn = 'player'  # Switch to player's turn

    if not playAgain():  # Ask if player wants to play again
        break  # Exit the game loop if not
