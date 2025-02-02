from typing import Iterable


def filter_by_state(transactions: list, state: str = "EXECUTED") -> Iterable[list]:
    """
    Функция принимает список словарей и опционально значение для ключа
    state(по умолчанию 'EXECUTED'). Функция возвращает новый список словарей,
    содержащий только те словари, у которых ключ state соответствует указанному значению.
    :param transactions: Список словарей с транзакциями.
    :param state: Значение ключа "state" по умолчанию.
    :return:
    """
    new_list = []
    for transaction in transactions:
        if transaction.get("state") == state:
            new_list.append(transaction)
    return new_list


def sort_by_date(transactions: list, ascending: bool = True) -> Iterable[list]:
    """
    Функция возвращающая новый список словарей, отсортированный по дате.
    :param transactions:
    :param ascending:
    :return:
    """
    sort_list = sorted(transactions, key=lambda x: x.get("date"), reverse=ascending)
    return sort_list
