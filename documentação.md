### Documentação Resumida

#### Arquivo `main.py`

1. **Importações**
    ```python
    import os
    import pygame
    from pygame.locals import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
    import numpy as np
    from trimesh.exchange.load import load_mesh
    ```

    - `pygame`: Biblioteca para criação de jogos e manipulação de eventos.
    - `OpenGL.GL` e `OpenGL.GLU`: Bibliotecas para renderização 3D usando OpenGL.
    - `trimesh`: Biblioteca para manipulação de malhas 3D.
    - `numpy`: Biblioteca para operações matemáticas e manipulação de arrays.
    - `os`: Biblioteca para manipulação de caminhos de arquivos e diretórios.

2. **Variáveis Globais**
    ```python
    telaX = 0
    telaY = 0
    telaZ = -5
    rotacaoX = 0
    rotacaoY = 0
    rotacaoZ = 0
    ```

    - Variáveis para controlar a posição e rotação da câmera.

3. **Função `init`**
    - Configura o ambiente OpenGL para iniciar o ambiente 3D.
    ```python
    def init():    
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_NORMALIZE)
    ```

4. **Função `carregar_materiais`**
    - Carrega os materiais do arquivo MTL.
    ```python
    def carregar_materiais(nome_arquivo):
        materiais = {}
        material_atual = None
        diretorio_base = os.path.dirname(nome_arquivo)

        with open(nome_arquivo) as f:
            for line in f:
                if line.startswith('newmtl '):
                    material_atual = line.strip().split()[1]
                    materiais[material_atual] = {}
                elif material_atual:
                    if line.startswith('Kd '):
                        materiais[material_atual]['Kd'] = list(map(float, line.strip().split()[1:]))
                    elif line.startswith('Ka '):
                        materiais[material_atual]['Ka'] = list(map(float, line.strip().split()[1:]))
                    elif line.startswith('Ks '):
                        materiais[material_atual]['Ks'] = list(map(float, line.strip().split()[1:]))
                    elif line.startswith('Ns '):
                        materiais[material_atual]['Ns'] = float(line.strip().split()[1])
                    elif line.startswith('map_Kd '):
                        caminho_textura = os.path.join(diretorio_base, 'textures', line.strip().split()[1])
                        materiais[material_atual]['map_Kd'] = caminho_textura
        return materiais
    ```

5. **Função `carregar_textura`**
    - Carrega uma textura a partir de um arquivo PNG.
    ```python
    def carregar_textura(caminho_textura):
        texture_surface = pygame.image.load(caminho_textura)
        texture_data = pygame.image.tostring(texture_surface, "RGB", 1)
        width, height = texture_surface.get_rect().size

        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        return texture_id
    ```

6. **Função `calcular_rotacao`**
    - Calcula a posição dos planetas em rotação ao redor do Sol.
    ```python
    def calcular_rotacao(angulo, raio, eixo):
        rad = np.radians(angulo)
        if eixo == 'X':
            x = 0
            y = raio * np.cos(rad)
            z = raio * np.sin(rad)
        elif eixo == 'Y':
            x = raio * np.cos(rad)
            y = 0
            z = raio * np.sin(rad)
        elif eixo == 'Z':
            x = raio * np.cos(rad)
            y = raio * np.sin(rad)
            z = 0
        return x, y, z
    ```

