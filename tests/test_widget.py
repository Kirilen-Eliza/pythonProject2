import pytest


from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("card_number_and_name, masked_number",
                         [('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
                         ('Счет 73654108430135874305', 'Счет **4305'),
                         ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
                         ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
                         ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229'),
                         ('Visa Gold 5999414228426353', 'Visa Gold 5999 41** **** 6353')])
def test_mask_account_card(card_number_and_name, masked_number):
    """Функция-тест, с помощью параметризации, проверяет корректность
    применения нужного типа маскировки входных данных."""
    assert mask_account_card(card_number_and_name) == masked_number


def test_mask_account_card_type():
    """Функция-тест, проверяет обработку некорректного типа входных данных."""
    with pytest.raises(TypeError, match='Ожидается формат ввода: "str".'):
        mask_account_card(000)


def test_mask_account_card_wrong_value(wrong_answer):
    """Функция-тест, обрабатывает некорректные входные данные"""
    with pytest.raises(ValueError):
        mask_account_card(wrong_answer)


def test_get_date(date):
    """Функция-тест, обрабатывает правильность преобразования даты."""
    assert get_date(date) == "11.03.2024"


def test_get_date_wrong_value(incorrect_date):
    """Функция-тест, обрабатывает некорректные входные данные."""
    with pytest.raises(TypeError):
        get_date(incorrect_date)


def test_get_date_invalid(date_invalid):
   """Функция-тест, обрабатывает некорректный формат ввода даты."""
   with pytest.raises(ValueError):
       get_date(date_invalid)

