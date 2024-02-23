import pygame
import tinline_bot as bot
import tinline_datareader as dr

import tkinter as tk
resolution_screen = tk.Tk()
sx = int(resolution_screen.winfo_screenwidth()*.7)
sy = int(resolution_screen.winfo_screenheight()*.7)
    
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((sx, sy))
pygame.display.set_caption("tic tac toe.")
pygame.mouse.get_visible

import os
direc = os.path.dirname(os.path.abspath(__file__)).replace('\'', '/')
def symb(txt, x, y, size, colour):
    try:
        font = pygame.font.Font(f"{direc}/CONSOLA.TTF", int(size))
    except:
        font = pygame.font.Font(None, int(size))
    img = font.render(str(txt), True, colour)
    rect = img.get_rect(center = (x,y))
    screen.blit(img, rect)

turn = 0
board = [[2 for y in range(3)] for x in range(3)]
wins = 3
u = int(sy/6)

def win(position):
    # 0 gana X, 1 gana O, 2 empate, 3 sigue en juego
    
    d = (((0,0), (1,1), (2,2)), ((2,0), (1,1), (0,2)))
    h = tuple(tuple((x,y) for y in range(3)) for x in range(3))
    v = tuple(tuple((x,y) for x in range(3)) for y in range(3))
    for i in [*d, *h, *v]:
        if position[i[0][0]][i[0][1]] == position[i[1][0]][i[1][1]] == position[i[2][0]][i[2][1]] == 1 or \
           position[i[0][0]][i[0][1]] == position[i[1][0]][i[1][1]] == position[i[2][0]][i[2][1]] == 0:
            return position[i[0][0]][i[0][1]]
    
    for x in range(3):
        for y in range(3):
            if position[x][y] == 2:
                return 3
    return 2
n=0
while True:
    n+=1
    screen.fill(tuple(20 for x in range(3)))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.dict["button"] and wins == 3 and turn == 0:
            mouse_pos = pygame.mouse.get_pos()
            for x in range(3):
                for y in range(3):
                    xx = sx/2 + (u*(x-1.5))
                    yy = u*(y+1.5)
                    if xx < mouse_pos[0] < xx+u and yy < mouse_pos[1] < yy+u and board[x][y] == 2 :
                        board[x][y] = turn
                        turn = abs(turn-1)
            n=0
                                     
    pygame.draw.rect(screen, tuple(50 for x in range(3)), (int((sx-u*3)/2 - u*.25), u*1.25, u*3.5, u*3.5), 0, int(u/2))
    for x in range(3):
        for y in range(3):
            if board[x][y] == 0:
                symb("x", int(sx/2 + (u*(x-1))), int(u*(y+2)), u, "white")
            elif board[x][y] == 1:
                symb("o", int(sx/2 + (u*(x-1))), int(u*(y+2)), u, "white")
            elif board[x][y] == 2:
                symb("_", int(sx/2 + (u*(x-1))), int(u*(y+2)), u, "white")
    
    wins = win(board)
    match wins:
        case 0: 
            symb("x wins (player)", int(sx/2), int(u*.75), u/2, "white")
        case 1: 
            symb("o wins (bot)", int(sx/2), int(u*.75), u/2, "white")
        case 2: 
            symb("tie", int(sx/2), int(u*.75), u/2, "white")
        case 3: 
            if turn == 0:
                symb("x to play (player)", int(sx/2), int(u*5.25), u/2, "white")
            elif turn == 1:
                symb("o to play (bot)", int(sx/2), int(u*5.25), u/2, "white")
            
    if n == 60 and turn == 1 and wins == 3:
        # coord = bot.minimax([y for x in board for y in x], turn)[1]
        coord = dr.main(board, turn)
        coord = coord//3, coord%3
        board[coord[0]][coord[1]] = turn
        turn = abs(turn-1)

    pygame.display.update()
    clock.tick(60)