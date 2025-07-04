import math
import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Utils import *

pygame.init()

screen_width = 1000
screen_height = 800

ortho_left = 0
ortho_right = 4
ortho_top = -1
ortho_bottom = 1

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Plotting Graph w/ Lines')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(ortho_left, ortho_right, ortho_top, ortho_bottom)


def plot_graph():
    glBegin(GL_LINE_STRIP)
    px: GL_DOUBLE
    py: GL_DOUBLE

    for px in np.arange(0, 4, 0.005):
        py = math.exp(-px) * math.cos(2 * math.pi * px)
        glVertex2f(px, py)

    glEnd()


points = []

init_ortho()

glPointSize(5)

mouse_down = False
done = False

while not done:
    p = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    plot_graph()

    pygame.display.flip()
    # pygame.time.wait(100)

pygame.quit()
