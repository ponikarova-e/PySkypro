import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    (" Skypro", "Skypro"),
    (" Hello world", "Hello world"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


def test_contains_positive():
    assert string_utils.contains("SkyPro", "S") is True


def test_delete_symbol_positive():
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("SkyPro", "SkyPro"),  #  строка уже обрезанная
    ("", ""),  # пустая строка
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


def test_contains_negative():
    assert string_utils.contains("SkyPro", "U") is False


@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize("input_str, expected", [
    ("Skypro", "z"),  # несуществующий символ
    ("", "S"),  # пустая строка
])
def test_delete_symbol_negative(input_str, expected):
    assert string_utils.delete_symbol(input_str) == expected
