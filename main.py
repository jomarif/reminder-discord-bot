# Ask user what it wants to be reminded about
# Ask when (in what amount of time, in minutes?)
# Calculate timeout
# Wait for the specified time
# Remind of what was requested

import schedule
import time

def job():
    print('Hello World')

if __name__ == "__main__":

    timeStart = time.time()

    while True:

        # Prints out something every 3 seconds
        if round((time.time() - timeStart)) % 3 == 0:
            while round(time.time() - timeStart) % 3 == 0: # we need this to ensure that it only prints once
                pass
            print('3 Seconds have passed')
            print(f"Total time has been {round((time.time() - timeStart))}")

        # this would be the timer

        # input from user