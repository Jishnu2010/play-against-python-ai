import chess, random
board=chess.Board()
print('Play against a very very easy AI as white.Just input your move notation and play!\n')
while True:
    stateofcheckmate=board.is_checkmate() #If checkmate
    isinsufficientmaterial=board.is_insufficient_material() #If draw by insufficient material
    isstalemate=board.is_stalemate() #if stalemate
    if stateofcheckmate==game_over: #if checkmate
	print('Checkmate!')
	break #stops program

    elif isstalemate==game_over: #if stalemate
	print('Draw by Stalemate\nResult: 1/2 - 1/2')
	break #stops progam

    elif isinsufficientmaterial==game_over: #if insufficient material
	print('Draw by Insufficient material\nResult: 1/2 - 1/2')
	break #stops program

    print(board)
    print()
    hmove=input('Enter Move: ')
    board.push_san(hmove)
    lmove=list(board.legal_moves)
    emove=random.choice(lmove)
    esmove=board.variation_san([emove])
    board.push(emove)
    print()
    print('Engine gave move: {}'.format(esmove))
    print()
