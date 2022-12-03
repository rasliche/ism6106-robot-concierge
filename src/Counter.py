"""
Generic counter class to keep track of visitors in an area
Usually it will begin and end at zero.
"""
class Counter():
    """
    Initialize a Counter instance
    """
    def __init__(self, count=0) -> None:
        self._count = count

    """
    Reset the counter to zero
    """
    def reset(self):
        self._count = 0

    """
    Increment the counter by the specified value.
    Defaults to 1
    """
    def increment(self, value=1):
        self._count += value

    """
    Decrement the counter by the specified value
    Defaults to 1, cannot go below zero
    """
    def decrement(self, value=1):
        if self._count > value:
            self._count -= value
        else:
            self._count = 0

    """
    Reports out the current count of the instance
    """
    def report(self):
        return self._count