import numpy as np
import math
import pygame
import sys


BLUE = (0,0,255)
RED = (255,0,0)
YELLOW = (0,255,0)
BLACK = (0,0,0)
ROW_C=6
COLUMN_C=7

def create_board():
	board = np.zeros((ROW_C, COLUMN_C))
	return board 

def print_board(board):
	print(np.flip(board, 0))

def drop_piece(board, row, col, piece):
	board[row][col] = piece 
	

def is_valid_location(board, col):
	return board[ROW_C - 1][col] == 0

def get_next_open_row(board, col):
	for r in range(ROW_C):
		if board[r][col] == 0:
			return r 
def winning_move(board, piece):
	for c in range(COLUMN_C-3):
		for r in range(ROW_C):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True
	for c in range(COLUMN_C):
		for r in range(ROW_C-3):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True

#diagnols
	for c in range(COLUMN_C- 3):
		for r in range(ROW_C - 3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True
	for c in range(COLUMN_C-3):
		for r in range(3, ROW_C):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r+3][c+3] == piece: 
				return True

def draw_board(board):
	for c in range(COLUMN_C):
		for r in range(ROW_C):
			pygame.draw.rect(screen, BLUE, (c*squaresize, r*squaresize + squaresize, squaresize, squaresize))
			pygame.draw.circle(screen, (0,0,0), (c*squaresize+squaresize/2, r*squaresize+squaresize+squaresize/2), RADIUS)
	for c in range(COLUMN_C):
		for r in range(ROW_C):
			if board[r][c] == 1:
				pygame.draw.circle(screen, RED, (int((c*squaresize+squaresize/2)), height - int(r*squaresize+squaresize/2)), RADIUS)
			elif board[r][c] == 2:
				pygame.draw.circle(screen, YELLOW, (int((c*squaresize+squaresize/2)), height - int(r*squaresize+squaresize/2)), RADIUS)
	pygame.display.update()





board = create_board()
print_board(board)
game_over = False
turn = 0


#pygame stuff
pygame.init()
squaresize = 100
width = COLUMN_C * squaresize
height = (ROW_C + 1) * squaresize
size = (width, height)
RADIUS = int(squaresize/2 - 5)
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

while not game_over:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(screen, BLACK, (0,0, width, squaresize))
			posx = event.pos[0]
			if turn == 0:
				pygame.draw.circle(screen, RED, (posx, int(squaresize/2)), RADIUS)
			else:
				pygame.draw.circle(screen, YELLOW, (posx, int(squaresize/2)), RADIUS)
		pygame.display.update()

		if event.type == pygame.MOUSEBUTTONDOWN:
			if turn == 0:
				posx = event.pos[0]
				col = int(math.floor(posx/squaresize))

				if is_valid_location(board,col):
					row = get_next_open_row(board,col)
					drop_piece(board, row, col, 1)
				if winning_move(board, 1):
					print("Player 1 wins")
					game_over = True
			else: 
				posx = event.pos[0]
				col = int(math.floor(posx/squaresize))

				if is_valid_location(board,col):
					row = get_next_open_row(board,col)
					drop_piece(board, row, col, 2)

				if winning_move(board, 2):
					print("Playoer 2 wins")
					game_over = True

	
			print_board(board)
			draw_board(board)

			turn += 1
			turn = turn % 2


