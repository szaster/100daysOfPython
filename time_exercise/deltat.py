import datetime
import re


def get_bg():
    print('Type your current bg.')
    bg = input()  # Type your current bg
    if not re.match("[1-9]", bg):
        print("Error! Only numbers are allowed.")
        print("My current bg is", bg)
    return bg


def eating_timer():
    target_bg = 100
    bg = get_bg()

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
