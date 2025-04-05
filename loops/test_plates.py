from plates import is_valid
import pytest


def test_startswith_two_letters():
    assert is_valid("LIVE90") == True
    assert is_valid("2PAC") == False
    assert is_valid("V12") == False


def test_length():
    assert is_valid("BATMAN") == True
    assert is_valid("SPIDERMAN") == False
    assert is_valid("G") == False


def test_chars():
    assert is_valid("NICE!") == False
    assert is_valid("MONEY$") == False


def test_zero():
    assert is_valid("CS50") == True
    assert is_valid("HELL01") == False


def test_endswith_digits():
    assert is_valid("LOVE69") == True
    assert is_valid("IM25YO") == False
