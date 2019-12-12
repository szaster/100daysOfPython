NOT_FOUND = "Not found"

group1 = {'tim': 30, 'bob': 17, 'ana': 24}
group2 = {'ana': 26, 'thomas': 64, 'helen': 26}
group3 = {'brenda': 17, 'otto': 44, 'thomas': 46}

groups = [group3, group2, group1]
print(groups)


def get_person_age(name):
    """Look up name (case insensitive search) and return age.
       If name in > 1 dict, return the match of the group with
       greatest N (so group3 > group2 > group1).
       Return true if name is found. Otherwise false.
    """
    is_found = False
    for group in groups:
        if name in group:
            # name = group1.keys()
            # age = group1.values()
            print(name + ' is ' + str(group[name]) + ' years old.')
            is_found = True
            break
    return is_found


while True:
    print("Enter a name: (blank to quit)")
    name = input()
    if name == '':
        break

    if not get_person_age(name):
        print("Name is not found")
