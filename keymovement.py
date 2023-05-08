import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
display = (640, 480)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

gluPerspective(90, (display[0] / display[1]), 0.1, 50.0)

# Coordenadas do quadrado
x = 0.0
y = 0.0


def draw_square():
    glBegin(GL_QUADS)
    glVertex3f(0, 0, 0.0)
    glVertex3f(1, 0, 0.0)
    glVertex3f(1, 1, 0.0)
    glVertex3f(0, 1, 0.0)
    glEnd()


def draw_retangle():
    glBegin(GL_QUADS)
    glVertex3f(x, y, 0.0)
    glVertex3f(x + 0.2, y, 0.0)
    glVertex3f(x + 0.2, y + 1.0, 0.0)
    glVertex3f(x, y + 1.0, 0.0)
    glEnd()


moving_left = False
moving_right = False
moving_up = False
moving_down = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            elif event.key == pygame.K_RIGHT:
                moving_right = True
            elif event.key == pygame.K_UP:
                moving_up = True
            elif event.key == pygame.K_DOWN:
                moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            elif event.key == pygame.K_RIGHT:
                moving_right = False
            elif event.key == pygame.K_UP:
                moving_up = False
            elif event.key == pygame.K_DOWN:
                moving_down = False

    if moving_left:
        x -= 0.02
    if moving_right:
        x += 0.02
    if moving_up:
        y += 0.02
    if moving_down:
        y -= 0.02

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Configura a matriz MVP
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90, (display[0] / display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

    # Configura a matriz MVP
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90, (display[0] / display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 3, 0, 0, 0, 0, 1, 0)

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    draw_square()
    draw_retangle()

    pygame.display.flip()
    pygame.time.wait(10)
