# Chess Board AI #
This simulates a relatively simple chess endgame. Player X has a rook and king and Player Y has only the king left. Of course, with more chess pieces, Player X will likely win this game. So Player X tries to win the game as quickly as possible avoiding the infinite loop or dead end. On the other hand, Player Y tries to play the game as long as possible by delaying it.

## Structure  ##
### main.py ###
* Runs the program as a main driver. The Controller class.
* Initializes everything in main function.
* whitePlayer = [wKing, wRook]
* blackPlayer = [bKing]
* play(n, whitePlayer, blackPlayer)
* checkAttack()
* moveWhite()
* moveBlack()
* minMax()
* heuristicX()
* heuristicY()
* checkDistance()

### chessBoard.py ####
* Acts as the View displaying the pieces on the board.
* displayBoard()

### gamePiece.py ###
* Model to store each piece's info
* tag
* row
* col
* [list of moves]

### kingPiece.py ###
* subclass of gamePiece.py
* getMoves()

### rookPiece.py ###
* subclass of gamePiece.py
* getMoves()

### Things to keep in mind ###
* White King - Player X
* White Rook - Player X
* Black King - Player Y
* We're using Python3 not Python2
* To edit this README. [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How to run ###
```
python3 main.py test.txt
```