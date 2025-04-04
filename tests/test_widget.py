from typing import Union

import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card_number_and_name, masked_number",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ],
)
def test_mask_account_card_with_different_data(card_number_and_name: Union[str], masked_number: Union[str]) -> None:
    """Функция-тест, с помощью параметризации, проверяет корректность
    применения нужного типа маскировки входных данных."""
    assert mask_account_card(card_number_and_name) == masked_number


def test_mask_account_card_type() -> None:
    """Функция-тест, проверяет обработку некорректного типа входных данных."""
    with pytest.raises(TypeError, match='Ожидается формат ввода: "str".'):
        mask_account_card(000)  # type: ignore[arg-type]


def test_mask_account_card_wrong_value(wrong_answer: str) -> None:
    """Функция-тест, обрабатывает некорректные входные данные"""
    with pytest.raises(ValueError):
        mask_account_card(wrong_answer)


def test_get_date(date: str) -> None:
    """Функция-тест, обрабатывает правильность преобразования даты."""
    assert get_date(date) == "11.03.2024"


def test_get_date_wrong_value(incorrect_date: str) -> None:
    """Функция-тест, обрабатывает некорректные входные данные."""
    with pytest.raises(TypeError):
        get_date(incorrect_date)


def test_get_date_invalid(date_invalid: str) -> None:
    """Функция-тест, обрабатывает некорректный формат ввода даты."""
    with pytest.raises(ValueError):
        get_date(date_invalid)
