# Ask user what it wants to be reminded about
# Ask when (in what amount of time, in minutes?)
# Calculate timeout
# Wait for the specified time
# Remind of what was requested

import threading
import time

class Timer:

    def __init__(self):
        self.counter = 0
        self.startClock = True
    
    def clock(self):
        while self.startClock:
            self.secondsCounter = 1
            while self.secondsCounter % 50 is not 0:
                time.sleep(0.1)
                self.secondsCounter += 1
            self.counter += 1 
            print(self.counter)

def getUserInput():
    userInput = int(input('Enter -1 to Quit\n'))
    if userInput == -1:
        timer.startClock = False



if __name__ == "__main__":

    timer = Timer()
    t1 = threading.Thread(target = timer.clock)
    t1.start()

    t2 = threading.Thread(target = getUserInput)
    t2.start()
