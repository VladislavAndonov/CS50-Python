from fuel import convert, gauge
import pytest


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")


def test_divider_value():
    with pytest.raises(ValueError):
        convert("5/3")


def test_fraction():
    assert convert("1/2") == 50
    assert convert("1/5") == 20


def test_empty():
    assert gauge(1) == "E"


def test_full():
    assert gauge(99) == "F"


def test_percent():
    assert gauge(50) == "50%"
    assert gauge(9) == "9%"
