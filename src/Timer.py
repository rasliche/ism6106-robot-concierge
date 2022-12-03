from time import time
from math import floor

# now = time()
# print(time()-now)

"""
Timer class is used to document how long a visitor
is within the detection range of an exhibit. It is
triggered by a sensor.
"""
class Timer():
    """
    Creates an instance of the Timer class
    """
    def __init__(self) -> None:
        self._startTime = None
        self._endTime = None

    """
    Record the current time in the startTime variable
    """
    def start(self):
        self._startTime = time()
        print("Timer started")

    """
    Record the current time in the endTime variable
    """
    def stop(self):
        self._endTime = time()
        print("Timer stopped")

    """
    Retrun the difference between the start and end time variables
    """
    def report(self):
        return floor(self._endTime - self._startTime)

    """
    Reset the timer variables to None
    """
    def reset(self):
        self._endTime = None
        self._startTime = None

