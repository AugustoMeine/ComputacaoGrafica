import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from objetos.esfera import desenhar_esfera
from objetos.cubo import desenhar_cubo
from objetos.arma import desenhar_pistola
from iluminacao.iluminacao_basica import iniciar_iluminacao
from OpenGL.GLUT import *

telaX = 0
telaY = 0
telaZ = -5
rotacaoX = 0
rotacaoY = 0
rotacaoZ = 0

def init():    
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, 640.0 / 480.0, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    global telaX, telaY, telaZ, rotacaoX, rotacaoY, rotacaoZ
    pygame.init()
    pygame.display.set_mode((640, 480), DOUBLEBUF | OPENGL)
    init()
    iniciar_iluminacao()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_w:
                    telaY += 0.1
                elif event.key == K_s:
                    telaY -= 0.1
                elif event.key == K_a:
                    telaX -= 0.1
                elif event.key == K_d:
                    telaX += 0.1
                elif event.key == K_UP:
                    rotacaoX += 5
                elif event.key == K_DOWN:
                    rotacaoX -= 5
                elif event.key == K_LEFT:
                    rotacaoY -= 5
                elif event.key == K_RIGHT:
                    rotacaoY += 5

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #materilal https://opengameart.org/content/desert-eagle-0
        #telaX, telaY, telaZ, rotacaoX, rotacaoY, rotacaoZ
        desenhar_pistola(telaX, telaY, telaZ, rotacaoX, rotacaoY, rotacaoZ)
        
        pygame.display.flip()
        pygame.time.wait(10)
        
    pygame.quit()

if __name__ == "__main__":
    main()