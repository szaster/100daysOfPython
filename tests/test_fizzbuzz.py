import pytest

from py_test_exercises.fizz_buzz import fizzbuzz


@pytest.mark.parametrize("arg, ret", [ # @ is a decorator
    (1, 1),
    (2, 2),
    (3, 'Fizz'),
    (4, 4),
    (5, 'Buzz'),
    (6, 'Fizz'),
    (7, 7),
    (8, 8),
    (9, 'Fizz'),
    (10, 'Buzz'),
    (11, 11),
    (12, 'Fizz'),
    (13, 13),
    (14, 14),
    (15, 'Fizz Buzz'),
])
def test_fizzbuzz(arg, ret):
    assert fizzbuzz(arg) == ret
