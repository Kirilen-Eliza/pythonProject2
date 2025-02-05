import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("card_number, disguised_number",
                         [(7000792289606361, '7000 79** **** 6361'),
                         (70007922896063622542, '7000 79** **** 6362 2542'),
                         (7000792289606363659463, '7000 79** **** 6363 6594 63')])
def test_get_mask_card_number(card_number, disguised_number):
    """Функция-тест, с помощью параметризации, проверяет корректность
    маскировки номера карт, в том числе разной длинной."""
    assert get_mask_card_number(card_number) == disguised_number


def test_get_mask_card_number_wrong_type():
    """Функция-тест, проверяет функцию на корректность обработки ошибки,
     когда на входной строке отсутствует номер карты."""
    with pytest.raises(ValueError):
        get_mask_card_number('0')
        

def test_get_mask_account(account):
    """Функция-тест, проверяет корректность маскировки номера счёта."""
    assert get_mask_account(account) == '**4305'


def test_get_mask_account_wrong_type():
    """Функция-тест, проверяет функцию на корректность обработки ошибки,
     когда на входной строке номер счёта не соответствует длине."""
    with pytest.raises(ValueError):
        get_mask_account('0')








