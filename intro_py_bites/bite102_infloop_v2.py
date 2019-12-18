def read_color(input_func):
    """
    Reads input color and lower cases it
    """
    user_supplied_color = input_func()
    return user_supplied_color.casefold()


def is_quit(user_supplied_color):
    return 'quit' == user_supplied_color


def print_colors():
    """
    In the while loop ask the user to enter a color,
    lowercase it and store it in a variable. Next check:
    - if 'quit' was entered for color, print 'bye' and break.
    - if the color is not in VALID_COLORS, print 'Not a valid color' and continue.
    - otherwise print the color in lower case.
    """
    pass
