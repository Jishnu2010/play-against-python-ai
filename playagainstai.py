import chess, random, time #modules needed
board=chess.Board() #the board
game_over=True #to check if game is over in a condition
print("Welcome to Play Against AI (PAA)!\nHere you have to play as black against a engine.\nDo not worry, the engine is super easy.\nIt uses python's 'chess','random' and 'time' modules to play.\nIt starts off as white.\nWhite pieces will appear as CAPITAL letter and Black pieces as small letters.\nHave fun!") #intro
print()
while True: #our master loop (game loop)
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

	legalmoves=list(board.legal_moves) #list of legal moves
	enginemove=random.choice(legalmoves) #a random choice
	producesan=board.variation_san([enginemove]) #the engine's move notation
	print()
	print('Current Position:')
	print()
	print(board) #current position
	print()
	print('AI thinking...')
	print()
	time.sleep(3) #to make it feel like a human
	board.push(enginemove) #give AI's move
	print('Current Position:')
	print()
	print(board) #current position
	print()
	print('Engine Move:', producesan) #to help black
	print()
	humanmove=input('Your move: ') #move of black(human) in SAN notation
	board.push_san(humanmove) #give black move
	print('Current Position:')
	print()
	print(board) #current position
	print()

'''
And that's it. Very simple but fun. Hope you have fun!
'''