from diana.logger import Logger;

import glfw

def diana_init():
    if not glfw.init():
        Logger.fatal("Failed to initialise GLFW!")
    Logger.info("Initialised Diana!")

def diana_shutdown():
    glfw.terminate()
    Logger.info("Terminated Diana!")