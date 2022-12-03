"""
Exhibit class is the main unit of an area that the
Digital Docent is responsible for monitoring
"""
class Exhibit():
    """
    Create an instance of an exhibit
    """
    def __init__(self, type="wall", location="main") -> None:
        self._type = type
        self._location = location

    """
    Skeleton of a method that would return the visitors currently 
    interacting with an exhibit
    """
    def visitorCount(self):
        pass