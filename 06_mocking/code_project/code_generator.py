import random
from datetime import date


def get_code():
    number = random.randint(0, 9)
    return f'XC-{number}'


def get_today_name():
    return date.today().strftime('%a')


def get_code_with_day():
    code = get_code()
    today = get_today_name().upper()
    return f'{code}-{today}'
