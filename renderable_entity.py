from entity import Entity
from renderer_component import RendererComponent


class RenderableEntity (Entity):
    def __init__(self, name = "Unnamed") -> None:
        super().__init__(name)
        self._render_component =  self.add_component (RendererComponent ())


    def renderer_component (self) -> RendererComponent:
        return self._render_component
    
        