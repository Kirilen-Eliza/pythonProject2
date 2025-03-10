from typing import Iterable


def filter_by_state(transactions: list, state: str = "EXECUTED") -> Iterable[list | str]:
    """
    Функция принимает список словарей и опционально значение для ключа
    state (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей,
    содержащий только те словари, у которых ключ state соответствует указанному значению.
    :param transactions: Список словарей с транзакциями.
    :param state: Значение ключа "state" по умолчанию.
    :return:
    """
    new_list = []
    if state in transactions:
        for transaction in transactions:
            if transaction.get("state") == state:
                new_list.append(transaction)
        return new_list
    else:
        raise ValueError('В списке словарей не найден заданный ключ')


def sort_by_date(transactions: list, ascending: bool = True) -> Iterable[list]:
    """
    Функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание). Возвращающая новый список словарей, отсортированный по дате.
    :param transactions:
    :param ascending:
    :return:
    """
    for data in transactions:
        if not isinstance(data['date'], str):
            raise TypeError('Дата должна быть строкой')
    return sorted(transactions, key=lambda x: x.get("date"), reverse=ascending)
