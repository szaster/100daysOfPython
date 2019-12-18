MIN_DRIVING_AGE = 18
group = {'tim': 17, 'bob': 18, 'ana': 24}



def allowed_driving(name):
    """Print '{name} is allowed to drive' or '{name} is not allowed to drive'
       checking the passed in age against the MIN_DRIVING_AGE constant
       """
    is_found = False
    if name in group:
            if group[name] >= MIN_DRIVING_AGE:
                print(name + " is allowed to drive")
                is_found = True
            else:
                print(name + " is not allowed to drive")
                is_found = True
    return is_found

while True:
    print("Enter a name: (blank to quit)")
    name = str.casefold(input())
    if name == '':
        break

    if not allowed_driving(name):
        print("Name is not found")

