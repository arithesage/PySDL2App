#!/usr/bin/env python

from sdl2app import SDL2App

from scene import Scene
from sprite import Sprite


class Test (SDL2App):
    def __init__(self,
                 resources_path: str = SDL2App.DEFAULTS.RESOURCES_PATH, 
                 app_name: str = SDL2App.DEFAULTS.WINDOW_TITLE,
                 window_size = SDL2App.DEFAULTS.WINDOW_SIZE, 
                 system_flags = SDL2App.DEFAULTS.SYSTEMS_FLAGS,
                 window_flags = SDL2App.DEFAULTS.WINDOW_FLAGS,
                 renderer_flags = SDL2App.DEFAULTS.RENDERER_FLAGS) -> None:
        
        super().__init__(resources_path, 
                         app_name, 
                         window_size, 
                         system_flags, 
                         window_flags, 
                         renderer_flags)
        
    def on_start(self):
        super().on_start()

        self.asset_store().load_graphic ("sprite", "graphics/sprite.jpg")
        scene = self.scenes().new("default")
        
        sprite = Sprite ("Test")
        sprite.set_image_id ("sprite")

        scene.add (sprite)

        sprite2 = Sprite ("Test")
        sprite2.set_image_id ("sprite")
        sprite2.transform().position().set(100, 100)
        
        scene.add (sprite2)


    

test = Test ("./res")
test.start ()
