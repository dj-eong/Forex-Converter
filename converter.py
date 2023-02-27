from currency_symbols import CurrencySymbols
import requests


def get_currency_codes():
    response = requests.get('https://api.exchangerate.host/symbols')
    data = response.json()
    return set(data['symbols'].keys())


def are_valid_inputs(currency_from, currency_to, amount):
    if not amount.replace('.', '').isnumeric() or float(amount) <= 0:
        return False

    currency_codes = get_currency_codes()
    if currency_from not in currency_codes or currency_to not in currency_codes:
        return False

    return True


def get_converted_amount(currency_from, currency_to, amount):
    url = f'https://api.exchangerate.host/convert?from={currency_from}&to={currency_to}&amount={amount}'
    response = requests.get(url)
    data = response.json()

    currency_symbol = CurrencySymbols.get_symbol(currency_to)
    result = currency_symbol + str(round(data['result'], 2)) if currency_symbol else str(round(
        data['result'], 2))
    return result
