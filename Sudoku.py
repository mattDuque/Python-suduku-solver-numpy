import numpy as np
import random

setDif = 'Easy'

def createBoard():
	board = np.zeros((9,9), int)
	j = 0
	for i in range(3):
		array = np.asarray(random.sample(range(1,10), 9)).reshape(3,3)
		board[(0+j):(3+j), (0+j):(3+j)] = array
		j+=3
	return board

def Solve(board): 
	if not findEmpty(board):
		return True
	else:
		x, y = findEmpty(board)
	for i in range (1,10):
		if isValid(board, i, x, y):
			board[x,y] = i
			if Solve(board):
				return True
			board[x,y] = 0
	return False
	
def findEmpty(board):
	for x in range (9):
		for y in range (9):
			if board[x,y] == 0:
				return (x,y)

def isValid(board, num, x, y):
	cS_x = (x//3)*3
	cS_y = (y//3)*3
	currentSquare = np.asarray(board[(cS_x):(cS_x+3),(cS_y):(cS_y+3)])
	currentRow = board[x]
	currentColumn = board[:,y]
	if num not in currentRow:
		if num not in currentColumn:
			if num not in currentSquare:
				return True

def unSolve(setDif, board):  
	if setDif == 'Easy':
		spread = ([1]*7 + [0]*3)
	elif setDif == 'Medium':
		spread = ([1]*6 + [0]*4)
	elif setDif == 'Hard':
		spread = ([1]*4 + [0]*6)
	bo = board.flatten()
	for i in range (81):
		if random.choice(spread) == 0:
			bo[i] = 0
	bo = bo.reshape(9,9)
	return bo

board = createBoard()
Solve(board)
print(board)
newBoard = unSolve(setDif, board)
print("")
print(newBoard)

