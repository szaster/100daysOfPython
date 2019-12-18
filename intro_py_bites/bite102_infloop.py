VALID_COLORS = ['blue', 'yellow', 'red']


def print_colors():
    """In the while loop ask the user to enter a color,
       lowercase it and store it in a variable. Next check:
       - if 'quit' was entered for color, print 'bye' and break.
       - if the color is not in VALID_COLORS, print 'Not a valid color' and continue.
       - otherwise print the color in lower case."""
    #is_found = False
    while True:
        print("Enter a color: (print quit to quit)")
        color = str.casefold(input())  # converts into string and lowercases the input
        if color == 'quit':
            print("bye")
            break

        if color in VALID_COLORS:
            print(color)
        elif color not in VALID_COLORS:
            print("Not a valid color")

print_colors()

#while True:
#    print("Enter a color: (print quit to quit)")
#    color = str.casefold(input())  # converts into string and lowercases the input
#    if color == 'quit':
#        print("bye")
#        break
#
#    if not print_colors(color):
#        print("Not a valid color")

#print_colors('tgr')






