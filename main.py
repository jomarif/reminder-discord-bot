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
        self.getUserInputBool = True
    
    def clock(self):
        while self.startClock: # Because it is like this it will always have to wait 1 second before it can stop the thread since it is asleep in the while function
            time.sleep(1)
            self.counter += 1
            print(self.counter)

    def getUserInput(self):
        while self.getUserInputBool:
            self.userInput = (input('Enter q to Quit\n'))
            if self.userInput == 'q':
                self.startClock = False
                self.getUserInputBool = False


if __name__ == "__main__":

    timer = Timer()
    t1 = threading.Thread(target = timer.clock)
    t2 = threading.Thread(target = timer.getUserInput)
    
    t1.start()
    t2.start()
    