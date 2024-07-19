
class Tags:
    def __init__(self) -> None:
        self.__tags = []


    def add (self, tag: str) -> None:
        if not self.contains (tag):
            self.__tags.append (tag)


    def contains (self, tag: str) -> bool:
        return (tag in self.__tags)
    

    def delete (self, tag: str) -> None:
        if self.contains (tag):
            self.__tags.remove (tag)


    def __str__(self) -> str:
        return str (self.__tags)
    