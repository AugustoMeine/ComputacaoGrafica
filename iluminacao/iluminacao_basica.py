from OpenGL.GL import *
from OpenGL.GLU import *

def iniciar_iluminacao():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    
    light_ambient = [0, 0, 0, 1.0]
    light_diffuse = [0.5, 0.5, 0.5, 0]
    light_position = [0, 2, 0, 0.5]

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    material_specular = [0.8, 0.8, 0.8, 1.0]
    material_shininess = [60.0]

    glMaterialfv(GL_FRONT, GL_SPECULAR, material_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, material_shininess)

    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)