from twttr import shorten
import pytest


def test_vowels():
    assert shorten("Facetious") == "Fcts"
    assert shorten("Automobile") == "tmbl"


def test_punctuation():
    assert shorten("Hello!") == "Hll!"
    assert shorten("What's your name?") == "Wht's yr nm?"


def test_type():
    assert shorten("2pac") == "2pc"
    assert shorten("June 1st") == "Jn 1st"
