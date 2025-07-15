import pytest

from string_utils import StringUtils

string_utils = StringUtils()


@pytest.fixture
def utils():
    return StringUtils()


# Тесты для capitalize
def test_capitalize_positive(utils):
    assert utils.capitalize("skypro") == "Skypro"
    assert utils.capitalize("hello world") == "Hello world"
    assert utils.capitalize("123abc") == "123abc"
    assert utils.capitalize("") == ""


# Тесты для trim
def test_trim_positive(utils):
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("skypro") == "skypro"
    assert utils.trim("  hello  ") == "hello  "
    assert utils.trim("") == ""


def test_trim_negative(utils):
    assert utils.trim("   skypro") != "   skypro"
    assert utils.trim("skypro   ") != "skypro"


# Тесты для contains
def test_contains_positive(utils):
    assert utils.contains("SkyPro", "S") is True
    assert utils.contains("SkyPro", "k") is True
    assert utils.contains("SkyPro", "Pro") is True
    assert utils.contains("", "") is True


def test_contains_negative(utils):
    assert utils.contains("SkyPro", "U") is False
    assert utils.contains("", "a") is False
    assert utils.contains("SkyPro", "sky") is False


# Тесты для delete_symbol
def test_delete_symbol_positive(utils):
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"
    assert utils.delete_symbol("HelloWorld", "o") == "HellWrld"
    assert utils.delete_symbol("", "a") == ""
    assert utils.delete_symbol("Same", "nonexistent") == "Same"


def test_delete_symbol_negative(utils):
    assert utils.delete_symbol("SkyPro", "k") != "SkyPro"
    assert utils.delete_symbol("SkyPro", "Pro") != "SkyPro"
    assert utils.delete_symbol("HelloWorld", "o") != "HelloWorld"
