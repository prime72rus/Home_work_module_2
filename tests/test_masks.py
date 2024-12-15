from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_account():
    assert get_mask_account("12345678912345678912") == "**8912"
    assert get_mask_account("98765432198765432198") == "**2198"


def test_get_mask_card_number():
    assert get_mask_card_number("1234567891234567") == "1234 56** **** 4567"
    assert get_mask_card_number("9876543219876543") == "9876 54** **** 6543"
