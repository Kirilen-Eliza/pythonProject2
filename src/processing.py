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
