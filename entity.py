from entity_component import EntityComponent
from tags import Tags

from utils import str_empty
from utils import type_of




class Entity:
    """
    An entity is the most basic object that can be in a scene.
    """
    def __init__(self, name = "Unnamed") -> None:
        self._name = name
        self._components = []
        self._renderable = False
        self._textures_cached = False
        self.__tags = Tags ()
        
    
    def name (self):
        """
        Returns the entity name
        """
        return self._name
    

    def add_component (self, 
                       component: EntityComponent):
        """
        Adds the given component to the entity
        """
        
        if component.must_be_unique() and self.has_component (type(component)):
            print ("ERROR: Failed adding component that must be unique.")
            print ("ERROR: A component of the same type already exists.")
            return None
        
        self._components.append (component)
        component._attach_to (self)

        return component
    

    def _all_textures_cached (self) -> None:
        """
        FOR INTERNAL USE ONLY. Returns if all needed textures for this entity
        have been already cached (uploaded to the GPU).
        """
        self._all_textures_cached = True
    

    def get_component (self, component_type: type, tag: str = ""):
        """
        Returns the first component found with the given type.
        You can specify a tag if the component you search includes it.
        """
        if self.has_no_components ():
            return None
        
        for component in self._components:
            if type_of (component, component_type):
                if not str_empty (tag):
                    if component.tags().contains(tag):
                        return component
                else:
                    return component
                
        return None


    def get_components (self, component_type: type, tag: str = ""):
        """
        Returns all the components that match the given component type
        and tag criteria or an empty list if nothing was founf.
        """
        found_components = []

        for component in self._components:
            if type_of (component, component_type):
                if not str_empty (tag):
                    if component.tags().contains(tag):
                        found_components.append (component)
                else:
                    found_components.append (component)

        return found_components


    def has_component (self, component_type: type, tag: str = "") -> bool:
        """
        Returns if this entity has a component with the given type.
        You can specify a tag if the component you search includes it.
        """
        if self.has_no_components ():
            return False
        
        for component in self._components:
            if type_of (component, component_type):
                if not str_empty (tag):
                    if component.tags().contains(tag):
                        return True
                else:
                    return True
                
        return False
        

    def has_no_components (self) -> bool:
        """
        Returns if the entity has no components.
        """
        return (len (self._components) == 0)
    

    def _has_textures_cached (self):
        """
        FOR INTERNAL USE ONLY. Returns if the entity has all its textures
        cached already.
        """
        return self._textures_cached
    

    def is_renderable (self) -> bool:
        """
        Returns if the entity is renderable.
        This requires having a RendererComponent and a ImageComponent.
        """
        return self._renderable
    

    def tags (self) -> Tags:
        """
        Returns the tags of this entity
        """
        return self.__tags
    