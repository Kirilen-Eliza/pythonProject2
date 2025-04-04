import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

def test_filter_by_currency_empty():
    """
    Функция-тест, обрабатывает ошибку, когда поданный на вход список, оказывается пустым.
    """
    with pytest.raises(ValueError, match='Список транзакций пуст.'):
        generator = filter_by_currency([{}], 'USD')
        next(generator)

@pytest.fixture
def transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]


@pytest.mark.parametrize("expected, currency", [([
                                                     {
                                                         "id": 939719570,
                                                         "state": "EXECUTED",
                                                         "date": "2018-06-30T02:08:58.425572",
                                                         "operationAmount": {
                                                             "amount": "9824.07",
                                                             "currency": {
                                                                 "name": "USD",
                                                                 "code": "USD"
                                                             }
                                                         },
                                                         "description": "Перевод организации",
                                                         "from": "Счет 75106830613657916952",
                                                         "to": "Счет 11776614605963066702"
                                                     },
                                                     {
                                                         "id": 142264268,
                                                         "state": "EXECUTED",
                                                         "date": "2019-04-04T23:20:05.206878",
                                                         "operationAmount": {
                                                             "amount": "79114.93",
                                                             "currency": {
                                                                 "name": "USD",
                                                                 "code": "USD"
                                                             }
                                                         },
                                                         "description": "Перевод со счета на счет",
                                                         "from": "Счет 19708645243227258542",
                                                         "to": "Счет 75651667383060284188"
                                                     },
{
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
    ], 'USD')])

def test_filter_by_currency_success(transactions, expected, currency):
    """
    Проверка, что функция корректно фильтрует транзакции по валюте.
    """
    generator = filter_by_currency(transactions, currency)
    assert list(generator) == expected

@pytest.fixture
def transactions_empty():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264260,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    ]

def test_transaction_descriptions_empty(transactions_empty):
    """
    Функция-тест, обрабатывает ошибки, когда описание по ключу не соответствует указанным ожиданиям
    """
    with pytest.raises(ValueError, match='Описание отсутствует.'):
        generator = transaction_descriptions(transactions_empty)
        next(generator)


@pytest.fixture
def transaction_expected():
    return ["Перевод организации",
            "Перевод со счета на счет",
            "Перевод со счета на счет",
            "Перевод с карты на карту",
            "Перевод организации"]

def test_transaction_descriptions_success(transactions, transaction_expected):
    """
    Проверка корректного извлечения описаний транзакций.
    """
    result = list(transaction_descriptions(transactions))
    assert result == transaction_expected


@pytest.fixture
def expected_card():
    return ["0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",]
def test_card_number_generator_valid(expected_card):
    """
    Проверка корректности выдачи номеров карт.
    """
    result = list(card_number_generator(1, 5))
    assert result == expected_card


def test_card_number_generator_edge_cases():
    """
    Проверка, что генератор корректно обрабатывает крайние значения диапазона.
    """
    # Проверка минимального значения
    result = list(card_number_generator(1, 1))
    expected = ["0000 0000 0000 0001"]
    assert result == expected, "Генератор некорректно обрабатывает минимальное значение"

    # Проверка максимального значения
    result = list(card_number_generator(9999999999999999, 9999999999999999))
    expected = ["9999 9999 9999 9999"]
    assert result == expected, "Генератор некорректно обрабатывает максимальное значение"


def test_card_number_generator_invalid_parameter():
    """
    Функция-тест, проверяет, то генератор корректно обрабатывает крайние
    значения диапазона.
    """
    with pytest.raises(ValueError, match='Значение диапазона некорректное.'):
        list(card_number_generator(0, 5))
    with pytest.raises(ValueError, match='Значение диапазона некорректное.'):
        list(card_number_generator(1, 10000000000000000))