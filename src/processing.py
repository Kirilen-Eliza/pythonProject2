from typing import Union


def filter_by_state(list_transactions: list, state: str = "EXECUTED") -> Union[list]:
    """
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    :param list_transactions: Список словарей с транзакциями.
    :param state: Значение ключа "state" по умолчанию.
    :return:
    """
    new_list = []
    for transaction in list_transactions:
        if transaction.get("state") == state:
            new_list.append(transaction)
    return new_list


def sort_by_date(list_transactions: list, ascending: bool = True) -> Union[list]:
    """
    Функция возвращающая новый список словарей, отсортированный по дате.
    :param list_transactions:
    :param ascending:
    :return:
    """
    sort_new_list = sorted(list_transactions, key=lambda x: x.get("date"), reverse=ascending)
    return sort_new_list
