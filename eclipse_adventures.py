import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
FPS = 60

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)
pygame.display.set_caption("3D Solar System Simulation")

# Initialize OpenGL
glMatrixMode(GL_PROJECTION)
gluPerspective(45, (WIDTH / HEIGHT), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
gluLookAt(0, -10, 3, 0, 0, 0, 0, 0, 1)

# Colors
WHITE = (1, 1, 1)
YELLOW = (1, 1, 0)
BLUE = (0, 0, 1)

# Function to draw a sphere
def draw_sphere(radius, slices, stacks):
    quad = gluNewQuadric()
    gluQuadricNormals(quad, GLU_SMOOTH)
    gluQuadricTexture(quad, GL_TRUE)
    gluSphere(quad, radius, slices, stacks)

# Main game loop
clock = pygame.time.Clock()
angle = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Draw Sun
    glColor3fv(YELLOW)
    draw_sphere(1, 100, 100)

    # Draw Earth
    glPushMatrix()
    glRotatef(angle, 0, 0, 1)
    glTranslatef(3, 0, 0)
    glColor3fv(BLUE)
    draw_sphere(0.2, 100, 100)
    glPopMatrix()

    # Draw Moon
    glPushMatrix()
    glRotatef(angle * 5, 0, 0, 1)
    glTranslatef(3.5, 0, 0)
    glColor3fv(WHITE)
    draw_sphere(0.05, 100, 100)
    glPopMatrix()

    pygame.display.flip()
    clock.tick(FPS)
    angle += 0.5