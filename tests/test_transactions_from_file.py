from unittest.mock import MagicMock, patch

from src.transactions_from_file import get_transaction_from_csv, get_transaction_from_xlsx


def test_not_found_file_csv():
    result = get_transaction_from_csv("not_found_file.csv")
    assert result == []


@patch("pandas.read_csv")
def test_valid_csv(mock_read_csv):
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
    mock_read_csv.return_value = mock_df
    result = get_transaction_from_csv("valid_file.csv")

    assert result == [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]


def test_not_found_file_xlsx():
    result = get_transaction_from_xlsx("not_found_file.xlsx")
    assert result == []


@patch("pandas.read_excel")
def test_valid_xlsx(mock_read_xlsx):
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
    mock_read_xlsx.return_value = mock_df
    result = get_transaction_from_xlsx("valid_file.xlsx")

    assert result == [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
