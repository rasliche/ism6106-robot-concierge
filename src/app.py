from DigitalDocent import DigitalDocent
from Sensor import Ultrasonic
from Counter import Counter
from Timer import Timer
from time import sleep
from random import randrange
from math import floor

"""
Utility to get a random time between 1 and 7 seconds to simulate a visitor
"""
def getRandomVisitTime():
    sleep(randrange(3,8))
    
"""
Utility to assign a visit to a random exhibit location
"""
def getRandomArea(dd):
    areasView = dd.areas()
    return areasView[randrange(0, len(areasView))]

"""
Main demonstration
"""
def main():
    print('{:^40}'.format("Beginning Day"))
    totalVisitors = 0
    totalTimeOfInteractions = 0
    # Create a Digital Docent instance to orchestrate
    # and record visits
    docent = DigitalDocent(areas=["Sea Grass", "Corals", "Mangroves", "SUP", "Aquarius"])
    for i in range(4, randrange(8,15)):

        # Create an Ultrasonic Sensor
        us = Ultrasonic(250)
        # Create a timer for the exhibit
        exhibitTimer = Timer()
        # Create a counter for the exhibit
        exhibitCounter = Counter()

        # Trigger the sensor
        us.on()
        exhibitCounter.increment(randrange(1,5))
        print("Visitor detected")
        exhibitTimer.start()
        getRandomVisitTime()
        print("Sensor detection area clear")
        exhibitTimer.stop()

        docent.trackArea(getRandomArea(docent), exhibitCounter.report() * exhibitTimer.report())
        docent.trackVisitor(exhibitCounter.report())
        totalVisitors += exhibitCounter.report()
        docent.trackTime(floor(exhibitTimer.report()))
        totalTimeOfInteractions += exhibitTimer.report()
        sleep(randrange(1,5)) # Wait for the next visitor group
        print("\n")

    print("Total Daily Visitors")
    print(f"{totalVisitors}")
    print("Total Time of Interactions")
    print(f"{floor(totalTimeOfInteractions)} minutes")
    docent.report()
    print('{:^40}'.format("Ending Day"))

"""
Run the demonstration application
"""
if __name__ == '__main__':
    main()