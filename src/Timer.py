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
    def __init__(self) -> None:
        self._startTime = None
        self._endTime = None

    def start(self):
        self._startTime = time()
        print("Timer started")

    def stop(self):
        self._endTime = time()
        print("Timer stopped")

    def report(self):
        return floor(self._endTime - self._startTime)

    def reset(self):
        self._endTime = None
        self._startTime = None

