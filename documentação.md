### Documentação Resumida

#### Arquivo `main.py`

1. **Importações**
    ```python
    import pygame
    from pygame.locals import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from objetos.esfera import desenhar_esfera
    from objetos.cubo import desenhar_cubo
    from objetos.arma import desenhar_pistola
    from iluminacao.iluminacao_basica import iniciar_iluminacao
    from OpenGL.GLUT import *
    ```

2. **Variáveis Globais**
    ```python
    telaX = 0
    telaY = 0
    telaZ = -5
    rotacaoX = 0
    rotacaoY = 0
    rotacaoZ = 0
    ```

3. **Função `init`**
    - Configura o ambiente OpenGL para iniciar o ambiente 3D.
    ```python
    def init():    
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClearDepth(1.0)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, 640.0 / 480.0, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
    ```

4. **Função `main`**
    - Inicializa o Pygame e configura a janela de exibição.
    - Chama as funções de inicialização do OpenGL e iluminação.
    - Entra no loop principal para processar eventos e desenhar a cena.
    ```python
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

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                           
            desenhar_pistola()
            
            pygame.display.flip()
            pygame.time.wait(10)
            
        pygame.quit()

    if __name__ == "__main__":
        main()
    ```

#### Arquivo `arma.py`

1. **Importações**
    ```python
    from OpenGL.GL import *
    from OpenGL.GLU import *
    import os
    import pygame
    ```

2. **Função `desenhar_pistola`**
    - Carrega o modelo OBJ e MTL.
    - Desenha o objeto na tela.
    ```python
    def desenhar_pistola():
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        caminho_objeto = os.path.join(diretorio_atual, 'pistola.obj')
        caminho_material = os.path.join(diretorio_atual, 'pistola.mtl')
        vertices, faces, normais, materiais = carregar_objeto(caminho_objeto, caminho_material)

        glPushMatrix()
        glTranslatef(0.0, 0.0, -5.0)  # Afasta o objeto ao longo do eixo Z
        desenhar_objeto(vertices, faces, normais, materiais)
        glPopMatrix()
    ```

3. **Função `carregar_objeto`**
    - Carrega os vértices, faces, normais e materiais do arquivo OBJ.
    ```python
    def carregar_objeto(nome_arquivo, nome_material):
        vertices = []
        faces = []
        normais = []
        materiais = carregar_materiais(nome_material)

        with open(nome_arquivo) as f:
            material_atual = None
            for line in f:
                if line.startswith('v '):
                    vertices.append(list(map(float, line.strip().split()[1:])))
                elif line.startswith('vn '):
                    normais.append(list(map(float, line.strip().split()[1:])))
                elif line.startswith('usemtl '):
                    material_atual = line.strip().split()[1]
                elif line.startswith('f '):
                    face = []
                    for vertex in line.strip().split()[1:]:
                        v, vt, vn = (vertex.split('/') + [None, None])[:3]
                        face.append((int(v) - 1, int(vn) - 1 if vn else None))
                    faces.append((face, material_atual))
        return vertices, faces, normais, materiais
    ```

4. **Função `carregar_materiais`**
    - Carrega os materiais do arquivo MTL.
    ```python
    def carregar_materiais(nome_arquivo):
        materiais = {}
        material_atual = None

        with open(nome_arquivo) as f:
            for line in f:
                if line.startswith('newmtl '):
                    material_atual = line.strip().split()[1]
                    materiais[material_atual] = {}
                    print(f"Carregando material: {material_atual}")
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
                        materiais[material_atual]['map_Kd'] = line.strip().split()[1]
                    elif line.startswith('map_Ns '):
                        materiais[material_atual]['map_Ns'] = line.strip().split()[1]
                    elif line.startswith('map_Bump '):
                        materiais[material_atual]['map_Bump'] = line.strip().split()[-1]
        return materiais
    ```

5. **Função `carregar_textura`**
    - Carrega uma textura a partir do png (Objeto/Textures).
    ```python
    def carregar_textura(caminho_textura):
        print(f"Carregando textura: {caminho_textura}")
        texture_surface = pygame.image.load(caminho_textura)
        texture_data = pygame.image.tostring(texture_surface, "RGB", True)
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

6. **Função `aplicar_material`**
    - Aplica as propriedades do material e carrega a textura.
    ```python
    def aplicar_material(material, diretorio_base, texturas):
        if 'Kd' in material:
            glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, material['Kd'])
        if 'Ka' in material:
            glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, material['Ka'])
        if 'Ks' in material:
            glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, material['Ks'])
        if 'Ns' in material:
            glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, material['Ns'])
        if 'map_Kd' in material:
            caminho_textura = os.path.join(diretorio_base, material['map_Kd'])
            if caminho_textura not in texturas:
                texturas[caminho_textura] = carregar_textura(caminho_textura)
            texture_id = texturas[caminho_textura]
            glBindTexture(GL_TEXTURE_2D, texture_id)
            glEnable(GL_TEXTURE_2D)
        else:
            glDisable(GL_TEXTURE_2D)
    ```

7. **Função `desenhar_objeto`**
    - Desenha o objeto usando os vértices, faces, normais e materiais carregados.
    ```python
    def desenhar_objeto(vertices, faces, normais, materiais):
        diretorio_base = os.path.dirname(os.path.abspath(__file__))
        texturas = {}
        for face, material in faces:
            if material and material in materiais:
                aplicar_material(materiais[material], diretorio_base, texturas)
            glBegin(GL_TRIANGLES)
            for vertex, normal in face:
                if normal is not None:
                    glNormal3fv(normais[normal])
                glVertex3fv(vertices[vertex])
            glEnd()
    ```

### Estrutura de Pastas e Arquivos
```
│
├── main.py
├── objetos/
│   ├── esfera.py
│   ├── cubo.py
│   ├── pistola.obj
│   ├── pistola.mtl
│   ├── arma.py
│   └── Textures/       
│       └── *.png
└── iluminacao/
    └── iluminacao_basica.py
```