from bank import value
import pytest

def test_value():
    assert value("hello") == 0
    assert value("howdy") == 20
    assert value("what's up") == 100

def test_case():
    assert value("Hello there!") == 0
    assert value("Hey") == 20
