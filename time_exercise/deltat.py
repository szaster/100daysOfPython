import datetime

now = datetime.datetime.now()
print(now)
delta15 = datetime.timedelta(minutes=15)
delta20 = datetime.timedelta(minutes=20)
print("time in " , delta15, "minutes is ", now + delta15)


def eatingtimer():
    print(
        'Press ENTER to begin. Afterwards, input your current BG. Stopwatch will start automatically. Press Ctrl-C to '
        'quit.')
    myBG = input()  # Press ENTER to begin
    print(myBG)
    #print("you can start eating in ", delta15, " minutes, or at", now + delta15)
