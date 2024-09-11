import pygame
import sys
import numpy as np
import cores as cor
#from vetor import vetor

pygame.init()

tela_largura, tela_altura = 1080,720
origem = np.array([tela_largura/2, tela_altura/2])
print(origem)
tela = pygame.display.set_mode((tela_largura,tela_altura))

pygame.display.set_caption("Augusto - Modelagem grafica")

def desenhar_vetor(tela, origem, vetor, cor, texto):
    pygame.draw.line(tela, cor, origem, np.add(origem,vetor), 2)
    tela.blit(pygame.font.Font(None, 24).render(texto + "["+str(vetor[0]) +","+str(vetor[1])+"]", True, cor),np.add(vetor,origem))

def desenhar_grid(tela, color):
    for x in range (0, tela_largura, 10):
        pygame.draw.line(tela, cor.PRETO,(x,0),(x,tela_altura))
    for y in range (0, tela_altura, 10):
        pygame.draw.line(tela, cor.PRETO,(0,y),(tela_largura,y))

def desenhar_eixos(sreen, colorX, colorY):
    pygame.draw.line(tela, colorX,(0,tela_altura/2),(tela_largura,tela_altura/2),3)
    pygame.draw.line(tela, colorY,(tela_largura/2,0),(tela_largura/2,tela_altura),3)

vetor = np.array((100,200))

#Execução
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    tela.fill(cor.BRANCO)
    
    desenhar_grid(tela, cor.PRETO)
    desenhar_eixos(tela,cor.PRETO,cor.PRETO)
    desenhar_vetor(tela,origem,vetor,cor.VERMELHO,"Vetor A")

    pygame.display.flip()

pygame.quit()
sys.exit()