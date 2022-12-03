"""
Generic counter class to keep track of visitors in an area
Usually it will begin and end at zero.
"""
class Counter():
    def __init__(self, count=0) -> None:
        self._count = count

    def reset(self):
        self._count = 0

    def increment(self, value=1):
        self._count += value

    def decrement(self):
        if self._count > 0:
            self._count -= 1

    def report(self):
        return self._count