from entity_component import EntityComponent
from vector_2d import Vector2D


class Transform2DComponent (EntityComponent):
    """
    A component that holds information about the position,
    rotation and scale of a entity.
    """
    def __init__(self, tag: str = "") -> None:
        super().__init__(tag)
        
        self._unique = True

        self.__position = Vector2D ()
        self.__rotation = Vector2D ()
        self.__scale = Vector2D (1.0, 1.0)
        

    def position (self) -> Vector2D:
        """
        Returns the position
        """
        return self.__position
    

    def rotation (self) -> Vector2D:
        """
        Returns the rotation
        """
        return self.__rotation
    

    def scale (self) -> Vector2D:
        """
        Returns the scale
        """
        return self.__scale
    
    