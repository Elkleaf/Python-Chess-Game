# # Chess Game ##
# White King - Player X
# White Rook - Player X
# Black King - Player Y
# How to use: python3 main.py test.txt
import sys
import chessBoard as cB
import gamePiece as gP
import Rook as rP
import King as kP
import random

## Functions ##
def printHeader(testCase, heuristicFunction, wKing, wRook, bKing):
    print('-------------------------------------------')
    print('Game started...')
    print('Testcase ', testCase+1, ': ', wKing, ', ', wRook, ', ', bKing, sep='')
    print('Heuristic function used:', heuristicFunction)
    print('-------------------------------------------')

def moveBlack(heuristic, wPlayer, bPlayer):
    depth = 4

    if heuristic == 'heuristicX':
        move_to_index = randomStrategy(bPlayer[0])
    else:
        move_score, move_to_index = minimax(bPlayer[0], depth, wPlayer, bPlayer)

    # Change players piece position
    bPlayer[0].row = move_to_index[0] #Black King Piece Row
    bPlayer[0].col = move_to_index[1] #Black King Piece Column


def moveWhite(wPlayer, bPlayer):
    depth = 4

    # Initialize moves
    wPlayer[0].set_legal_moves()
    wPlayer[1].set_legal_moves()
    bPlayer[0].set_legal_moves()

    wPlayer[0].attack_value = calculateAttackValue(wPlayer[0].legal_moves, bPlayer[0].legal_moves)
    wPlayer[1].attack_value = calculateAttackValue(wPlayer[1].legal_moves, bPlayer[0].legal_moves)

    # Remove Checks after attack values have been set!
    removeChecksWhite(wPlayer, bPlayer)

    if wPlayer[0].attack_value < wPlayer[1].attack_value:
        # Move the King
        move_score, move_to_index = minimax(wPlayer[0], depth, wPlayer, bPlayer)

        wPlayer[0].row = move_to_index[0] #White King Piece Row
        wPlayer[0].col = move_to_index[1] #White King Piece Column
    else:
        # Move the Rook
        move_score, move_to_index = minimax(wPlayer[1], depth, wPlayer, bPlayer)

        wPlayer[1].row = move_to_index[0] #White King Piece Row
        wPlayer[1].col = move_to_index[1] #White King Piece Column


def removePiecePositions(gamePiece1, wPlayer, bPlayer):
    gamePiece1.set_temp_legal_moves()

    if gamePiece1.tag == 'wK':
        w_rook = (wPlayer[1].row, wPlayer[1].col)
        b_king = (bPlayer[0].row, bPlayer[0].col)

        if w_rook in gamePiece1.temp_legal_moves: gamePiece1.temp_legal_moves.remove(w_rook)
        if b_king in gamePiece1.temp_legal_moves: gamePiece1.temp_legal_moves.remove(b_king)

    elif gamePiece1.tag == 'wR':
        w_king = [(wPlayer[0].row, wPlayer[0].col)]
        b_king = [(bPlayer[0].row, bPlayer[0].col)]

        if w_king in gamePiece1.temp_legal_moves: gamePiece1.temp_legal_moves.remove(w_king)
        if b_king in gamePiece1.temp_legal_moves: gamePiece1.temp_legal_moves.remove(b_king)

    else:
        w_king = [(wPlayer[0].row, wPlayer[0].col)]
        w_rook = [(wPlayer[1].row, wPlayer[1].col)]

        if w_king in gamePiece1.temp_legal_moves: gamePiece1.temp_legal_moves.remove(w_king)
        if w_rook in gamePiece1.temp_legal_moves: gamePiece1.temp_legal_moves.remove(w_rook)


