import chess, random
board=chess.Board()
print('Play against a very very easy AI as white.Just input your move notation and play!\n')
while True:
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