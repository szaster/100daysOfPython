from py_test_exercises.ex1 import hello_people, square_root


def test_hello_people_returns_correct_greeting():
    name = "Joe"
    assert hello_people(name) == f'Hello {name}!'


def test_square_root_returns_correct_answer_for_positive():
    number = 81
    assert square_root(number) == 9

#def test_square_root_returns_correct_answer_for_negative():
 #   number = 81
  #  assert square_root(number) == 9i
