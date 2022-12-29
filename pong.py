import pygame
from pygame.locals import *
from OpenGL.GL import *

larg_j = 640
alt_j = 480

X_bola = 0
Y_bola = 0
Tan_Bola = 20
V_Bola_x = 0.1
V_Bola_y = 0.1

Y_Jogador1 = 0
Y_Jogador2 = 0


def x_jogador1():
    return -larg_j / 2 + larg_jogadores() / 2


def x_jogador2():
    return larg_j / 2 - larg_jogadores() / 2


def larg_jogadores():
    return Tan_Bola


def alt_jogadores():
    return 3 * Tan_Bola


def atualizar():
    global X_bola, Y_bola, V_Bola_x, V_Bola_y, Y_Jogador1, Y_Jogador2

    X_bola = X_bola + V_Bola_x
    Y_bola = Y_bola + V_Bola_y

    if (X_bola + Tan_Bola / 2 > x_jogador2() - larg_jogadores() / 2
            and Y_bola - Tan_Bola / 2 < Y_Jogador2 + alt_jogadores() / 2
            and Y_bola + Tan_Bola / 2 > Y_Jogador2 - alt_jogadores() / 2):
        V_Bola_x = -V_Bola_x

    if (X_bola - Tan_Bola / 2 < x_jogador1() + larg_jogadores() / 2
            and Y_bola - Tan_Bola / 2 < Y_Jogador1 + alt_jogadores() / 2
            and Y_bola + Tan_Bola / 2 > Y_Jogador1 - alt_jogadores() / 2):
        V_Bola_x = -V_Bola_x

    if Y_bola + Tan_Bola / 2 > alt_j / 2:
        V_Bola_y = -V_Bola_y

    if Y_bola - Tan_Bola / 2 < -alt_j / 2:
        V_Bola_y = -V_Bola_y

    if X_bola < -larg_j / 2 or X_bola > larg_j / 2:
        X_bola = 0
        Y_bola = 0

    keys = pygame.key.get_pressed()

    if keys[K_w]:
        Y_Jogador1 = Y_Jogador1 + 0.2

    if keys[K_s]:
        Y_Jogador1 = Y_Jogador1 - 0.2

    if keys[K_UP]:
        Y_Jogador2 = Y_Jogador2 + 0.2

    if keys[K_DOWN]:
        Y_Jogador2 = Y_Jogador2 - 0.2


def desenhar_rec(x_, y, larg, alt, r, g, b):
    glColor(r, g, b)

    glBegin(GL_QUADS)
    glVertex2f(-0.5 * larg + x_, -0.5 * alt + y)
    glVertex2f(0.5 * larg + x_, -0.5 * alt + y)
    glVertex2f(0.5 * larg + x_, 0.5 * alt + y)
    glVertex2f(-0.5 * larg + x_, 0.5 * alt + y)
    glEnd()


def desenhar():
    glViewport(0, 0, larg_j, alt_j)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-larg_j / 2, larg_j / 2, -alt_j / 2, alt_j / 2, 0, 1)

    glClear(GL_COLOR_BUFFER_BIT)

    desenhar_rec(X_bola, Y_bola, Tan_Bola, Tan_Bola, 1, 1, 0)
    desenhar_rec(x_jogador1(), Y_Jogador1, larg_jogadores(), alt_jogadores(), 1, 0, 0)
    desenhar_rec(x_jogador2(), Y_Jogador2, larg_jogadores(), alt_jogadores(), 0, 0, 1)

    pygame.display.flip()


pygame.init()
pygame.display.set_mode((larg_j, alt_j), DOUBLEBUF | OPENGL)

while True:
    atualizar()
    desenhar()
    pygame.event.pump()
