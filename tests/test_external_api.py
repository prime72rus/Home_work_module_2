import os
from unittest.mock import patch

from src.external_api import api_convert_currency  # Замените 'your_module' на имя вашего модуля


@patch("requests.get")
def test_api_convert_currency_success(mock_get):
    os.environ["API_KEY"] = f"fake_api_key"
    mock_get.return_value.text = '{"result": 7500.0}'
    assert api_convert_currency("USD", "100") == 7500.0

    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        headers={"apikey": "fake_api_key"},
        params={"amount": "100", "from": "USD", "to": "RUB"}
    )