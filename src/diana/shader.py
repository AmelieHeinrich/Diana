from OpenGL.GL import *
import OpenGL.GL.shaders
from diana.logger import Logger

class Shader:
    program = 0

    def __init__(self, vertex_file, fragment_file):
        vertex_file_handle = open(vertex_file)
        vertex_source = vertex_file_handle.read()

        fragment_file_handle = open(fragment_file)
        fragment_source = fragment_file_handle.read()

        self.program = OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(vertex_source,GL_VERTEX_SHADER), OpenGL.GL.shaders.compileShader(fragment_source, GL_FRAGMENT_SHADER))

    def bind(self):
        glUseProgram(self.program)

    def unbind(self):
        glUseProgram(0)

    def set_int(self, val, name):
        loc = glGetUniformLocation(self.program, name)
        glUniform1i(loc, val)

    def set_float(self, val, name):
        loc = glGetUniformLocation(self.program, name)
        glUniform1f(loc, val)

    def set_vec2(self, x, y, name):
        loc = glGetUniformLocation(self.program, name)
        glUniform2f(loc, x, y)

    def set_vec3(self, x, y, z, name):
        loc = glGetUniformLocation(self.program, name)
        glUniform3f(loc, x, y, z)

    def set_vec4(self, x, y, z, w, name):
        loc = glGetUniformLocation(self.program, name)
        glUniform4f(loc, x, y, z, w)

    def set_matrix4(self, mat, name):
        loc = glGetUniformLocation(self.program, name)
        glUniformMatrix4fv(loc, 1, GL_FALSE, mat)