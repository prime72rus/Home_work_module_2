import pytest

from src.generators import filter_by_currency, transaction_descriptions


@pytest.fixture
def test_data():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "RU", "code": "RU"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 939719571,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод частному лицу",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 939719572,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 939719573,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "RU", "code": "RU"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 939719574,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 939719575,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод частному лицу",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 939719576,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "RU", "code": "RU"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
    ]


def test_filter_by_currency_1(test_data):
    gen_filter_by_currency = filter_by_currency(test_data, "RU")
    assert next(gen_filter_by_currency) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "RU", "code": "RU"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(gen_filter_by_currency) == {
        "id": 939719573,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "RU", "code": "RU"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(gen_filter_by_currency) == {
        "id": 939719576,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "RU", "code": "RU"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    with pytest.raises(StopIteration):
        next(gen_filter_by_currency)

def test_filter_by_currency_2():
    gen_filter_by_currency = filter_by_currency([], "RU")
    with pytest.raises(StopIteration):
        next(gen_filter_by_currency)


def test_filter_by_currency_3(test_data):
    gen_filter_by_currency = filter_by_currency(test_data, "EUR")
    with pytest.raises(StopIteration):
        next(gen_filter_by_currency)


def test_transaction_descriptions_1(test_data):
    gen_transaction_descriptions = transaction_descriptions(test_data)
    assert next(gen_transaction_descriptions) == "Перевод организации"
    assert next(gen_transaction_descriptions) == "Перевод частному лицу"
    assert next(gen_transaction_descriptions) == "Перевод организации"
    assert next(gen_transaction_descriptions) == "Перевод организации"
    assert next(gen_transaction_descriptions) == "Перевод организации"
    assert next(gen_transaction_descriptions) == "Перевод частному лицу"
    assert next(gen_transaction_descriptions) == "Перевод организации"
    with pytest.raises(StopIteration):
        next(gen_transaction_descriptions)


def test_transaction_descriptions_2(test_data):
    gen_transaction_descriptions = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(gen_transaction_descriptions)
