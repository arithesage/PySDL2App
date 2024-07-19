from sdl2 import SDL_Rect
from sdl2 import SDL_Texture




class TextureData:
    def __init__(self, texture: SDL_Texture, size: SDL_Rect) -> None:
        self.__texture = texture
        self.__size = size


    def size (self) -> SDL_Rect:
        return self.__size


    def texture (self) -> SDL_Texture:
        return self.__texture
    