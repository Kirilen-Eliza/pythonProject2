from typing import Union

from masks import get_mask_account, get_mask_card_number


def mask_account_card(card_number_and_name: Union[str]) -> Union[str]:
    """
    Функция, которая принимает строку, содержащую тип и номер карты или счёта.
    Возвращает строку с замаскированным номером.
    :param card_number_and_name:
    :return:
    """
    if card_number_and_name[:4] in "Счет":
        account_name = str(card_number_and_name[:4])
        account_number = str(get_mask_account(card_number_and_name[-20:]))
        return f'{account_name} {account_number}'
    else:
        card_name = str(card_number_and_name[0:-16])
        card_number = str(get_mask_card_number(card_number_and_name[-16:]))
        return f'{card_name}{card_number}'


def get_date(date: Union[str]) -> Union[str]:
    """
    Функция, которая принимает строку с датой и точным временем
    и возвращает строку в формате 'ДД.ММ.ГГГГ'
    :param date:
    :return:
    """
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
