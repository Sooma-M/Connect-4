import pygame
import numpy
import math
import random

# initialize the pygame library
pygame.init()

# create the board initially by 0
TOTAL_ROW = 6
TOTAL_COLUMN = 7
board = numpy.zeros((TOTAL_ROW, TOTAL_COLUMN))

# how many pieces to win?
WIN_LENGTH = 4

game_over = False   # will be true if one player win
turn = 1            # to determine how is playing now
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

# This function checks if a given window of cells (i.e., a row, column, or diagonal) contains only the player's piece and is therefore a winning sequence.
def count_window_pieces(window, player):
    count = 0
    for i in range(WIN_LENGTH):
        if window[i] == player:
            count += 1
    return count

# This function count pieces for recent player and set score to him based on current pieces in the window.
def evaluate_window(window, piece):
    score = 0
    opp_piece = AGENT if piece == COMPUTER else COMPUTER

    pieceCount = count_window_pieces(window, piece)
    oopPieceCount = count_window_pieces(window, opp_piece)
    emptyCell = count_window_pieces(window, 0)

    if pieceCount == 4:
        score += 100
    elif pieceCount == 3 and emptyCell == 1:
        score += 10
    elif pieceCount == 2 and emptyCell == 2:
        score += 1
    elif oopPieceCount == 4:
        score -= 100
    elif oopPieceCount == 3 and emptyCell == 1:
        score -= 10
    elif oopPieceCount == 2 and emptyCell == 2:
        score -= 1

    return score