def minimax(gamePiece1, depth, wPlayer, bPlayer):
    """Returns a tuple (score, bestmove) for the position at the given depth.
        Alternates between white and black player's optimal moves. """
    # Inspired from here: http://www.naftaliharris.com/blog/chess/

    if gamePiece1.color == "white":
        if depth == 0 or checkmate(gamePiece1):
            gamePiece1.set_temp_legal_moves()
            removePiecePositions(gamePiece1, wPlayer, bPlayer)
            # Technically our Heuristic is here, calculate attack values...
            gamePiece1.attack_value = heuristicX(gamePiece1.temp_legal_moves, bPlayer[0].legal_moves)
            if gamePiece1.tag == 'wR':
                if gamePiece1.tempRow == bPlayer[0].row or gamePiece1.tempCol == bPlayer[0]:
                    gamePiece1.attack_value = gamePiece1.attack_value + 100
            return (gamePiece1.attack_value, (gamePiece1.tempRow , gamePiece1.tempCol))
        else:
            bestscore = -float("inf")
            bestmove = None

            for move in gamePiece1.legal_moves:
                gamePiece1.tempRow = move[0]
                gamePiece1.tempCol = move[1]
                score, move = minimax(gamePiece1, depth - 1, wPlayer, bPlayer)
                if score > bestscore:
                    bestscore = score
                    bestmove = move
            return (bestscore, bestmove)
    else:
        if depth == 0 or checkmate(gamePiece1):
            gamePiece1.set_temp_legal_moves()
            removePiecePositions(gamePiece1, wPlayer, bPlayer)
            # Technically our Heuristic is here, calculate attack values...
            gamePiece1.attack_value = heuristicY(gamePiece1.temp_legal_moves, wPlayer[0].legal_moves)
            gamePiece1.attack_value = gamePiece1.attack_value + heuristicY(gamePiece1.temp_legal_moves, wPlayer[1].legal_moves)
            return (gamePiece1.attack_value, (gamePiece1.tempRow, gamePiece1.tempCol))
        else:
            bestscore = float("inf")
            bestmove = None
            for move in gamePiece1.legal_moves:
                gamePiece1.tempRow = move[0]
                gamePiece1.tempCol = move[1]
                score, move = minimax(gamePiece1, depth - 1, wPlayer, bPlayer)
                if score < bestscore:
                    bestscore = score
                    bestmove = move
            return (bestscore, bestmove)


def heuristicX(player1_move_list, player2_move_list):
    """Heuristic actually happens in Min/Max function. This only specifies Black Move's behavior"""
    return calculateAttackValue(player1_move_list, player2_move_list)


def heuristicY(player1_move_list, player2_move_list):
    """Heuristic actually happens in Min/Max function. This only specifies Black Move's behavior"""
    return calculateAttackValue(player1_move_list, player2_move_list)


def removeChecksWhite(w_player, b_player):
    w_king = (w_player[0].row, w_player[0].col)
    w_rook = (w_player[1].row, w_player[1].col)
    b_king = (b_player[0].row, b_player[0].col)

    # Filter out intersection with black player
    # Check king first, then rook
    w_king_moves = [x for x in w_player[0].legal_moves if x not in b_player[0].legal_moves]
    w_rook_moves = [x for x in w_player[1].legal_moves if x not in b_player[0].legal_moves]

    # Remove actual positions as well
    if w_rook in w_king_moves:
        w_king_moves.remove(w_rook)
    if b_king in w_king_moves:
        w_king_moves.remove(b_king)

    # Also need to remove additional rook moves beyond
    if w_king in w_rook_moves: 
        w_rook_moves.remove(w_king)
    if b_king in w_rook_moves:
        w_rook_moves.remove(b_king)
    if w_rook in w_rook_moves:
        w_rook_moves.remove(w_rook)

    # Remove moves beyond blocking units
    if w_player[1].row == w_player[0].row:
        if w_player[1].col > w_player[0].col:
            temp = w_player[0].col - 1

            for i in range(1, (temp+1)):
                if (w_player[0].row, temp) in w_rook_moves:
                    w_rook_moves.remove((w_player[0].row,temp))
        else:
            for i in range(w_player[0].col, 9):
                if (w_player[0].row, i) in w_rook_moves:
                    w_rook_moves.remove((w_player[0].row,i))

    if w_player[1].col == w_player[0].col:
        if w_player[1].row > w_player[0].row:
            temp = w_player[0].row - 1

            for i in range(1, (temp + 1)):
                if (i, w_player[0].col) in w_rook_moves:
                    w_rook_moves.remove((i,w_player[0].col))
        else:
            for i in range(w_player[0].row,9):
                if (i, w_player[0].col) in w_rook_moves:
                    w_rook_moves.remove((i,w_player[0].col))

    #Tests
    #print('White King Moves Before:', w_player[0].legal_moves)
    #print('White Rook Moves Before:', w_player[1].legal_moves)
    #print('------------------------')
    #print('White King Moves After:', w_king_moves)
    #print('White Rook Moves After:', w_rook_moves)
    
    # Set legal moves to new values
    w_player[0].legal_moves = w_king_moves
    w_player[1].legal_moves = w_rook_moves
    

def removeChecksBlack(w_player, b_player):
    w_king = (w_player[0].row, w_player[0].col)
    w_rook = (w_player[1].row, w_player[1].col)
    b_king = (b_player[0].row, b_player[0].col)

    # Filter out intersection with white player
    # Check against king, then against rook
    b_king_moves = [x for x in b_player[0].legal_moves if not x in w_player[0].legal_moves]
    b_king_moves = [x for x in b_king_moves if x not in w_player[1].legal_moves]

    # Remove actual positions as well
    if w_king in b_king_moves: b_king_moves.remove(w_king)
    if w_rook in b_king_moves: b_king_moves.remove(w_rook)

    #Tests
    # print('Black King Moves Before:', b_player[0].legal_moves)
    # print('------------------------')
    # print('Black King Moves After:', b_king_moves)

    # Set legal moves to new values
    b_player[0].legal_moves = b_king_moves


