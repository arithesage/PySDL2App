from scene import Scene

from utils import print_va




class Scenes:
    def __init__(self) -> None:
        self.__scenes = {}
        self.__current_scene = None
        self.__on_scene_load = None


    def current (self) -> Scene:
        return self.__current_scene
    

    def delete (self, scene_name: str) -> bool:
        if not scene_name in self.__scenes.keys():
            print_va ("ERROR: Failed to delete scene '$[0]'. Does not exists.")
            return False
        
        self.__scenes.pop (scene_name)
        print_va ("Deleted scene '$[0]'.", scene_name)
        return True


    def new (self, scene_name: str) -> Scene:
        if not scene_name in self.__scenes.keys ():
            scene = Scene (scene_name)
            self.__scenes[scene_name] = scene
            self.__current_scene = scene
            print_va ("Created new scene '$[0]'.", scene_name)

            if (self.__on_scene_load != None):
                self.__on_scene_load ()

        else:
            print_va ("ERROR: Failed to create scene '$[0]'. Already exists.", scene_name)

        return scene


    def load (self, scene_name: str) -> Scene:
        if scene_name in self.__scenes.keys ():
            self.__current_scene = self.__scenes[scene_name]
            print_va ("Loaded scene '$[0]'.", scene_name)

            if (self.__on_scene_load != None):
                self.__on_scene_load ()

            return self.__current_scene
        
        print ("ERROR: Failed to load scene '$[0]'. Scene not found.", scene_name)
        return None
    

    def on_scene_load (self, func) -> None:
        self.__on_scene_load = func