# Evaluate the score for a given board state.
def score_position(board, piece):
    score = 0

    # Score center column
    mid_board = []
    for r in range(TOTAL_ROW):
        mid_board.append(int(board[r][TOTAL_COLUMN // 2]))
    mid_count = mid_board.count(piece)
    score += (mid_count * 3)

    # Score Horizontal
    for r in range(TOTAL_ROW):
        for c in range(TOTAL_COLUMN - 3):
            window = []
            for i in range(WIN_LENGTH):
                window.append(int(board[r][c + i]))
            score += evaluate_window(window, piece)
    # Score Vertical
    for c in range(TOTAL_COLUMN):
        for r in range(TOTAL_ROW - 3):
            window = []
            for i in range(WIN_LENGTH):
                window.append(int(board[r + i][c]))
            score += evaluate_window(window, piece)
    # score for diagonal / (top-left to bottom-right)
    for r in range(TOTAL_ROW - 3):
        for c in range(TOTAL_COLUMN - 3):
            window = []
            for i in range(WIN_LENGTH):
                window.append(int(board[r + i][c + i]))
            score += evaluate_window(window, piece)
    # score for diagonal \ (bottom-left to top-right)
    for r in range(TOTAL_ROW - 3):
        for c in range(TOTAL_COLUMN - 3):
            window = []
            for i in range(WIN_LENGTH):
                window.append(int(board[r + 3 - i][c + i]))
            score += evaluate_window(window, piece)
    #print(score)
    return score

WIN_CNT = 10000000000000000
LOS_CNT = -10000000000000000
def AI_Algorithm(board, depth, maximizingPlayer, alpha = -math.inf, beta = math.inf, AlphaBetaFlag = False):
    # get all possible position valid to drop piece
    valid_locations = get_all_valid_locations(board)

    # check if current node is end of the game
    # if agent winning end the game
    if check_winning_player(board, AGENT):
        return None, WIN_CNT
    # if computer winning end the game
    elif check_winning_player(board, COMPUTER):
        return None, LOS_CNT
    # Game is over, no more valid moves
    elif len(get_all_valid_locations(board)) == 0:
        return None, 0
    # Force stop : Depth is zero
    elif depth == 0:
        return None, score_position(board, AGENT)

    # check if the current player want to maximize
    if maximizingPlayer:
        # get minimum score and random position as initial value
        current_score = -math.inf
        column = [random.choice(valid_locations)]

        # check the possible cols to add new piece
        for col in valid_locations:
            row = get_next_available_row(board, col)

            # simulate as we drop the piece and check board score after it
            board_copy = board.copy()
            drop_piece_in_board(board_copy, row, col, AGENT)
            new_score = AI_Algorithm(board_copy, depth - 1, False, alpha, beta, AlphaBetaFlag)[1]

            # update the value
            #if new_score == current_score:
                # print('max', new_score)
            #    column.append(col)

            if new_score > current_score:
                current_score = new_score
                column = [col]

            # if we use alpha beta instead of minimax it's will help instead of repeat the code
            if AlphaBetaFlag:
                alpha = max(alpha, current_score)
                if alpha >= beta:
                    break

        #print(column)
        return random.choice(column), current_score

    # Minimizing player
    else:
        # get maximum score and random position as initial value
        current_score = math.inf
        column = [random.choice(valid_locations)]

        # check the possible cols to add new piece
        for col in valid_locations:
            row = get_next_available_row(board, col)

            # simulate as we drop the piece and check board score after it
            board_copy = board.copy()
            drop_piece_in_board(board_copy, row, col, COMPUTER)
            new_score = AI_Algorithm(board_copy, depth - 1, True, alpha, beta, AlphaBetaFlag)[1]

            # update the value
            #if new_score == current_score:
                # print('min', new_score)
                #column.append(col)

            if new_score < current_score:
                current_score = new_score
                column = [col]

            # if we use alpha beta instead of minimax it's will help instead of repeat the code
            if AlphaBetaFlag:
                beta = min(beta, current_score)
                if alpha >= beta:
                    break
        #print(column)
        return random.choice(column), current_score

def play(board, col, piece):
    if (check_current_valid_location(board, col)):
        row = get_next_available_row(board, col)
        drop_piece_in_board(board, row, col, piece, True)
        return True

def minimax(board, player, level):
    if level == 'easy':
        if player == AGENT:
            return AI_Algorithm(board, 2, True)[0]
        else:
            return AI_Algorithm(board, 2, False)[0]
    elif level == 'medium':
        if player == AGENT:
            return AI_Algorithm(board, 3, True)[0]
        else:
            return AI_Algorithm(board, 3, False)[0]
    else:
        if player == AGENT:
            return AI_Algorithm(board, 4, True)[0]
        else:
            return AI_Algorithm(board, 4, False)[0]

def alpha_beta(board, player, level):
    if level == 'easy':
        if player == AGENT:
            return AI_Algorithm(board, 2, True, -math.inf, math.inf, True)[0]
        else:
            return AI_Algorithm(board, 2, False, -math.inf, math.inf, True)[0]
    elif level == 'medium':
        if player == AGENT:
            return AI_Algorithm(board, 3, True, -math.inf, math.inf, True)[0]
        else:
            return AI_Algorithm(board, 3, False, -math.inf, math.inf, True)[0]
    else:
        if player == AGENT:
            return AI_Algorithm(board, 5, True, -math.inf, math.inf, True)[0]
        else:
            return AI_Algorithm(board, 5, False, -math.inf, math.inf, True)[0]

def draw_board():
    for col in range(TOTAL_COLUMN):
        for row in range(TOTAL_ROW):
            # Draw a solid yellow rectangle
            pygame.draw.rect(screen, YELLOW, pygame.Rect(col * ShapeSize, (TOTAL_ROW - row) * ShapeSize, ShapeSize, ShapeSize))
            # Draw a solid white circle
            pygame.draw.circle(screen, WHITE, (col * ShapeSize + ShapeSize / 2, (TOTAL_ROW - row) * ShapeSize + ShapeSize / 2), ShapeSize / 2 - 5)
    pygame.display.update()


# Run until the user asks to quit
running = True

# initial value for playing mode
computer_play_mode = 'minimax'
agent_play_mode = 'minimax'

# choose playing mode
screen.fill(WHITE)
text = font.render("Choose for Computer", True, BLACK)
screen.blit(text, ((WIDTH - text.get_width()) // 2, ((HEIGHT - text.get_height()) // 2) - 50))

pygame.draw.rect(screen, BLACK, pygame.Rect(50, 350, 250, 100), False, 10)
text = font.render("Minimax", True, WHITE)
screen.blit(text, ((50*2 + 250 - text.get_width()) // 2, 355))
pygame.draw.rect(screen, BLACK, pygame.Rect(350, 350, 300, 100), False, 10)
text = font.render("Alpha-Beta", True, WHITE)
screen.blit(text, ((350*2 + 300 - text.get_width()) // 2, 355))
pygame.display.update()

while running:
    mode = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            position_x = event.pos[0]  # take x-axis position
            position_y = event.pos[1]  # take y-axis position
            #print(event.pos[0], event.pos[1])
            # computer
            if (position_y >= 350 and position_y <= 450):
                if (position_x >= 50 and position_x <= 300):
                    computer_play_mode = 'minimax'
                elif (position_x >= 350 and position_x <= 650):
                    computer_play_mode = 'alpha-beta'
                else:
                    continue
                mode = True
                break
    if mode:
        break

if running:
    # choose playing mode
    screen.fill(WHITE)
    text = font.render("Choose for Agent", True, BLACK)
    screen.blit(text, ((WIDTH - text.get_width()) // 2, ((HEIGHT - text.get_height()) // 2) - 50))

    pygame.draw.rect(screen, BLACK, pygame.Rect(50, 350, 250, 100), False, 10)
    text = font.render("Minimax", True, WHITE)
    screen.blit(text, ((50*2 + 250 - text.get_width()) // 2, 355))
    pygame.draw.rect(screen, BLACK, pygame.Rect(350, 350, 300, 100), False, 10)
    text = font.render("Alpha-Beta", True, WHITE)
    screen.blit(text, ((350*2 + 300 - text.get_width()) // 2, 355))
    pygame.display.update()

while running:
    mode = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            position_x = event.pos[0]  # take x-axis position
            position_y = event.pos[1]  # take y-axis position
            #print(event.pos[0], event.pos[1])
            # computer
            if (position_y >= 350 and position_y <= 450):
                if (position_x >= 50 and position_x <= 300):
                    agent_play_mode = 'minimax'
                elif (position_x >= 350 and position_x <= 650):
                    agent_play_mode = 'alpha-beta'
                else:
                    continue
                mode = True
                break
    if mode:
        break

# Fill the background with white (default is black)
if running:
    screen.fill(WHITE)
    text = font.render("Choose level of difficult", True, BLACK)
    screen.blit(text, ((WIDTH - text.get_width()) // 2, 10))
    text = font.render("Computer", True, BLACK)
    screen.blit(text, ((100 + 250 - text.get_width()) // 2, 100))
    text = font.render("Agent", True, BLACK)
    screen.blit(text, ((800 + 250 - text.get_width()) // 2, 100))
def levels(x):
    # Draw a solid GREEN rectangle (Easy)
    pygame.draw.rect(screen, GREEN, pygame.Rect(x, 200, 250, 100), False, 10)  # screen, color, (x y - |), radius, round corner
    text = font.render("Easy", True, WHITE)
    screen.blit(text, (((x*2 + 250) - text.get_width()) // 2, 205))
    # Draw a solid YELLOW rectangle (Medium)
    pygame.draw.rect(screen, YELLOW, pygame.Rect(x, 350, 250, 100), False, 10)
    text = font.render("Medium", True, WHITE)
    screen.blit(text, (((x*2 + 250) - text.get_width()) // 2, 355))
    # Draw a solid RED rectangle (HARD)
    pygame.draw.rect(screen, RED, pygame.Rect(x, 500, 250, 100), False, 10)
    text = font.render("Hard", True, WHITE)
    screen.blit(text, (((x*2 + 250) - text.get_width()) // 2, 505))
    pygame.display.update()

if running:
    # Choose Level
    computer_mode = 'easy'
    mode1 = True
    levels(50)
    agent_mode = 'easy'
    mode2 = True
    levels(400)
    # Done click
    pygame.draw.rect(screen, BLACK, pygame.Rect(220, 620, 250, 70), False, 10)
    text = font.render("Done", True, WHITE)
    screen.blit(text, ((440+250 - text.get_width()) // 2, 615))
    pygame.display.update()

while running:
    mode = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            position_x = event.pos[0]  # take x-axis position
            position_y = event.pos[1]  # take y-axis position
            # print(event.pos[0], event.pos[1])
            # computer
            if (position_x >= 50 and position_x <= 300):
                if (position_y >= 200 and position_y <= 300):
                    levels(50)
                    pygame.draw.rect(screen, BLACK, pygame.Rect(50, 200, 250, 100), False, 10)
                    text = font.render("Easy", True, WHITE)
                    screen.blit(text, ((350 - text.get_width()) // 2, 205))
                    computer_mode = 'easy'
                elif (position_y >= 350 and position_y <= 450):
                    levels(50)
                    pygame.draw.rect(screen, BLACK, pygame.Rect(50, 350, 250, 100), False, 10)
                    text = font.render("Medium", True, WHITE)
                    screen.blit(text, ((350 - text.get_width()) // 2, 355))
                    computer_mode = 'medium'
                elif (position_y >= 500 and position_y <= 600):
                    levels(50)
                    pygame.draw.rect(screen, BLACK, pygame.Rect(50, 500, 250, 100), False, 10)
                    text = font.render("Hard", True, WHITE)
                    screen.blit(text, ((350 - text.get_width()) // 2, 505))
                    computer_mode = 'hard'
                else:
                    continue
                pygame.display.update()
                mode1 = False
                break
            # agent
            elif (position_x >= 400 and position_x <= 650):
                if (position_y >= 200 and position_y <= 300):
                    levels(400)
                    pygame.draw.rect(screen, BLACK, pygame.Rect(400, 200, 250, 100), False, 10)
                    text = font.render("Easy", True, WHITE)
                    screen.blit(text, ((800 + 250 - text.get_width()) // 2, 205))
                    agent_mode = 'easy'
                elif (position_y >= 350 and position_y <= 450):
                    levels(400)
                    pygame.draw.rect(screen, BLACK, pygame.Rect(400, 350, 250, 100), False, 10)
                    text = font.render("Medium", True, WHITE)
                    screen.blit(text, ((800 + 250 - text.get_width()) // 2, 355))
                    agent_mode = 'medium'
                elif (position_y >= 500 and position_y <= 600):
                    levels(400)
                    pygame.draw.rect(screen, BLACK, pygame.Rect(400, 500, 250, 100), False, 10)
                    text = font.render("Hard", True, WHITE)
                    screen.blit(text, ((800 + 250 - text.get_width()) // 2, 505))
                    agent_mode = 'hard'
                else:
                    continue
                pygame.display.update()
                mode2 = False
                break
            elif (position_x >= 220 and position_x <= 470) and (position_y >= 620 and position_y <= 690):
                if not mode1 and not mode2:
                    mode = True
    if mode:
        break


if running:
    # Fill again the background with white (default is black)
    screen.fill(WHITE)
    draw_board()  # Draw Board
    pygame.draw.rect(screen, WHITE, pygame.Rect(0, 0, WIDTH, ShapeSize))
    text = font.render("Computer Turn (RED)", True, RED)
    screen.blit(text, ((WIDTH - text.get_width()) // 2, 10))
    pygame.display.update()

while running:
    # Did the user click the window close button? (X in the left top)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if turn == COMPUTER and not game_over:
        selection = minimax(board, COMPUTER, computer_mode) if computer_play_mode == 'minimax' else alpha_beta(board, COMPUTER, computer_mode)
        if (play(board, selection, COMPUTER)):
            if computer_mode != 'hard':
                pygame.time.wait(500)
            else:
                pygame.time.wait(200)
            if check_winning_player(board, COMPUTER, True):
                pygame.draw.rect(screen, WHITE, pygame.Rect(0, 0, WIDTH, ShapeSize))
                text = "Computer Win !"
                color = RED
                text = font.render(text, True, color)
                screen.blit(text, ((WIDTH - text.get_width()) // 2, 10))
                game_over = True
            else:
                turn = AGENT
                text = "Agent Turn (BLUE)"
                color = BLUE
                pygame.draw.rect(screen, WHITE, pygame.Rect(0, 0, WIDTH, ShapeSize))
                text = font.render(text, True, color)
                screen.blit(text, ((WIDTH - text.get_width()) // 2, 10))
            pygame.display.update()


    if turn == AGENT and not game_over:
        selection = minimax(board, AGENT, agent_mode) if agent_play_mode == 'minimax' else alpha_beta(board, AGENT, agent_mode)

        if (play(board, selection, AGENT)):
            if agent_mode != 'hard':
                pygame.time.wait(500)
            else:
                pygame.time.wait(200)
            if check_winning_player(board, AGENT, True):
                pygame.draw.rect(screen, WHITE, pygame.Rect(0, 0, WIDTH, ShapeSize))
                text = "Agent Win !"
                color = BLUE
                text = font.render(text, True, color)
                screen.blit(text, ((WIDTH - text.get_width()) // 2, 10))
                game_over = True
            else:
                turn = COMPUTER
                text = "Computer Turn (RED)"
                color = RED
                pygame.draw.rect(screen, WHITE, pygame.Rect(0, 0, WIDTH, ShapeSize))
                text = font.render(text, True, color)
                screen.blit(text, ((WIDTH - text.get_width()) // 2, 10))
            pygame.display.update()

    # check if there is any valid location (game end if no one win but cannot play anymore)
    if len(get_all_valid_locations(board)) == 0 and not game_over:
        pygame.draw.rect(screen, WHITE, pygame.Rect(0, 0, WIDTH, ShapeSize))
        text = font.render("Game Over", True, BLACK)
        screen.blit(text, ((WIDTH - text.get_width()) // 2, 10))
        pygame.display.update()
        game_over = True

    if game_over:
        text = font.render("Exit after 3 seconds...", True, BLACK)
        screen.blit(text, ((WIDTH - text.get_width()) // 2, (HEIGHT - text.get_height()) // 2))
        pygame.display.update()
        pygame.time.wait(3000)
        break

# Done! Time to quit.
pygame.quit()