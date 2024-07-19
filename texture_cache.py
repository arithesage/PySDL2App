from sdl2 import SDL_Rect
from sdl2 import SDL_Texture

from sdl2 import SDL_DestroyTexture

from texture_data import TextureData

from utils import print_va




class TextureCache:
    def __init__(self) -> None:
        self.__cache = {}


    def add (self, 
             graphic_id: str, 
             texture: SDL_Texture,
             size: SDL_Rect) -> None:
        
        if not self.has (graphic_id):
            self.__cache[graphic_id] = TextureData (texture, size)
            print_va ("Cached texture for graphic '$[0]'.", graphic_id)


    def clear (self) -> None:
        print ("Clearing texture cache...")

        for entry in self.__cache.values():
            SDL_DestroyTexture (entry)

        print ("Done.")


    def get_texture (self, graphic_id: str) -> SDL_Texture:
        if self.has (graphic_id):
            return self.__cache[graphic_id].texture()
        
        return None
    

    def get_texture_data (self, graphic_id: str) -> TextureData:
        if self.has (graphic_id):
            return self.__cache[graphic_id]
        
        return None
    

    def get_texture_size (self, graphic_id: str) -> SDL_Rect:
        if self.has (graphic_id):
            return self.__cache[graphic_id].size()
        
        return None
    

    def has (self, graphic_id: str) -> bool:
        return graphic_id in self.__cache.keys()

