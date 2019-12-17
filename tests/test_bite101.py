from intro_py_bites.bite101_test_practice import allowed_driving


def test_not_allowed_to_drive(capfd):
    allowed_driving('tim', 17)
    output = capfd.readouterr()[0].strip()
    assert output == 'tim is not allowed to drive'


def test_allowed_to_drive(capfd):
    allowed_driving('bob', 18)
    output = capfd.readouterr()[0].strip()
    assert output == 'bob is allowed to drive'


def test_allowed_to_drive_other_name(capfd):
    allowed_driving('ana', 24)
    output = capfd.readouterr()[0].strip()
    assert output == 'ana is allowed to drive'