from time import sleep


def print_elapsed_time(ms):
    """
    Prints time in HH:MM:SS format given number of milliseconds.
    Input is number of milliseconds to print.
    """
    seconds = ms / 1000
    print(seconds, end="\r")


def stopwatch():
    print("Press 's' to start stopwatch")
    while True:
        pressed_key = input()
        if pressed_key == 's':
            break
    # elapsed milli-seconds
    i = 0
    while True:
        sleep(0.001)
        i += 1
        print_elapsed_time(i)
