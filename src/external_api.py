import json
import os
from typing import Any

import requests
from dotenv import load_dotenv


def api_convert_currency(code: str, amount: str) -> Any:
    """
    Функция принимает на вход сод валюты и сумму операции, обращается к внешнему API
    для получения текущего курса валют и конвертации суммы операции в рубли.
    """
    load_dotenv()
    api_key = os.getenv("API_KEY")
    url = "https://api.apilayer.com/exchangerates_data/convert"

    payload = {"amount": amount, "from": code, "to": "RUB"}
    headers = {"apikey": api_key}

    response = requests.get(url, headers=headers, params=payload)

    # status_code = response.status_code
    result = json.loads(response.text)
    # convert_amount = json.loads(result)

    return result["result"]

print(api_convert_currency("USD", "100"))