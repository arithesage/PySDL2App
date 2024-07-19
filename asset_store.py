from sdl2 import SDL_FreeSurface
from sdl2.sdlimage import IMG_Load
from graphic_data import GraphicData

from utils import file_exists
from utils import make_path




class AssetStore:
    """
    Used for loading resources like audio, fonts, graphics...
    """
    def __init__(self, resources_path: str) -> None:
        self.__resources = resources_path
        self.__graphics = {}


    def destroy (self):
        for graphic_data in self.__graphics.values():
            if (graphic_data.graphic() != None):
                SDL_FreeSurface (graphic_data.graphic())
    

    def has_graphic (self, graphic_id: str) -> bool:
        """
        Returns if a GraphicData object is stored with the given ID.
        """
        return graphic_id in self.__graphics.keys()


    def load_graphic (self, graphic_id: str, path: str) -> GraphicData:
        """
        Loads a image file and store its path, dimensions and the
        graphic data itself in a GraphicData object.

        Returns the create GraphicData or None if the process failed.
        """
        image_path = make_path (self.__resources, path)

        if file_exists (image_path):
            surface = IMG_Load (image_path.encode())

            if (surface != None):
                graphic_data = GraphicData (image_path, surface)
                self.__graphics[graphic_id] = graphic_data
                return graphic_data
            
        return None
    

    def get_graphic (self, graphic_id: str) -> GraphicData:
        """
        Returns the GraphicData object stored with the given ID
        or None if nothing was found.
        """
        if not self.has_graphic (graphic_id):
            return None
        
        return self.__graphics[graphic_id]
    
