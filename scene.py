from typing import Tuple

from entity import Entity




class Scene:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__scene = []
        self.__on_entity_add = None


    def add (self, entity: Entity) -> None:
        self.__scene.append (entity)

        if (self.__on_entity_add != None):
            self.__on_entity_add (entity)


    def get_entity (self, name: str) -> Entity:        
        if self.is_empty ():
            return None
        
        for entity in self.__scene:
            if (entity.name() == name):
                return entity
            
        return None
    

    def get_entities (self) -> Tuple[Entity]:
        return self.__scene
    

    def get_entities_named (self, name: str) -> Tuple [Entity]:        
        found_entities = []        
        
        if not self.is_empty ():
            for entity in self.__scene:
                if (entity.name() == name):
                    found_entities.append (entity)

        return found_entities
    

    def has_entity (self, name: str) -> bool:
        entity = self.get_entity (name)
        return (entity != None)


    def is_empty (self) -> bool:
        return (len (self.__scene) == 0)
    

    def name (self) -> str:
        return self.__name
    

    def on_entity_add (self, func) -> None:
        self.__on_entity_add = func
        