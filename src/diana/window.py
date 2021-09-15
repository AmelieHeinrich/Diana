import glfw
from diana.logger import Logger
from OpenGL.GL import *

class Window:
    width = 0
    height = 0
    title = 0
    handle = None

    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title
        self.handle = glfw.create_window(width, height, title, None, None)

        Logger.info(f"Created window with size ({width}, {height}) and title {title}")

        glfw.make_context_current(self.handle)

    def should_close(self):
        return glfw.window_should_close(self.handle)

    def update(self):
        glfw.poll_events()
        glfw.swap_buffers(self.handle)

        (x, y) = glfw.get_window_size(self.handle)
        self.width = x
        self.height = y

        glViewport(0, 0, self.width, self.height)

    def __del__(self):
        glfw.destroy_window(self.handle)
