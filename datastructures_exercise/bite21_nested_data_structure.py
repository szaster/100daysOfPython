cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']}


#print(cars.keys())


def get_all_jeeps():
    #"""return a comma  + space (', ') separated string of jeep models
     #      (original order)"""
#for keys in cars:
    #if cars.keys() == cars['Jeep']:
    s = ', '
    print(s.join(cars['Jeep']))

get_all_jeeps()

def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    pass


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    pass


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    pass


#while True:
#   if not get_all_jeeps(car):
#        print("Car is not found")
#        break
