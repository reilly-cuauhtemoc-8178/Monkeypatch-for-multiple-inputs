"""Mocking input with monkeypatch"""

import pytest


def mock_in():
    # Takes two inputs and divides them. Does not return a value.
    x = input("query 1")
    y = input("query 2")
    z = x / y

@pytest.mark.parametrize("input, expected", [
    ([3], StopIteration),           # Not enough values for input
    ([1, 0], ZeroDivisionError),    # Values that result in zero division
    (['a', 'b'], TypeError)         # Values are incorrect type
    ])
def test_mock_in(monkeypatch, input, expected):
    # Make a generator from a list of values provided by parametrize
    mark_gen = (i for i in input)

    # Gets next item in generator for each time input() is required
    monkeypatch.setattr('builtins.input', lambda x: next(mark_gen))

    with pytest.raises(expected):
        mock_in()
