import datetime


def eatingtimer():
    targetBG = 120
    print(
        'Type your current BG.')
    BG = input()  # Type your current BG
    print ("My current BG is", BG)
    print('Type food GI: "high", "moderate", or "low"')
    GI = input() # Type food GI
    print("The food's GI is", GI)
    now = datetime.datetime.now()
    print("Current time is: ", datetime.datetime.now())

    #High GI block
    if GI == "high" and BG > targetBG:
        minutes = 30
    dthigh = datetime.timedelta(minutes=30)
    deltahigh= now + dthigh
    print("My current BG is ", BG, "at time ", now, "I can eat in ", dt, "minutes at", delta)
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

