import datetime


def eatingtimer():
    print(
        'Type your current BG. Stopwatch will start automatically. Press Ctrl-C to '
        'quit.')
    BG = input()  # Type your current BG
    now = datetime.datetime.now()
    delta15 = datetime.timedelta(minutes=15)
    print("My current BG is ", BG, "at time ", now, "I can eat in ", delta15)
    #print("you can start eating in ", delta15, " minutes, or at", now + delta15)

    #try:
       # while True:
            #now = datetime.datetime.now()
            #print(now)
            #delta15 = datetime.timedelta(minutes=15)
            #delta20 = datetime.timedelta(minutes=20)
            #print("Start eating in ", delta15, "minutes is ", now + delta15)
   # except KeyboardInterrupt:
        # Handle the Ctrl+C exception to keep its error message from displaying.
       # print('\nDone.')

