from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> Union[str]:
    """
    Функция, которая принимает номер карты и возвращает её маску.
    :param card_number:
    :return:
    """
    card_number_str = str(card_number)
    first_digits = card_number_str[0:4]
    second_digits = card_number_str[4:6] + "**"
    third_digits = "****"
    recent_figures = card_number_str[12:]
    return f"{first_digits} {second_digits} {third_digits} {recent_figures}"


def get_mask_account(account: Union[int, str]) -> Union[str]:
    """
    Функция, которая принимает номер счёта и возвращает его маску.
    :param account:
    :return:
    """
    account_str = str(account)
    first_digits = "**"
    recent_figures = account_str[16:]
    return f"{first_digits}{recent_figures}"
