from OpenGL.GL import *
from OpenGL.GLU import *

def desenhar_cubo():
    
    glLoadIdentity()
    glTranslatef(-1.5, 0.0, -7.0)
    glRotatef(0, 1.0, 1.0, 1.0)

    glBindTexture(GL_TEXTURE_2D, 1)  # Vincula a textura
    glBegin(GL_QUADS)
    
    # Topo
    glNormal3f(0.0, 1.0, 0.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, 1.0, 1.0)

    # Base
    glNormal3f(0.0, -1.0, 0.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)

    # Frente
    glNormal3f(0.0, 0.0, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, -1.0, 1.0)

    # Traseira
    glNormal3f(0.0, 0.0, -1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, 1.0, -1.0)

    # Esquerda
    glNormal3f(-1.0, 0.0, 0.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, -1.0, 1.0)

    # Direita
    glNormal3f(1.0, 0.0, 0.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0, -1.0, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)
    
    glEnd()