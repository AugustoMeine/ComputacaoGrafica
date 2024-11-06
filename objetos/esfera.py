from OpenGL.GL import *
from OpenGL.GLU import *

def desenhar_esfera():
    glLoadIdentity()
    glPushMatrix()
    glTranslatef(2.5, 1.0, -12.0)
    glBindTexture(GL_TEXTURE_2D, 1)
    textured_sphere = gluNewQuadric()
    gluQuadricTexture(textured_sphere, GL_TRUE)
    gluSphere(textured_sphere, 2, 32, 32)
    glPopMatrix()