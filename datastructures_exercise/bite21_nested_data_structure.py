from collections import OrderedDict

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']}


def case_insensitive_contains(container, substring):
    lower_case_substring = substring.casefold() # converts substring to lowercase
    lower_case_container = container.casefold() # converts string to lowercase
    return lower_case_container.find(lower_case_substring) >= 0 # finds substring in string


def get_all_matching_models(car_db, grep):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    a = []
    for model in car_db:
        for element in car_db[model]:
            #if case_insensitive_contains(element, grep):
            lower_case_substring = grep.casefold()  # converts substring to lowercase
            lower_case_container = element.casefold()  # converts string to lowercase
            if lower_case_container.find(lower_case_substring) >= 0:  # finds substring in string
                a.append(element)
    a.sort()
    return a


def check(car_db):
    for model in car_db:
        for element in car_db[model]:
            print(element)


#print(check(cars))
print("trail: ", get_all_matching_models(cars, 'Trail'))


def get_first_model_each_manufacturer(car_db):
    """return a list of matching models (original ordering)"""
    a = []
    for make in car_db:
        a.append(car_db[make][0])
    return a



def sort_car_models(car_db):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    sorted_db = {}
    for model in car_db:
        sorted_db[model] = sorted(car_db[model])
    return sorted_db


print(sort_car_models(cars))



def get_all_jeeps(car_db):
    # """return a comma  + space (', ') separated string of jeep models
    #      (original order)"""
    a = ', '.join(car_db['Jeep'])
    return a


jeeps = get_all_jeeps(cars)
print(jeeps)



def better_get_first_model_each_manufacturer(car_db):
    """Uses map function and lambda to avoid code with side effects."""
    result = map(lambda x: x[0], car_db.values())
    # convert map to list
    return list(result)


print(get_first_model_each_manufacturer(cars))
print("Better way: ", better_get_first_model_each_manufacturer(cars))


