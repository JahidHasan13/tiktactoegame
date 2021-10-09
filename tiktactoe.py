import numpy as np
import pygame
import sys

# start pygame
pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 10
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15

# RGB color
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCLE_COLOR = (239, 231, 200)
CROSS_WIDTH = 25
SPACE = 35
CROSS_COLOR = (66, 66, 66)
# ins,, the screen

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)

# pygame.draw.line(screen, LINE_COLOR, (10, 10), (300, 300), LINE_WIDTH)
# board
board = np.zeros((BOARD_ROWS, BOARD_COLS))


# print(board)


def draw_line():
    # 1 horizontal line
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    # 2nd line
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    # 3rd line
    pygame.draw.line(screen, LINE_COLOR, (0, 600), (600, 600), LINE_WIDTH)
    # 1st vertical line
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    # 2nd line
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)


draw_line()
player = 1
game_over = False


def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(
                    screen, CIRCLE_COLOR, (int(col * 200 + 100),
                                           int(row * 200 + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(
                    screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + 200 - SPACE),
                    (col * 200 + 200 - SPACE, row * 200 + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + SPACE),
                                 (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_WIDTH)


def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True


def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    return board[row][col] == 0


def check_win(player):
    # vertical win check
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_horizontal_winning_line(col, player)
            return True
    # horanzontal win check

    for row in range(BOARD_ROWS):
        if board[0][row] == player and board[1][row] == player and board[2][row] == player:
            draw_horizontal_winning_line(row, player)
            return True
    # asc diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True
    # dcsc diagolan win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True
    return False


def draw_vertical_winning_line(col, player):
    # posX = col * 200 + 100
    posY = col * 200 + 100
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (posY, 15), (posY, HEIGHT - 15), 15)


def draw_horizontal_winning_line(row, player):

    posX = row * 200 + 100
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    # pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), 15)
    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), 15)


def draw_asc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)


def draw_desc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)


def restart():
    screen.fill(BG_COLOR)
    draw_line()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0

#  main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0]  # X
            mouseY = event.pos[1]  # Y
            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)
            # print(clicked_row)
            # print(clicked_col)

            if available_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    if check_win(player):
                        game_over = True
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    if check_win(player):
                        game_over = True
                    player = 1
                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
            print(board)

    pygame.display.update()
