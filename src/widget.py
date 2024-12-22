from typing import Union
from masks import get_mask_card_number, get_mask_account


def mask_account_card(card_number_and_name: Union[str]) -> Union[str]:
    """
    Функция, которая принимает строку, содержащую тип и номер карты или счёта.
    Возвращает строку с замаскированным номером.
    :param card_number_and_name:
    :return:
    """
    if card_number_and_name[:4] in "Счет":
        return f'{str(card_number_and_name[:4])} {str(get_mask_account(card_number_and_name[-20:]))}'
    else:
        return f'{str(get_mask_card_number(card_number_and_name[-16:]))} {str(card_number_and_name[0:-16])}'