def randomStrategy(playerPiece):
    return random.choice(playerPiece.legal_moves)


def calculateAttackValue(player1_move_list, player2_move_list):
    # Function calculates attack value of player 1
    # Attack value is determined by the number of spaces the player 1 and player 2 share

    attackValue = 0

    for move in player1_move_list:
        if move in player2_move_list:
            #print('attack move: ', move)
            attackValue = attackValue + 1

    return attackValue


def checkmate(bKing):
    # Analyze each gamepieces next possible moves, and check if any overlap(those are attack positions)

    if len(bKing.legal_moves) == 0:
        return True
    else:
        return False


def play(maxMoves, heuristic, wPlayer, bPlayer):
    chessBoard = cB.ChessBoard()
    chessBoard.printBoard(wPlayer, bPlayer)

    for i in range(0, maxMoves):
        print("== Turn", i+1, "==")

        # White moves first
        print("White to move")

        # Set possible moves
        wPlayer[0].set_legal_moves()
        wPlayer[1].set_legal_moves()
        bPlayer[0].set_legal_moves()
        removeChecksWhite(wPlayer, bPlayer)

        moveWhite(wPlayer, bPlayer)
        chessBoard.printBoard(wPlayer, bPlayer)

        # Black moves second
        # Re-evaluate possible moves again for Black player
        wPlayer[0].set_legal_moves()
        wPlayer[1].set_legal_moves()
        bPlayer[0].set_legal_moves()
        removeChecksBlack(wPlayer, bPlayer)

        print("Black to move")

        if(checkmate(bPlayer[0])):
            print('Checkmate, game over!')
            return
        else:
            moveBlack(heuristic, wPlayer, bPlayer)
            chessBoard.printBoard(wPlayer, bPlayer)
    
    print("Stalemate")


## Main ##
def main():
    # Open file with Test Cases
    if len(sys.argv) <= 1:  # python3 main.py
        file_name = 'test.txt'
    else:
        file_name = sys.argv[1]

    # Read entire input from file
    with open(file_name) as input_file:
        lines = input_file.readlines()

    numLoop = int(lines[0])
    maxMoves = int(lines[1])

    # Loop for how many test cases the user is going to send in
    for testCase in range(0, numLoop):
        # Grab pieces, offsetting by 3 each time
        i = (testCase * 3) + 1
        wKing, wRook, bKing = [lines[i + 1].rstrip(), lines[i + 2].rstrip(), lines[i + 3].rstrip()]

        # Error Checking
        assert (wKing[:2] == 'w(')
        assert (wRook[:2] == 'r(')
        assert (bKing[:2] == 'b(')

        # First run Heuristic X
        heuristic = 'heuristicX'

        # Print the header
        printHeader(testCase, heuristic, wKing, wRook, bKing)

        # Create game pieces
        wKing = kP.King("wK", int(wKing[2:3]), int(wKing[4:5]), "white")
        wRook = rP.Rook("wR", int(wRook[2:3]), int(wRook[4:5]), "white")
        bKing = kP.King("bK", int(bKing[2:3]), int(bKing[4:5]), "black")

        # Organize pieces under players
        wPlayer = [wKing, wRook]
        bPlayer = [bKing]

        # Play game and loop through logic
        play(maxMoves, heuristic, wPlayer, bPlayer)

        ################################
        # Play again under Heuristic Y #
        heuristic = 'heuristicX&Y'

        # Grab info again to print out
        wKing, wRook, bKing = [lines[i + 1].rstrip(), lines[i + 2].rstrip(), lines[i + 3].rstrip()]

        # Print the header
        printHeader(testCase, heuristic, wKing, wRook, bKing)

        # Recreate game pieces to reset positions
        wKing = kP.King("wK", int(wKing[2:3]), int(wKing[4:5]), "white")
        wRook = rP.Rook("wR", int(wRook[2:3]), int(wRook[4:5]), "white")
        bKing = kP.King("bK", int(bKing[2:3]), int(bKing[4:5]), "black")

        # Organize pieces under players
        wPlayer = [wKing, wRook]
        bPlayer = [bKing]

        # Play game and loop through logic
        play(maxMoves, heuristic, wPlayer, bPlayer)


if __name__ == '__main__':
    main()
