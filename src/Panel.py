from Exhibit import Exhibit

"""
Child class of an Exhibit. A sub unit.
"""
class Panel(Exhibit):
    """
    Create an instance of a Panel
    """
    def __init__(self, name, type="wall", location="main") -> None:
        super().__init__(type, location)
        self._name = name

    """
    Returns the count of visitors in front of a panel.
    """
    def count():
        pass

    """
    Returns the duration of a visitors interaction with a panel.
    """
    def stayDuration():
        pass
