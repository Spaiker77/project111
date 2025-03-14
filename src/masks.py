from typing import Union


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Функиция принимает на вход номер карты и возвращает ее маску"""
    return f"{card_number[:4]}{card_number[4:6]}** **** {card_number[-4:]}"


print(get_mask_card_number("7000792289606361"))


def get_mask_account(account: Union[str]) -> Union[str]:
    """Функция принимает на вход номер счета и возвращает его маску"""
    return f"** {account[-4:]}"


print(get_mask_account("73654108430133874305"))
