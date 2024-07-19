from entity_component import EntityComponent




class RendererComponent (EntityComponent):
    """
    An entity needs a Renderer and a Image
    component at minimum for being renderable.
    """
    def __init__(self) -> None:
        super().__init__()        
        self._unique = True


    def is_valid(self) -> bool:
        return True


    def is_visible (self):
        """
        Returns if this entity is visible (has the renderer
        component enabled)
        """
        return self.is_enabled ()
    

    def enable (self) -> None:
        """
        Enables the component making the entity renderable if also
        an ImageComponent exists, is valid and enabled.
        """
        super().enable()

        image_component = self._owner.get_component (ImageComponent)

        if (image_component != None) and image_component.is_valid() and \
            image_component.is_enabled():
            self._owner._renderable = True


    def disable (self) -> None:
        """
        Disables the component making the entity no renderable.
        """
        super().disable()
        self._owner._renderable = False




from image_component import ImageComponent