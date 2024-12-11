import os
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

telaX = 0
telaY = 0
telaZ = -30
rotacaoX = 0
rotacaoY = -90
rotacaoZ = 0

def init():    
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, 1080.0 / 720.0, 0.1, 400.0)
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_NORMALIZE)

def carregar_textura(caminho_textura):
    texture_surface = pygame.image.load(os.path.join(os.path.dirname(__file__), caminho_textura))
    texture_data = pygame.image.tostring(texture_surface, "RGB", True)
    width, height = texture_surface.get_rect().size

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glEnable(GL_TEXTURE_2D)
    return texture_id

def calcular_rotacao(angulo, raio):
    rad = np.radians(angulo)
    x = raio * np.cos(rad)
    y = 0
    z = raio * np.sin(rad)
    return x, y, z

def desenhar_esfera(raio, textura_id):
    glBindTexture(GL_TEXTURE_2D, textura_id)
    quad = gluNewQuadric()
    gluQuadricTexture(quad, GL_TRUE)
    gluSphere(quad, raio, 40, 40)
    gluDeleteQuadric(quad)

def main():
    global telaX, telaY, telaZ, rotacaoX, rotacaoY, rotacaoZ
    pygame.init()
    pygame.display.set_mode((1080, 720), DOUBLEBUF | OPENGL)
    init()

    textura_terra = carregar_textura('objetos/texturas/terra.png')
    textura_sol = carregar_textura('objetos/texturas/sol.png')
    textura_planeta1 = carregar_textura('objetos/texturas/Planeta1.png')
    textura_planeta2 = carregar_textura('objetos/texturas/Planeta2.png')
    textura_planeta3 = carregar_textura('objetos/texturas/Planeta3.png')
    textura_planeta4 = carregar_textura('objetos/texturas/Planeta4.png')
    textura_planeta5 = carregar_textura('objetos/texturas/Planeta5.png')
    textura_planeta6 = carregar_textura('objetos/texturas/Planeta6.png')
    

    anguloTerra = 0
    anguloPlanetaUm = 0
    anguloPlanetaDois = 0
    anguloPlanetaTres = 0
    anguloPlanetaQuatro = 0
    anguloPlanetaCinco = 0
    anguloPlanetaSeis = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:                    
                    running = False
                elif event.key == K_w:
                    telaY += 1
                elif event.key == K_s:
                    telaY -= 1
                elif event.key == K_a:
                    telaX -= 1
                elif event.key == K_d:
                    telaX += 1
                elif event.key == K_UP:
                    rotacaoX += 5
                elif event.key == K_DOWN:
                    rotacaoX -= 5
                elif event.key == K_LEFT:
                    rotacaoY -= 5
                elif event.key == K_RIGHT:
                    rotacaoY += 5    
                elif event.key == K_q:
                    if(telaZ < -10):
                        telaZ += 5
                elif event.key == K_e:
                    telaZ -= 5           

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        rotacaoY += 0.5

        glPushMatrix()
        glTranslatef(telaX, telaY, telaZ)
        glScalef(2, 2, 2)
        glRotatef(rotacaoX, 1, 0, 0)
        glRotatef(rotacaoY, 0, 1, 0)
        glRotatef(rotacaoZ, 0, 0, 1)
        
        desenhar_esfera(2, textura_sol)
        glPopMatrix()

        anguloTerra += 1
        anguloPlanetaUm += 2
        anguloPlanetaDois += 3
        anguloPlanetaTres += 2
        anguloPlanetaQuatro += 1
        anguloPlanetaCinco += 3
        anguloPlanetaSeis += 2

        x, y, z = calcular_rotacao(anguloTerra, 6)
        glPushMatrix()
        glTranslatef(telaX + x, telaY + y, telaZ + z)
        glScalef(1, 1, 1)
        glRotatef(rotacaoX, 1, 0, 0)
        glRotatef(rotacaoY, 0, 1, 0)
        glRotatef(rotacaoZ, 0, 0, 1)
        
        desenhar_esfera(1, textura_terra)
        glPopMatrix()

        x, y, z = calcular_rotacao(anguloPlanetaUm, 8)
        glPushMatrix()
        glTranslatef(telaX + x, telaY + y, telaZ + z)
        glScalef(0.5, 0.5, 0.5)
        glRotatef(rotacaoX, 1, 0, 0)
        glRotatef(rotacaoY, 0, 1, 0)
        glRotatef(rotacaoZ, 0, 0, 1)
        
        desenhar_esfera(0.5, textura_planeta1)
        glPopMatrix()

        x, y, z = calcular_rotacao(anguloPlanetaDois, 10)
        glPushMatrix()
        glTranslatef(telaX + x, telaY + y, telaZ + z)
        glScalef(0.75, 0.75, 0.75)
        glRotatef(rotacaoX, 1, 0, 0)
        glRotatef(rotacaoY, 0, 1, 0)
        glRotatef(rotacaoZ, 0, 0, 1)
        
        desenhar_esfera(0.75, textura_planeta2)
        glPopMatrix()

        x, y, z = calcular_rotacao(anguloPlanetaTres, 12)
        glPushMatrix()
        glTranslatef(telaX + x, telaY + y, telaZ + z)
        glScalef(0.6, 0.6, 0.6)
        glRotatef(rotacaoX, 1, 0, 0)
        glRotatef(rotacaoY, 0, 1, 0)
        glRotatef(rotacaoZ, 0, 0, 1)
        
        desenhar_esfera(0.6, textura_planeta3)
        glPopMatrix()

        x, y, z = calcular_rotacao(anguloPlanetaQuatro, 14)
        glPushMatrix()
        glTranslatef(telaX + x, telaY + y, telaZ + z)
        glScalef(0.7, 0.7, 0.7)
        glRotatef(rotacaoX, 1, 0, 0)
        glRotatef(rotacaoY, 0, 1, 0)
        glRotatef(rotacaoZ, 0, 0, 1)
        
        desenhar_esfera(0.7, textura_planeta4)
        glPopMatrix()

        x, y, z = calcular_rotacao(anguloPlanetaCinco, 16)
        glPushMatrix()
        glTranslatef(telaX + x, telaY + y, telaZ + z)
        glScalef(0.8, 0.8, 0.8)
        glRotatef(rotacaoX, 1, 0, 0)
        glRotatef(rotacaoY, 0, 1, 0)
        glRotatef(rotacaoZ, 0, 0, 1)
        
        desenhar_esfera(0.8, textura_planeta5)
        glPopMatrix()

        x, y, z = calcular_rotacao(anguloPlanetaSeis, 18)
        glPushMatrix()
        glTranslatef(telaX + x, telaY + y, telaZ + z)
        glScalef(0.9, 0.9, 0.9)
        glRotatef(rotacaoX, 1, 0, 0)
        glRotatef(rotacaoY, 0, 1, 0)
        glRotatef(rotacaoZ, 0, 0, 1)
        
        desenhar_esfera(0.9, textura_planeta6)
        glPopMatrix()
        
        pygame.display.flip()
        pygame.time.wait(10)
        
    pygame.quit()

if __name__ == "__main__":
    main()