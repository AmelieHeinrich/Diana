from OpenGL.GL import *
import numpy as np

class Mesh:
    vao = 0
    vbo = 0
    ebo = 0
    index_size = 0

    def __init__(self, vertices, indices):
        self.vao =  glGenVertexArrays(1)
        glBindVertexArray(self.vao)

        raw_vertices = np.array(vertices, dtype = np.float32)
        raw_indices = np.array(indices, dtype = np.uint32)

        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, len(raw_vertices) * 4, raw_vertices, GL_STATIC_DRAW)
        
        self.ebo = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, len(raw_indices) * 4, raw_indices, GL_STATIC_DRAW)

        self.index_size = len(indices)
        
        vertex_stride = (3 * 4) + (3 * 4) + (2 * 4)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, False, vertex_stride, ctypes.c_void_p(0))
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, False, vertex_stride, ctypes.c_void_p(12))
        glEnableVertexAttribArray(2)
        glVertexAttribPointer(2, 2, GL_FLOAT, False, vertex_stride, ctypes.c_void_p(24))

    def draw(self):
        glBindVertexArray(self.vao)
        glDrawElements(GL_TRIANGLES, self.index_size, GL_UNSIGNED_INT, None)
