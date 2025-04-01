from typing import Union


def filter_by_state(transactions: Union[list], state: Union[str] = "EXECUTED") -> Union[list]:
    """
    Функция принимает список словарей и опционально значение для ключа
    state (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей,
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


def sort_by_date(transactions: Union[list], ascending: Union[bool] = True) -> Union[list]:
    """
    Функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание). Возвращающая новый список словарей, отсортированный по дате.
    :param transactions:
    :param ascending:
    :return:
    """
    for transaction in transactions:
        if not isinstance(transaction["date"], str):
            raise TypeError("Дата должна быть строкой")
    return sorted(transactions, key=lambda date: date.get("date"), reverse=ascending)
