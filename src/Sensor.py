class Sensor():
    def __init__(self, pins=[], sensors=[], type="generic", measuring=False, active=False) -> None:
        self._pins = pins
        self._sensors = sensors
        self.type = type
        self._measuring = measuring
        self._active = active

    def timeMeasuring(self):
        return self._measuring

    def counting(self):
        pass

    def locating(self):
        pass

    def on(self) -> bool:
        self._active = True
        return True

    def off(self) -> bool:
        self._active = False
        return False

    def query(self):
        pass

class LaserBreakBeam(Sensor):
    def __init__(self, pins=[], sensors=[], type="Laser", measuring=False, active=False) -> None:
        super().__init__(pins, sensors, type, measuring, active)

class Ultrasonic(Sensor):
    def __init__(self, pins=[], sensors=[], type="Ultrasonic", measuring=False, active=False) -> None:
        super().__init__(pins, sensors, type, measuring, active)

class Microwave(Sensor):
    def __init__(self, pins=[], sensors=[], type="Microwave", measuring=False, active=False) -> None:
        super().__init__(pins, sensors, type, measuring, active)

