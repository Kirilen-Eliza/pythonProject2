import pytest

from src.generators import filter_by_currency

def test_filter_by_currency_empty():
    """Функция-тест, обрабатывает ошибку, когда поданный на вход список, оказывается пустым."""
    with pytest.raises(ValueError, match='Список транзакций пуст.'):
        generator = filter_by_currency([{}], 'USD')
        next(generator)

@pytest.fixture
def transactions():
    return [
        {
            'id': 1,
            'operationAmount': {
                'amount': '100',
                'currency': {
                    'code': 'USD'
                }
            }
        },
        {
            'id': 2,
            'operationAmount': {
                'amount': '200',
                'currency': {
                    'code': 'RUB'
                }
            }
        },
        {
            'id': 3,
            'operationAmount': {
                'amount': '300',
                'currency': {
                    'code': 'USD'
                }
            }
        },
    ]


@pytest.mark.parametrize("expected, currency", [([
        {
            'id': 1,
            'operationAmount': {
                'amount': '100',
                'currency': {
                    'code': 'USD'
                }
            }
        },
        {
            'id': 3,
            'operationAmount': {
                'amount': '300',
                'currency': {
                    'code': 'USD'
                }
            }
        },
    ], 'USD')])

def test_filter_by_currency_success(transactions, expected, currency):
    """Проверка, что функция корректно фильтрует транзакции по валюте."""
    generator = filter_by_currency(transactions, currency)
    assert list(generator) == expected

