from OpenGL.GL import *
from OpenGL.GLU import *
import os
import pygame

def desenhar_pistola(telaX, telaY, telaZ, rotacaoX, rotacaoY, rotacaoZ):
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_objeto = os.path.join(diretorio_atual, 'pistola.obj')
    caminho_material = os.path.join(diretorio_atual, 'pistola.mtl')
    vertices, faces, normais, materiais = carregar_objeto(caminho_objeto, caminho_material)

    glPushMatrix()
    glTranslatef(telaX, telaY, telaZ)
    glRotatef(rotacaoX, 1, 0, 0)
    glRotatef(rotacaoY, 0, 1, 0)
    glRotatef(rotacaoZ, 0, 0, 1)
    desenhar_objeto(vertices, faces, normais, materiais)
    glPopMatrix()

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
