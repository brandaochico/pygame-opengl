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
pygame.display.set_caption('Simple Paint!')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(ortho_left, ortho_right, ortho_top, ortho_bottom)


def plot_line():
    for l in points:
        glBegin(GL_LINE_STRIP)
        for coords in l:
            glVertex2f(coords[0], coords[1])
        glEnd()


def plot_graph():
    glBegin(GL_LINE_STRIP)
    px: GL_DOUBLE
    py: GL_DOUBLE

    for px in np.arange(0, 4, 0.005):
        py = math.exp(-px) * math.cos(2 * math.pi * px)
        glVertex2f(px, py)

    glEnd()


def save_drawing():
    file = open('drawing.txt', 'w')
    file.write(str(len(points)) + '\n')

    for line in points:
        file.write(str(len(line)) + '\n')
        for coords in line:
            file.write(str(coords[0]) + ' ' + str(coords[1]) + '\n')

    file.close()
    print('Drawing saved!')


def load_drawing():
    file = open('drawing.txt', 'r')
    n_lines = int(file.readline())

    global points
    global line
    points = []

    for l in range(n_lines):
        line = []
        points.append(line)
        n_coords = int(file.readline())
        for coord in range(n_coords):
            px, py = [float(value) for value in next(file).split()]
            line.append((px, py))
            print(str(px) + ',' + str(py))


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

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                save_drawing()
            if event.key == pygame.K_l:
                load_drawing()
            if event.key == pygame.K_SPACE:
                points = []

        elif event.type == MOUSEBUTTONDOWN:
            mouse_down = True
            line = []
            points.append(line)
        elif event.type == MOUSEBUTTONUP:
            mouse_down = False
        elif event.type == MOUSEMOTION and mouse_down:
            p = pygame.mouse.get_pos()
            line.append((map_value(0, screen_width, ortho_left, ortho_right, p[0]),
                         map_value(0, screen_height, ortho_bottom, ortho_top, p[1])))

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    plot_line()

    pygame.display.flip()
    # pygame.time.wait(100)

pygame.quit()
