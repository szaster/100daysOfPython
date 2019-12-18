from intro_py_bites.bite102_infloop_v2 import read_color


def fake_input_function():
    return "GreY"


def test_read_color():
    expected = "grey"
    actual = read_color(fake_input_function)
    assert expected == actual


def test_is_quit():
    expected = "grey"
    actual = read_color(fake_input_function)
    assert expected == actual