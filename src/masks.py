from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> Union[str]:
    """
    Функция, которая принимает номер карты и возвращает её маску.
    :param card_number:
    :return:
    """
    if len(str(card_number)) >= 16:
        card_number_str = str(card_number)
        mask_card = card_number_str[0:6] + "*" * 6 + card_number_str[12:]
        result = " ".join([mask_card[i : i + 4] for i in range(0, len(mask_card), 4)])
        return str(result)
    else:
        raise ValueError("Отсутствует номер карты")


def get_mask_account(account: Union[int, str]) -> Union[str]:
    """
    Функция, которая принимает номер счёта и возвращает его маску.
    :param account:
    :return:
    """
    if len(str(account)) == 20:
        account_str = str(account)
        return f"{"**"}{account_str[-4:]}"
    else:
        raise ValueError("Длина строки не соответствует номеру счёта")
