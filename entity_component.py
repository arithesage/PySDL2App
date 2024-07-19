from tags import Tags




class EntityComponent:
    """
    Base for all entity components
    """
    def __init__(self, tag: str = "") -> None:
        self._enabled = True
        self._unique = True
        self._on_enable = None
        self._on_disable = None
        self._owner = None
        self.__tags = Tags ()

        if (tag != ""):
            self.tags().add(tag)


    def _attach_to (self, entity) -> None:
        """
        FOR INTERNAL USE ONLY. Associates this component with an entity.
        """
        self._owner = entity


    def enable (self) -> None:
        """
        Enables this component.
        """
        self._enabled = True

        if (self._on_enable != None):
            self._on_enable ()


    def disable (self) -> None:
        """
        Disables this component.
        """
        self._enabled = False

        if (self._on_disable != None):
            self._on_disable ()


    def is_enabled (self) -> bool:
        """
        Returns if this component is enabled.
        """
        return self._enabled
    

    def is_valid (self) -> bool:
        """
        Override to check if the component is valid.
        """
        pass
    
    
    def must_be_unique (self) -> bool:
        """
        Returns if the component must be unique (only one with this
        type can be added to an entity).
        """
        return self._unique
    

    def on_enable (self, func) -> None:
        """
        Add a callback function to be notified of when this component
        is enabled.
        """
        self._on_enable = func
    

    def on_disable (self, func) -> None:
        """
        Add a callback function to be notified of when this component
        is disabled.
        """
        self._on_disable = func


    def owner (self):
        """
        Returns the entity owning this component
        """
        return self._owner


    def tags (self) -> Tags:
        """
        Returns this component tags
        """
        return self.__tags

