#Minimax algoritme https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/

def printBord(bord):
    print(bord[1] + '|' + bord[2] + '|' + bord[3])
    print('-+-+-')
    print(bord[4] + '|' + bord[5] + '|' + bord[6])
    print('-+-+-')
    print(bord[7] + '|' + bord[8] + '|' + bord[9])
    print("\n")


def positieOpen(position):
    if board[position] == ' ':
        return True
    else:
        return False


def plaats(letter, position):
    if positieOpen(position):
        board[position] = letter
        printBord(board)
        if (checkGelijkSpel()):
            print("Gelijk spel!")
            exit()
        if winnaarCheck():
            if letter == 'X':
                print("X wins!")
                exit()
            else:
                print("O wins!")
                exit()

        return


    else:
        print("Kies een vrije vak!")
        position = int(input("Nieuwe positie:  "))
        plaats(letter, position)
        return


def winnaarCheck():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False


def winCheck(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False


def checkGelijkSpel():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True


def speler():
    positie = int(input("Kies voor 'O':  "))
    plaats(player, positie)
    return


def ai(): #Computer strategie
    bestScore = -1000 #Global minimum
    bestMove = 0 #Begin score
    for key in board.keys(): #Zoekt voor beste positie door het hele bord
        if (board[key] == ' '):
            board[key] = bot
            score = minimax(board, 0, False) #algoritme om het beste positie te vinden
            board[key] = ' '
            if (score > bestScore): #Als het score hoger is dan het beste score, zet beste score als score
                bestScore = score
                bestMove = key

    plaats(bot, bestMove)
    return


def minimax(bord, diepte, globalMax): #Minimax algoritme volgens GeeksForGeeks
    if (winCheck(bot)):
        return 1
    elif (winCheck(player)):
        return -1
    elif (checkGelijkSpel()):
        return 0

    if (globalMax):
        bestScore = -1000 #Voor gevallen onder global min
        for key in bord.keys():
            if (bord[key] == ' '):
                bord[key] = bot
                score = minimax(bord, diepte + 1, False)
                bord[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore #nieuwe beste score gevonden

    else:
        bestScore = 1000 #Voor gevallen boven global min
        for key in bord.keys():
            if (bord[key] == ' '):
                bord[key] = player
                score = minimax(bord, diepte + 1, True)
                bord[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore #nieuwe beste score gevonden


board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

printBord(board)
print("AI begint")
ronde = 1
player = 'O'
bot = 'X'

while not winnaarCheck():
    try:
        print("Ronde: " + str(ronde))
        ronde = ronde + 1
        ai()
        print("Ronde: " + str(ronde))
        print("1, 2, 3 ")
        print("4, 5, 6 ")
        print("7, 8, 9 ")
        print("\n")
        ronde = ronde + 1
        speler()
    except:
        print("Kies een nummer")
        speler()