7. **Função `desenhar_objeto_trimesh`**
    - Desenha um objeto 3D usando a biblioteca trimesh.
    ```python
    def desenhar_objeto_trimesh(mesh, materiais):
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_NORMAL_ARRAY)
        
        vertices = mesh.vertices.view(dtype=float)
        normais = mesh.vertex_normals.view(dtype=float)
        
        glVertexPointer(3, GL_FLOAT, 0, vertices)
        glNormalPointer(GL_FLOAT, 0, normais)
        
        if hasattr(mesh.visual, 'uv') and mesh.visual.uv is not None:
            glEnableClientState(GL_TEXTURE_COORD_ARRAY)
            texturas = mesh.visual.uv.view(dtype=float)
            glTexCoordPointer(2, GL_FLOAT, 0, texturas)
            
            for material_name, material in materiais.items():
                if 'map_Kd' in material:
                    caminho_textura = material['map_Kd']
                    texture_id = carregar_textura(caminho_textura)
                    glBindTexture(GL_TEXTURE_2D, texture_id)
                    glEnable(GL_TEXTURE_2D)
                else:
                    glDisable(GL_TEXTURE_2D)
        
        glDrawElements(GL_TRIANGLES, len(mesh.faces) * 3, GL_UNSIGNED_INT, mesh.faces)
        
        glDisableClientState(GL_VERTEX_ARRAY)
        glDisableClientState(GL_NORMAL_ARRAY)
        if hasattr(mesh.visual, 'uv') and mesh.visual.uv is not None:
            glDisableClientState(GL_TEXTURE_COORD_ARRAY)
    ```

8. **Função `main`**
    - Inicializa o Pygame e configura a janela de exibição.
    - Carrega os objetos 3D e materiais.
    - Entra no loop principal para processar eventos e desenhar a cena.
    ```python
    def main():
        global telaX, telaY, telaZ, rotacaoX, rotacaoY, rotacaoZ
        pygame.init()
        pygame.display.set_mode((1080, 720), DOUBLEBUF | OPENGL)
        init()

        cenaSol = load_mesh('objetos/planeta.obj')
        materialSol = carregar_materiais('objetos/planetaSol.mtl')
        meshSol = cenaSol

        cenaTerra = load_mesh('objetos/planeta.obj')
        materialTerra = carregar_materiais('objetos/planetaTerra.mtl')
        meshTerra = cenaTerra

        cenaPlanetaUm = load_mesh('objetos/planeta.obj')
        materialPlanetaUm = carregar_materiais('objetos/planetaUm.mtl')
        meshPlanetaUm = cenaPlanetaUm

        cenaPlanetaDois = load_mesh('objetos/planeta.obj')
        materialPlanetaDois = carregar_materiais('objetos/planetaDois.mtl')
        meshPlanetaDois = cenaPlanetaDois

        anguloTerra = 0
        anguloPlanetaUm = 0
        anguloPlanetaDois = 0

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
                    elif event.key == K_q:
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
            
            desenhar_objeto_trimesh(meshSol, materialSol)
            glPopMatrix()

            anguloTerra += 1
            anguloPlanetaUm += 1
            anguloPlanetaDois += 1

            x, y, z = calcular_rotacao(anguloTerra, 4, 'X')
            glPushMatrix()
            glTranslatef(telaX + x, telaY + y, telaZ + z)
            glScalef(1, 1, 1)
            glRotatef(rotacaoX, 1, 0, 0)
            glRotatef(rotacaoY, 0, 1, 0)
            glRotatef(rotacaoZ, 0, 0, 1)
            
            desenhar_objeto_trimesh(meshTerra, materialTerra)
            glPopMatrix()

            x, y, z = calcular_rotacao(anguloPlanetaUm, 7, 'Y')
            glPushMatrix()
            glTranslatef(telaX + x, telaY + y, telaZ + z)
            glScalef(0.5, 0.5, 0.5)
            glRotatef(rotacaoX, 1, 0, 0)
            glRotatef(rotacaoY, 0, 1, 0)
            glRotatef(rotacaoZ, 0, 0, 1)
            
            desenhar_objeto_trimesh(meshPlanetaUm, materialPlanetaUm)
            glPopMatrix()

            x, y, z = calcular_rotacao(anguloPlanetaDois, 12, 'Z')
            glPushMatrix()
            glTranslatef(telaX + x, telaY + y, telaZ + z)
            glScalef(0.75, 0.75, 0.75)
            glRotatef(rotacaoX, 1, 0, 0)
            glRotatef(rotacaoY, 0, 1, 0)
            glRotatef(rotacaoZ, 0, 0, 1)
            
            desenhar_objeto_trimesh(meshPlanetaDois, materialPlanetaDois)
            glPopMatrix()
            
            pygame.display.flip()
            pygame.time.wait(10)
            
        pygame.quit()

    if __name__ == "__main__":
        main()
    ```