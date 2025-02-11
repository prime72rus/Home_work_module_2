import pytest
from unittest.mock import patch, mock_open

from src.utils import get_operations_from_file
from src.utils import get_amount_transactions

mocked_valid_json_content = '[{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]'
mocked_invalid_json_content = '{"key": "value"}'
mocked_corrupted_json_content = "invalid json content"

@patch("os.path.isfile", return_value=False)
def test_get_operations_from_file_nonexistent_file(mock_isfile):
    result = get_operations_from_file("non_existent_file.json")
    assert result == []
    mock_isfile.assert_called_once_with("non_existent_file.json")


@patch("os.path.isfile", return_value=True)
@patch("os.path.getsize", return_value=0)
def test_get_operations_from_file_empty_file(mock_getsize, mock_isfile):
    result = get_operations_from_file("empty_file.json")
    assert result == []
    mock_isfile.assert_called_once_with("empty_file.json")
    mock_getsize.assert_called_once_with("empty_file.json")


@patch("os.path.isfile", return_value=True)
@patch("os.path.getsize", return_value=len(mocked_valid_json_content))
@patch("builtins.open", new_callable=mock_open, read_data=mocked_valid_json_content)
def test_get_operations_from_file_valid_list(mock_file, mock_getsize, mock_isfile):
    result = get_operations_from_file("valid_list.json")
    expected_result = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    assert result == expected_result
    mock_isfile.assert_called_once_with("valid_list.json")
    mock_getsize.assert_called_once_with("valid_list.json")
    mock_file.assert_called_once_with("valid_list.json", encoding="utf-8")


@patch("os.path.isfile", return_value=True)
@patch("os.path.getsize", return_value=len(mocked_invalid_json_content))
@patch("builtins.open", new_callable=mock_open, read_data=mocked_invalid_json_content)
def test_get_operations_from_file_invalid_content(mock_file, mock_getsize, mock_isfile):
    result = get_operations_from_file("invalid_content.json")
    assert result == []
    mock_isfile.assert_called_once_with("invalid_content.json")
    mock_getsize.assert_called_once_with("invalid_content.json")
    mock_file.assert_called_once_with("invalid_content.json", encoding="utf-8")


@patch("os.path.isfile", return_value=True)
@patch("os.path.getsize", return_value=len(mocked_corrupted_json_content))
@patch("builtins.open", new_callable=mock_open, read_data=mocked_corrupted_json_content)
def test_get_operations_from_file_malformed_json(mock_file, mock_getsize, mock_isfile):
    result = get_operations_from_file("malformed_json.json")
    assert result == []
    mock_isfile.assert_called_once_with("malformed_json.json")
    mock_getsize.assert_called_once_with("malformed_json.json")
    mock_file.assert_called_once_with("malformed_json.json", encoding="utf-8")


mocked_api_responses = {
    ("USD", "100"): 7500.0,
    ("EUR", "50"): 4500.0,
}

def mock_api_convert_currency(code, amount):
    return mocked_api_responses.get((code, amount), 0.0)

@pytest.mark.parametrize(
    "transactions, expected_amount",
    [
        (
            [
                {"operationAmount": {"amount": "1000.50", "currency": {"code": "RUB"}}},
                {"operationAmount": {"amount": "2000.75", "currency": {"code": "RUB"}}},
            ],
            3001.25,
        ),
        (
            [
                {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}},
                {"operationAmount": {"amount": "50", "currency": {"code": "EUR"}}},
            ],
            12000.0,
        ),
        (
            [
                {"operationAmount": {"amount": "500", "currency": {"code": "RUB"}}},
                {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}},
                {"operationAmount": {"amount": "50", "currency": {"code": "EUR"}}},
            ],
            12500.0,
        ),
        ([], 0.0),
        (
            [
                {"operationAmount": {"amount": "1000", "currency": {}}},
                {"operationAmount": {"amount": "", "currency": {"code": "USD"}}},
                {"operationAmount": {"amount": "abc", "currency": {"code": "RUB"}}},
                {"operationAmount": {"amount": "100", "currency": {"code": "XYZ"}}},
            ],
            0.0,
        ),
        (
            [
                {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}},
                {"operationAmount": {"amount": "xyz", "currency": {"code": "EUR"}}},
            ],
            7500.0,
        ),
        (
            [
                {"operationAmount": {"amount": "", "currency": {"code": "RUB"}}},
                {"operationAmount": {"amount": "200", "currency": {"code": "RUB"}}},
            ],
            200.0,
        ),
        (
            [
                {"operationAmount": {"currency": {"code": "RUB"}}},
                {"operationAmount": {"amount": "300", "currency": {"code": "RUB"}}},
            ],
            300.0,
        ),
    ],
)
@patch("src.utils.api_convert_currency", side_effect=mock_api_convert_currency)
def test_get_amount_transactions(mock_api, transactions, expected_amount):
    result = get_amount_transactions(transactions)
    assert result == expected_amount
