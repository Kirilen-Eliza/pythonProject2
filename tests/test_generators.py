import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

def test_filter_by_currency_empty():
    """Функция-тест, обрабатывает ошибку, когда поданный на вход список, оказывается пустым."""
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
                    "name": "RUS",
                    "code": "RUS"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
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
            "description": "Перевод с карты на карту",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
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
                                                         "description": "Перевод с карты на карту",
                                                         "from": "Счет 19708645243227258542",
                                                         "to": "Счет 75651667383060284188"
                                                     },
    ], 'USD')])

def test_filter_by_currency_success(transactions, expected, currency):
    """Проверка, что функция корректно фильтрует транзакции по валюте."""
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
    """Функция-тест, обрабатывает ошибки, когда описание по ключу не соответствует указанным ожиданиям"""
    with pytest.raises(ValueError, match='Описание отсутствует.'):
        generator = transaction_descriptions(transactions_empty)
        next(generator)


def test_transaction_descriptions_success(transactions):
    """Проверка корректного извлечения описаний транзакций."""
    result = list(transaction_descriptions(transactions))
    expected = ["Перевод организации", "Перевод со счета на счет", "Перевод с карты на карту"]
    assert result == expected


@pytest.fixture
def expected_card():
    return ["0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",]
def test_card_number_generator_valid(expected_card):
    """Проверка корректности выдачи номеров карт."""
    result = list(card_number_generator(1, 5))
    assert result == expected_card


def test_card_number_generator_invalid_parameter():
    """"""
    with pytest.raises(ValueError):
        list(card_number_generator(0, 5))
    with pytest.raises(ValueError):
        list(card_number_generator(1, 10000000000000000))