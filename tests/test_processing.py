import pytest


from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(transactions):
    """Функция-тест, тестирует список словарей по заданному параметру
    по умолчанию 'state'."""
    assert filter_by_state(transactions) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


def test_filter_by_state_2(transactions):
    """Функция-тест, тестирует вывод списков словарей по заданному параметру
    при вызове функции."""
    assert filter_by_state(transactions, 'CANCELED') == [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

def test_filter_by_state_lack_of_status(transactions):
    """Функция-тест, проверяет обработку случаев, когда в списке
    отсутствует словарь с указанным статусом."""
    with pytest.raises(ValueError):
        assert filter_by_state(transactions, 'TRALALA')


def test_sort_by_date(transactions):
    """Функция-тест, тестирует обработку сортировки по дате по-умолчанию."""
    assert sort_by_date(transactions) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


def test_sort_by_date_false(transactions):
    """Функция-тест, тестирует обработку сортировки по противоположному направлению от умолчания."""
    assert sort_by_date(transactions, False) == [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]


def test_sort_by_date_type():
    """Функция-тест, обрабатывает исключение, когда дата в словаре не строка."""
    with pytest.raises(TypeError):
        assert sort_by_date([{'id': 594226727, 'state': 'EXECUTED', 'date': 20180912}])