from typing import List, Dict, Any, Generator

def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Generator[Dict, None, None]:
    """Генератор, который принимает список словарей и возвращает только операции с валютой `currency`.

    :param transactions: Список транзакций.
    :param currency: Код валюты для фильтрации (например, 'USD', 'RUB').
    :return: Генератор транзакций с указанной валютой.
    """
    for transaction in transactions:
        # Проверяем, есть ли информация о валюте и соответствует ли она заданной
        operation_amount = transaction.get('operationAmount', {})
        transaction_currency = operation_amount.get('currency', {})
        if operation_amount and transaction_currency != {}:
            if transaction_currency.get('code') == currency:
                yield transaction
        else:
            raise ValueError('Список транзакций пуст.')


def transaction_descriptions(transactions: List[Dict]) -> Generator[str, None, None]:
    """Генератор, который принимает список словарей с транзакциями и
    возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        description = transaction.get('description')
        if description is None:
            raise ValueError('Описание отсутствует.')
        yield description




