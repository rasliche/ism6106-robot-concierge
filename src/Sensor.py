"""
Sensor parent class
This class contains all of the non-unique info for a generic sensor
Child sensors override data with their own specific info and
methods that are unique to each, if applicable.
"""
class Sensor():
    def __init__(self, pins=[], sensors=[], type="generic", measuring=False, active=False) -> None:
        self._pins = pins
        self._sensors = sensors
        self.type = type
        self._measuring = measuring
        self._active = active

    """
    Request whether the sensor has signaled to begin timing
    visitor interactions with an exhibit or panel
    """
    def timeMeasuring(self):
        return self._measuring

    """
    Request whether the sensor has counted a visitor
    """
    def counting(self):
        pass

    """
    Request the location of the sensor if applicable
    """
    def locating(self):
        pass
    
    """
    Set the sensor to active
    """
    def on(self) -> bool:
        self._active = True
        return True

    """
    Set the sensor to inactive
    """
    def off(self) -> bool:
        self._active = False
        return False

    """
    Request information from the sensor to determine whether a visitor is being detected
    """
    def query(self):
        pass

"""
Laser break beam sensor helps count traffic in one-way areas
Also useful in narrow areas like halways.
"""
class LaserBreakBeam(Sensor):
    def __init__(self, beam, pins=[], sensors=[], type="Laser", measuring=False, active=False) -> None:
        super().__init__(pins, sensors, type, measuring, active)
        self._beam = beam

"""
Ultrasonic Sensor used to detect visitors within a designated area.
This sensor is useful when detection in a specific "slice" zone is
desired and there is no opposite wall to mount a laser reflector.
"""
class Ultrasonic(Sensor):
    def __init__(self, detectionDistance, pins=[], sensors=[], type="Ultrasonic", measuring=False, active=False) -> None:
        super().__init__(pins, sensors, type, measuring, active)
        self._detectionDistance = detectionDistance

"""
Microwave sensor used to detect visitors within a designated area
"""
class Microwave(Sensor):
    def __init__(self, powerLevel, pins=[], sensors=[], type="Microwave", measuring=False, active=False) -> None:
        super().__init__(pins, sensors, type, measuring, active)
        self._powerLevel = powerLevel

"""
Pressure Sensitive Sensor Class
Used to measure whether a visitor is interacting with an area with a mat
or stand-up paddle board photo op activity
"""
class Pressure(Sensor):
    def __init__(self, standingSpace, pins=[], sensors=[], type="Pressure", measuring=False, active=False) -> None:
        super().__init__(pins, sensors, type, measuring, active)
        self._standingSpace = standingSpace