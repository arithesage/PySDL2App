from renderable_entity import RenderableEntity
from transform2d_component import Transform2DComponent
from image_component import ImageComponent



class Sprite (RenderableEntity):
    """
    Shortcut for creating an entity with:
    - A renderer component (so, its renderable)
    - A image component (holds an id of a loaded graphic)
    """
    def __init__(self, name = "Unnamed") -> None:
        super().__init__(name)
        self.__transform_component = self.add_component (Transform2DComponent ())
        self.__image_component =  self.add_component (ImageComponent ())
        


    def image_id (self) -> str:
        """
        Returns the ID of the assigned graphic
        """
        return self.__image_component.image_id ()
    

    def move_to (self, x: float, y: float) -> None:
        self.transform().position().set(x, y)
    

    def set_image_id (self, image_id: str) -> None:
        """
        Sets the ID of a loaded graphic
        """
        self.__image_component.set_image_id (image_id)

        
    def transform (self) -> Transform2DComponent:
        return self.__transform_component