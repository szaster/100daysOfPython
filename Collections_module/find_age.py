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
            print(name + ' is ' + str(group[name]) + ' years old.')
            is_found = True
            break
    return is_found


while True:
    print("Enter a name: (blank to quit)")
    name = str.casefold(input())
    if name == '':
        break

    if not get_person_age(name):
        print("Name is not found")


    def test_regular_name():
        assert get_person_age('tim') == 30
        assert get_person_age('helen') == 26
        assert get_person_age('otto') == 44

    def test_case_insensitive_lookup():
        assert get_person_age('Tim') == 30
        assert get_person_age('BOB') == 17
        assert get_person_age('BrEnDa') == 17

    def test_name_not_found():
        assert get_person_age('timothy') == NOT_FOUND
        assert get_person_age(None) == NOT_FOUND
        assert get_person_age(False) == NOT_FOUND
        assert get_person_age(-1) == NOT_FOUND

    def test_duplicate_name():
        assert get_person_age('thomas') == 46
        assert get_person_age('ana') == 26