from typing import Any, Hashable

import pandas as pd


def get_transaction_from_csv(csv_file_path: str) -> list[dict[Hashable, Any]]:
    """
    Функция для считывания финансовых операций из CSV-файла. Принимает путь к файлу CSV в качестве аргумента
    и возвращает список словарей с транзакциями.
    """
    try:
        df = pd.read_csv(csv_file_path, sep=";")
        transactions = df.to_dict(orient="records")
        return transactions

    except FileNotFoundError:
        print(f"Ошибка: Файл {csv_file_path} не найден.")
        return []


def get_transaction_from_xlsx(xlsx_file_path: str) -> list[dict[Hashable, Any]]:
    """
    Функция для считывания финансовых операций из XLSX-файла. Принимает путь к файлу XLSX в качестве аргумента
    и возвращает список словарей с транзакциями.
    """
    try:
        df = pd.read_excel(xlsx_file_path)
        transactions = df.to_dict(orient="records")
        return transactions

    except FileNotFoundError:
        print(f"Ошибка: Файл {xlsx_file_path} не найден.")
        return []
