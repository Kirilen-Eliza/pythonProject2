from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(card_number_and_name: [str]) -> [str]:
    """
    Функция, которая принимает строку, содержащую тип и номер карты или счёта.
    Возвращает строку с замаскированным номером.
    :param card_number_and_name:
    :return:
    """
    if type(card_number_and_name) is not str:
        raise TypeError('Ожидается формат ввода: "str".')

    elif card_number_and_name[:4] in "Счет" :
        account_number = get_mask_account(card_number_and_name[5:])
        return f'{card_number_and_name[:4]} {account_number}'
    else:
        card_name = card_number_and_name[0:-16]
        card_number = get_mask_card_number(card_number_and_name[-16:])
        return f'{card_name}{card_number}'
#print(mask_account_card('Счет 73654108430135874305'))

def get_date(date: [str]) -> [str]:
    """
    Функция, которая принимает строку с датой и точным временем
    и возвращает строку в формате 'ДД.ММ.ГГГГ'
    :param date:
    :return:
    """
    if type(date) is not str:
        raise TypeError('Ожидается тип данных: строка')
    if date[4] == '-' and date[7] == '-':
        return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
    else:
        raise ValueError('Не верный формат даты, ожидается ГГГГ.ММ.ДД')
#print(get_date("2024-03-11T02:26:18.671407"))