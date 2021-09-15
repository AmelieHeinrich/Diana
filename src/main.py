from diana.window import Window
from diana.core import *
from diana.renderer import *
from diana.shader import *
from diana.mesh import *
from diana.texture2D import *
from diana.model import *

import pyrr

class Application:
    window = None
    model = None
    shader = None

    albedo = None
    normal = None
    metallic = None
    roughness = None
    ao = None

    def __init__(self):
        diana_init()
        self.window = Window(1280, 720, "Diana!")
        self.shader = Shader("shaders/simple_vertex.glsl", "shaders/simple_fragment.glsl")  
        
        # TODO: Multithread that big function

        self.load_models()
        self.load_textures()

        self.shader.bind()
        self.shader.set_int(0, "albedoMap")
        self.shader.set_int(1, "normalMap")
        self.shader.set_int(2, "metallicMap")
        self.shader.set_int(3, "roughnessMap")
        self.shader.set_int(4, "aoMap")
        
    def load_textures(self):
        self.albedo = Texture2D("image/cerberus_albedo.png")
        self.normal = Texture2D("image/cerberus_normal.png")
        self.metallic = Texture2D("image/cerberus_metallic.png")
        self.roughness = Texture2D("image/cerberus_roughness.png")
        self.ao = Texture2D("image/cerberus_ao.png")
    
    def load_models(self):      
        self.model = Model("models/cerberus.obj")

    def run(self):
        while not self.window.should_close():
            renderer_clear(0.0, 0.0, 0.0, 1.0)
            
            view = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.0, 0.0, -2.0]))
            projection = pyrr.matrix44.create_perspective_projection_matrix(65.0, 1280 / 720, 0.01, 1000.0)
            model = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.0, 0.0, 0.0]))
            rot_y = pyrr.Matrix44.from_y_rotation(1.0 * glfw.get_time())

            self.shader.bind()

            self.shader.set_matrix4(view, "view_matrix")
            self.shader.set_matrix4(projection, "projection_matrix")
            self.shader.set_matrix4(model, "model_matrix")
            self.shader.set_matrix4(rot_y, "transform_matrix")

            # Send light info
            self.shader.set_vec3(1.0, 1.0, 0, "lightPosition")
            self.shader.set_vec3(5.0, 5.0, 5.0, "lightColor")

            # Bind textures
            self.albedo.bind(0)
            self.normal.bind(1)
            self.metallic.bind(2)
            self.roughness.bind(3)
            self.ao.bind(4)

            self.model.draw()

            self.window.update()


def main():
    app = Application()
    app.run()


if __name__ == "__main__":
    main()
    diana_shutdown()
