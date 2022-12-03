from math import floor
"""
Digital Docent is the main class that coordinates the rest
of the sub-units. Users of the Digital Docent program requesting
information about the state of the visitor center will interact
with the DigitalDocent class instance.
"""
class DigitalDocent():
    """
    Create an instances of the class
    Defaults to a single 'main' area, but can accept a list of
    other areas
    """
    def __init__(self, areas=[]) -> None:
        self._areas = {}
        self._areas["main"] = 0
        for area in areas:
            self._areas[area] = 0

    """
    Returns the areas tracked by the DigitalDocent instance
    """
    def areas(self):
        return list(self._areas)

    """
    Prints a report of the visitors the DD was made aware of
    """
    def trackVisitor(self, maxCount=1):
        print(f"Visitor interaction recorded: {maxCount} visitors")

    """
    Tabulates and records the 'peopleTime' of a visit.
    peopleTime is the number of visitors multiplied by
    how long they were at an exhibit
    """
    def trackArea(self, area="Main", peopleTime=0):
        self._areas[area] += peopleTime
        print(f"Area interaction recorded for {area} with {floor(peopleTime)} people-minutes")
    
    """
    Reports on a duration of a visit
    """
    def trackTime(self, duration=0):
        print(f"Duration of interaction recorded: {floor(duration)}")

    """
    Print a detailed report of the DigitalDocent's records for an instance.
    """
    def report(self):
        print('{:^20}'.format("Area")+"|"+'{:^7}'.format("Count"))
        for area in self._areas:
            print(f"{area:<20}|{self._areas[area]:>7}")
