import pytest

from src.widget import format_date_is_correct, get_date, mask_account_card


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("Visa 1230124562147856", "Visa 1230 12** **** 7856"),
        ("Счет 12345678912315478523", "Счет **8523"),
    ],
)
def test_mask_account_card(input_text, expected):
    assert mask_account_card(input_text) == expected


@pytest.mark.parametrize(
    "input_text_error",
    [
        "1234567891234567",
        "Visa 1234567567",
        "Visa 1234567567card",
        "Счет 1234567567365366card",
        "Счет 12345675673653648562698745",
        "Счет 1232",
        "23456756736536456215",
        "Master Card",
    ],
)
def test_mask_account_card_error(input_text_error):
    with pytest.raises(ValueError):
        mask_account_card(input_text_error)


@pytest.fixture
def empty():
    return ""


def test_mask_account_card_empty(empty):
    with pytest.raises(IndexError):
        mask_account_card(empty)


@pytest.fixture
def date():
    return "2024-03-11T02:26:18.671407"


def test_get_date(date):
    assert get_date(date) == "11.03.2024"


@pytest.mark.parametrize(
    "date_error",
    [
        "2024-03-11 02:26:18.671407",
        "24-03-11T02:26:18.671407",
        "2024-3-11T02:26:18.671407",
        "2024-03-11",
        "",
    ],
)
def test_get_date_error(date_error):
    with pytest.raises(ValueError):
        get_date(date_error)


def test_format_date_is_correct():
    assert format_date_is_correct("2024-03-11T02:26:18.671407") is True
    assert format_date_is_correct("2024-03-11") is False
    assert format_date_is_correct("") is False
