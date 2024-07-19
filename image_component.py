from entity_component import EntityComponent




class ImageComponent (EntityComponent):
    """
    This components holds the ID of a loaded image
    """
    def __init__(self, tag: str = "") -> None:
        super().__init__(tag)
        self._unique = False
        self.__image_id = None


    def enable(self) -> None:
        """
        Enables this component making the entity renderable if
        a RendererComponent is present, is valid and is enabled.
        """
        super().enable()

        renderer_component = self._owner.get_component (RendererComponent)

        if (renderer_component != None) and renderer_component.is_valid() and \
            renderer_component.is_enabled ():
            self._owner._renderable = True


    def disable (self) -> None:
        """
        Disables this component making the entity not renderable.
        """
        super().disable()
        self._owner._renderable = False


    def set_image_id (self, image_id: str) -> None:
        """
        Sets the ID of the image to be used.
        This makes makes the entity graphics to need caching.
        """
        self.__image_id = image_id
        self._owner._textures_cached = False

        if self.is_enabled ():
            self.owner()._renderable = True


    def image_id (self) -> str:
        """
        Returns the ID of the image being used
        """
        return self.__image_id
        

    def is_valid (self) -> bool:
        """
        Returns if this component is valid
        """
        super().is_valid ()

        return (self.__image_id != None) and \
               (self.__image_id != "")
    



# Left at bottom to avoid cyclic imports errors
from renderer_component import RendererComponent
    