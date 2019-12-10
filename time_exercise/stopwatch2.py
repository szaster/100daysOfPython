# stopwatch2.py  - A simple stopwatch program

import time

def stopwatch2():
    # Display the program's instructions.
    print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
    input()  # Press ENTER to begin
    print("Started.")
    starttime = time.time()  # get the first lap's start time
    lasttime = starttime
    print(starttime)
    lapnum = 1

    # Start tracking the lap times

    try:
        while True:
            input()
            laptime = round(time.time() - lasttime, 2)
            totaltime = round(time.time() - starttime, 2)
            print('Lap #%s: %s (%s)' % (lapnum, totaltime, laptime), end='')
            lapnum += 1
        lasttime = time.time()  # reset the last lap time
    except KeyboardInterrupt:
        # Handle the Ctrl+C exception to keep its error message from displaying.
        print('\nDone.')

#if __name__ == "__main__":
 #   stopwatch2()
