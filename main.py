import pygame
import sys
import numpy as np
import cores as cor
from vetor import vetor

pygame.init()

screen_h = 600
screen_w = 600
origem = np.array([screen_h/2, screen_w/2])

screen = pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption("Augusto - Modelagem grafica")

def desenhar_vetor(screen, origem, ponto, cor, texto):
    pygame.draw.line(screen, cor, origem, (origem[0] + ponto.x(), origem[1] + ponto.x()), 2)
    screen.blit(pygame.font.Font(None, 24).render(texto + "["+str(ponto.x()) +","+str(ponto.x())+"]", True, cor),(origem[0] + ponto.x(), origem[1] + ponto.x()))

def desenhar_grid(screen, color):
    for x in range (0, screen_w, 10):
        pygame.draw.line(screen, cor.PRETO,(x,0),(x,screen_h))
    for y in range (0, screen_h, 10):
        pygame.draw.line(screen, cor.PRETO,(0,y),(screen_w,y))

def desenhar_eixos(sreen, colorX, colorY):
    pygame.draw.line(screen, colorX,(0,screen_h/2),(screen_w,screen_h/2),3)
    pygame.draw.line(screen, colorY,(screen_w/2,0),(screen_w/2,screen_h),3)

#Execução
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(cor.BRANCO)
    
    desenhar_grid(screen, cor.PRETO)
    desenhar_eixos(screen,cor.PRETO,cor.PRETO)

    desenhar_vetor(screen, origem, vetor(100,100),cor.VERMELHO,"Vetor A")

    pygame.display.flip()

pygame.quit()
sys.exit()