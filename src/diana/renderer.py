from OpenGL.GL import *

def renderer_clear(r, g, b, a):
    glEnable(GL_DEPTH_TEST)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(r, g, b, a)