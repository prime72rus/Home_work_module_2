import json
import os

import requests
from dotenv import load_dotenv


def api_convert_currency(code: str, amount: str) -> float:
    load_dotenv()
    api_key = os.getenv("API_KEY")
    url = "https://api.apilayer.com/exchangerates_data/convert"

    payload = {
        "amount": amount,
        "from": code,
        "to": "RUB"
    }
    headers= {
        "apikey": api_key
    }

    response = requests.request("GET", url, headers=headers, params=payload)

    # status_code = response.status_code
    result = response.text
    convert_amount = json.loads(result)

    return convert_amount.get("result")
