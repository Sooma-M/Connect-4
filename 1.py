import pygame
import numpy

# initialize the pygame library
pygame.init()

# create the board initially by 0
TOTAL_ROW = 6
TOTAL_COLUMN = 7
board = numpy.zeros((TOTAL_ROW, TOTAL_COLUMN))

ShapeSize = 100     # size of the Square 1*1
WIDTH = TOTAL_COLUMN * ShapeSize
HEIGHT = (TOTAL_ROW + 1) * ShapeSize

# Set up the drawing window (size of the window)
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# make font
font = pygame.font.SysFont('comicsansms', 50, True)  # name of font, size

# players
COMPUTER = 1
AGENT = 2

# colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# This function checks if the given column is a valid move (i.e., if it is within the bounds of the game board and not already full).
def check_current_valid_location(board, col):
    return board[TOTAL_ROW - 1][col] == 0

# This function checks if there is any valid location (we can continue playing)
def get_all_valid_locations(board):
	valid_locations = []
	for col in range(TOTAL_COLUMN):
		if check_current_valid_location(board, col):
			valid_locations.append(col)
	return valid_locations

# This function finds the next available row in the given column (i.e., the first row from the bottom that is not already occupied).
def get_next_available_row(board, col):
    for row in range(TOTAL_ROW):
        if (board[row][col] == 0):
            return row

# This function sets the value of the given cell on the game board to the given piece (either COMPUTER or AGENT).
def drop_piece_in_board(board, row, col, piece, print = False):
    board[row][col] = piece
    if (piece == COMPUTER and print):
        # Draw a solid red circle
        pygame.draw.circle(screen, RED, (col * ShapeSize + ShapeSize / 2, (TOTAL_ROW - row) * ShapeSize + ShapeSize / 2), ShapeSize / 2 - 5)
    elif print:
        # Draw a solid blue circle
        pygame.draw.circle(screen, BLUE, (col * ShapeSize + ShapeSize / 2, (TOTAL_ROW - row) * ShapeSize + ShapeSize / 2), ShapeSize / 2 - 5)

# This function checks if the given player has won the game on the current board.
def check_winning_player(board, peice, print = False):
    # check horizontal wins
    for c in range(TOTAL_COLUMN-3):
        for r in range(TOTAL_ROW):
            if board[r][c] == peice and board[r][c+1] == peice and board[r][c+2] == peice and board[r][c+3] == peice:
                if (print):
                    pygame.draw.circle(screen, WHITE, (c * ShapeSize + ShapeSize / 2, (TOTAL_ROW-r) * ShapeSize + ShapeSize / 2), ShapeSize / 5)
                    pygame.draw.circle(screen, WHITE, ((c + 1) * ShapeSize + ShapeSize / 2, (TOTAL_ROW-r) * ShapeSize + ShapeSize / 2), ShapeSize / 5)
                    pygame.draw.circle(screen, WHITE, ((c + 2) * ShapeSize + ShapeSize / 2, (TOTAL_ROW-r) * ShapeSize + ShapeSize / 2), ShapeSize / 5)
                    pygame.draw.circle(screen, WHITE, ((c + 3) * ShapeSize + ShapeSize / 2, (TOTAL_ROW-r) * ShapeSize + ShapeSize / 2), ShapeSize / 5)
                return True
    # check vertical wins
    for c in range(TOTAL_COLUMN):
        for r in range(TOTAL_ROW-3):
            if board[r][c] == peice and board[r+1][c] == peice and board[r+2][c] == peice and board[r+3][c] == peice:
                if (print):
                    pygame.draw.circle(screen, WHITE, (c * ShapeSize + ShapeSize / 2, (TOTAL_ROW - r) * ShapeSize + ShapeSize / 2), ShapeSize / 5)
                    pygame.draw.circle(screen, WHITE, (c * ShapeSize + ShapeSize / 2, (TOTAL_ROW - (r + 1)) * ShapeSize + ShapeSize / 2), ShapeSize / 5)
                    pygame.draw.circle(screen, WHITE, (c * ShapeSize + ShapeSize / 2, (TOTAL_ROW - (r + 2)) * ShapeSize + ShapeSize / 2), ShapeSize / 5)
                    pygame.draw.circle(screen, WHITE, (c * ShapeSize + ShapeSize / 2, (TOTAL_ROW - (r + 3)) * ShapeSize + ShapeSize / 2), ShapeSize / 5)
                return True
    # Check diagonal / (bottom-left to top-right) wins
    for c in range(TOTAL_COLUMN-3):
        for r in range(TOTAL_ROW-3):
            if board[r][c] == peice and board[r+1][c+1] == peice and board[r+2][c+2] == peice and board[r+3][c+3] == peice:
                if (print):
                    pygame.draw.circle(screen, WHITE, (c * ShapeSize + ShapeSize / 2, (TOTAL_ROW - r) * ShapeSize + ShapeSize / 2), ShapeSize / 5)
                    pygame.draw.circle(screen, WHITE, ((c + 1) * ShapeSize + ShapeSize / 2, (TOTAL_ROW - (r + 1)) * ShapeSize + ShapeSize / 2), ShapeSize / 5)
                    pygame.draw.circle(screen, WHITE, ((c + 2) * ShapeSize + ShapeSize / 2, (TOTAL_ROW - (r + 2)) * ShapeSize + ShapeSize / 2), ShapeSize / 5)
                    pygame.draw.circle(screen, WHITE, ((c + 3) * ShapeSize + ShapeSize / 2, (TOTAL_ROW - (r + 3)) * ShapeSize + ShapeSize / 2), ShapeSize / 5)
                return True
    # Check diagonal \ (top-left to bottom-right) wins
    for c in range(TOTAL_COLUMN-3):
        for r in range(TOTAL_ROW-3):
            if board[r][c+3] == peice and board[r+1][c+2] == peice and board[r+2][c+1] == peice and board[r+3][c] == peice:
                if (print):
                    pygame.draw.circle(screen, WHITE, ((c + 3) * ShapeSize + ShapeSize / 2, (TOTAL_ROW - r) * ShapeSize + ShapeSize / 2), ShapeSize / 5)
                    pygame.draw.circle(screen, WHITE, ((c + 2) * ShapeSize + ShapeSize / 2, (TOTAL_ROW - (r + 1)) * ShapeSize + ShapeSize / 2), ShapeSize / 5)
                    pygame.draw.circle(screen, WHITE, ((c + 1) * ShapeSize + ShapeSize / 2, (TOTAL_ROW - (r + 2)) * ShapeSize + ShapeSize / 2), ShapeSize / 5)
                    pygame.draw.circle(screen, WHITE, (c * ShapeSize + ShapeSize / 2, (TOTAL_ROW - (r + 3)) * ShapeSize + ShapeSize / 2), ShapeSize / 5)
                return True
    return False

# Run until the user asks to quit
running = True

while running:
    # Did the user click the window close button? (X in the left top)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Done! Time to quit.
pygame.quit()