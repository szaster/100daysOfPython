import datetime
import math


def get_bg(bg_reader):
    """
    Asks user to enter his/her blood glucose reading. Sanitizes user input,
    echos read value back to user, and returns it to caller.
    If user input cannot be parsed, function return nan.
    :param bg_reader: Function responsible for reading information from user input
    :return: Bg or nan
    """
    print('Type your current bg.')
    bg = bg_reader()  # Type your current bg
    try:
        bg_as_integer = int(bg)
        return bg_as_integer
    except Exception as e:
        return math.nan


def eating_timer():
    target_bg = 100
    bg = get_bg(input)

    print('Type food glycemic index: "high", "moderate", or "low"')
    glycemic_index = input()  # Type food glycemic_index
    print("The food's glycemic index is", glycemic_index)

    now = datetime.datetime.now()
    print("Current time is: ", datetime.datetime.now())

    # bg is above target block
    if int(bg) > target_bg and glycemic_index == "high":
        # time interval we need to wait before eating
        waiting_time = datetime.timedelta(minutes=30)
        time_when_to_eat = now + waiting_time
        print("My current bg is ", bg, "at time ", now, "I can eat in ", waiting_time, "minutes at", time_when_to_eat)
    if int(bg) > target_bg and glycemic_index == "moderate":
        # time interval we need to wait before eating
        waiting_time = datetime.timedelta(minutes=20)
        time_when_to_eat = now + waiting_time
        print("My current bg is ", bg, "at time ", now, "I can eat in ", waiting_time, "minutes at", time_when_to_eat)
    if int(bg) > target_bg and glycemic_index == "low":
        # time interval we need to wait before eating
        waiting_time = datetime.timedelta(minutes=10)
        time_when_to_eat = now + waiting_time
        print("My current bg is ", bg, "at time ", now, "I can eat in ", waiting_time, "minutes at", time_when_to_eat)

    # bg is at target block
    if int(bg) == target_bg and glycemic_index == "high":
        # time interval we need to wait before eating
        waiting_time = datetime.timedelta(minutes=20)
        time_when_to_eat = now + waiting_time
        print("My current bg is ", bg, "at time ", now, "I can eat in ", waiting_time, "minutes at", time_when_to_eat)
    if int(bg) == target_bg and glycemic_index == "moderate":
        # time interval we need to wait before eating
        waiting_time = datetime.timedelta(minutes=10)
        time_when_to_eat = now + waiting_time
        print("My current bg is ", bg, "at time ", now, "I can eat in ", waiting_time, "minutes at", time_when_to_eat)
    if int(bg) == target_bg and glycemic_index == "low":
        # time interval we need to wait before eating
        waiting_time = datetime.timedelta(minutes=10)
        time_when_to_eat = now + waiting_time
        print("My current bg is ", bg, "at time ", now, "I can eat right now and bolus in 10 minutes at",
              time_when_to_eat)

    # bg is below target block
    if int(bg) < target_bg and glycemic_index == "high":
        waiting_time = datetime.timedelta(minutes=5)
        time_when_to_eat = now + waiting_time
        print("My current bg is ", bg, "at time ", now, "I can eat in ", waiting_time, "minutes at", time_when_to_eat)
    if int(bg) < target_bg and glycemic_index == "moderate":
        waiting_time = datetime.timedelta(minutes=5)
        time_when_to_eat = now + waiting_time
        print("My current bg is ", bg, "at time ", now, "I can eat right now and bolus in 5 minutes at",
              time_when_to_eat)
    if int(bg) < target_bg and glycemic_index == "low":
        waiting_time = datetime.timedelta(minutes=20)
        time_when_to_eat = now + waiting_time
        print("My current bg is ", bg, "at time ", now, "I can eat right now and bolus in 20 minutes at",
              time_when_to_eat)

    # try:
    # while True:
    # now = datetime.datetime.now()
    # print(now)
    # delta15 = datetime.timedelta(minutes=15)
    # delta20 = datetime.timedelta(minutes=20)
    # print("Start eating in ", delta15, "minutes is ", now + delta15)

# except KeyboardInterrupt:
# Handle the Ctrl+C exception to keep its error message from displaying.
# print('\nDone.')
