import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("OpenGL in Python")

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 640, 0, 480)

def draw_star(x, y, size):
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2i(x,y)
    glEnd()

done = False
init_ortho()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    draw_star(370, 50, 10)
    draw_star(360, 80, 10)
    draw_star(375, 90, 10)
    draw_star(500, 220, 5)
    draw_star(470, 340, 7)
    draw_star(315, 410, 10)
    draw_star(280, 290, 5)
    draw_star(250, 250, 5)
    draw_star(220, 270, 6)

    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()
