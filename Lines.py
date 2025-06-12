import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Utils import *

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Plotting Lines w/ Mouse')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 640, 0, 480)


def plot_line():
    for l in points:
        glBegin(GL_LINE_STRIP)
        for coords in l:
            glVertex2f(coords[0], coords[1])
        glEnd()


points = []
line = []

init_ortho()

glPointSize(5)

mouse_down = False
done = False

while not done:
    p = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            mouse_down = True
            line = []
            points.append(line)
        elif event.type == MOUSEBUTTONUP:
            mouse_down = False
        elif event.type == MOUSEMOTION and mouse_down:
            p = pygame.mouse.get_pos()
            line.append((map_value(0, screen_width, 0, 640, p[0]),
                         map_value(0, screen_height, 480, 0, p[1])))

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    plot_line()

    pygame.display.flip()
    # pygame.time.wait(100)

pygame.quit()
