"""
Digital Docent is the main class that coordinates the rest
of the sub-units. Users of the Digital Docent program requesting
information about the state of the visitor center will interact
with the DigitalDocent class instance.
"""
class DigitalDocent():
    def __init__(self) -> None:
        pass

    def trackVisitor(self):
        print("Visitor interaction recorded")

    def trackArea(self):
        print("Area interaction recorded")

    def trackTime(self):
        print("Duration of interaction recorded")
