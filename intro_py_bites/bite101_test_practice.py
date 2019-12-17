MIN_DRIVING_AGE = 18
group = {'tim': 17, 'bob': 18, 'ana': 24}


#def allowed_driving(thisgroup):
   # """Print '{name} is allowed to drive' or '{name} is not allowed to drive'
      # checking the passed in age against the MIN_DRIVING_AGE constant
    #   """
 #   for name in thisgroup:
  #      if thisgroup[name] >= MIN_DRIVING_AGE:
   #         print(name + " is allowed to drive")
    #    else:
     #       print(name + " is not allowed to drive")
def allowed_driving(name, age):
    """Print '{name} is allowed to drive' or '{name} is not allowed to drive'
       checking the passed in age against the MIN_DRIVING_AGE constant"""
    is_allowed = 'is allowed' if age >= MIN_DRIVING_AGE else 'is not allowed'
    print(f'{name} {is_allowed} to drive')

allowed_driving('kok' , 89)