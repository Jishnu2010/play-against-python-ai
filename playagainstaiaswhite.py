import chess, random
board=chess.Board()
print('Play against a very very easy AI as white.Just input your move notation and play!\n')
while True:
    if board.is_checkmate()==True:
    	print('Checkmate')
    elif board.is_stalemate()==True:
    	print('Stalemate')
    elif board.is_insufficient_material()==True:
    	print('Insufficurnt Material')
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