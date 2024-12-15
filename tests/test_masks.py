import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_account_1():
    assert get_mask_account("12345678912345678912") == "**8912"
    assert get_mask_account("98765432198765432198") == "**2198"


def test_get_mask_card_number_1():
    assert get_mask_card_number("1234567891234567") == "1234 56** **** 4567"
    assert get_mask_card_number("9876543219876543") == "9876 54** **** 6543"


def test_get_mask_account_2():
    with pytest.raises(ValueError):
        get_mask_account("123456")


def test_get_mask_card_number_2():
    with pytest.raises(ValueError):
        get_mask_card_number("1232514523655588955258742")
