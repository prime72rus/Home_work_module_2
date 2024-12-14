import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("Visa 1234567891234567", "Visa 1234 56** **** 4567"),
        ("1234567891234567", "Ошибка"),
        ("Visa 1234567567", "Ошибка"),
        ("Visa 1234567567card", "Ошибка"),
        ("Счет 1234567567365366card", "Ошибка"),
        ("Счет 12345678912345678945", "Счет **8945"),
        ("Счет 12345675673653648562698745", "Ошибка"),
        ("23456756736536456215", "Ошибка"),
        ("Master Card", "Ошибка"),
        ("Мир 4276452136544589", "Мир 4276 45** **** 4589"),
    ],
)
def test_mask_account_card(input_text, expected):
    assert mask_account_card(input_text) == expected


@pytest.fixture
def date():
    return "2024-03-11T02:26:18.671407"


def test_get_date(date):
    assert get_date(date) == "11.03.2024"
