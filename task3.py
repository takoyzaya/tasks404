import requests
import json


def get_name_by_code(code='SG'):
    return json.loads(
        requests.get(
            f'https://restcountries.eu/rest/v2/alpha/{code}').text
    )['name']


def get_code_by_name(name='Viet Nam'):
    return json.loads(
        requests.get(
            f'https://restcountries.eu/rest/v2/name/{name}').text
    )[0]['alpha2Code']


res = {}
res[get_name_by_code('SG')] = 'SG'
res['Viet Nam'] = get_code_by_name('Viet Nam')