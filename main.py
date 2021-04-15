import requests
import os

from dotenv import load_dotenv
from urllib.parse import urlparse

def shorten_link(url, headers, params):
    response = requests.post(url, headers=headers, json=params)
    response.raise_for_status()
    bitlink = response.json()['id']
    return bitlink


def count_clicks(url, headers, link):
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    clicks_count = response.json()
    return clicks_count['total_clicks']


def start():
    load_dotenv()
    bitly_token = os.getenv('BITLY_TOKEN')

    bitly_url = 'https://api-ssl.bitly.com/v4/shorten'
    link = input('Введите ссылку\n')
    fragments_link = urlparse(link)
    fragments_link = fragments_link.netloc + fragments_link.path

    load_url = {
        'long_url': link
    }

    headers = {
        'Authorization': bitly_token,
    }

    click_url = f'https://api-ssl.bitly.com/v4/bitlinks/{fragments_link}/clicks/summary'

    params = {
        'unit': 'day'
    }


    if fragments_link.startswith('bit.ly'):
        try:
            print('Количество переходов по ссылке:', count_clicks(click_url, headers,params))
        except requests.exceptions.HTTPError:
            print('*** ERROR * ERROR *ERROR ***\nВы ввели неверную сокращенную ссылку')
    elif fragments_link.startswith('bit.ly')==False:
        try:
            print('Битлинк', shorten_link(bitly_url, headers, load_url))	
        except requests.exceptions.HTTPError:
            print('*** ERROR * ERROR * ERROR ***\nВы ввели неверную ссылку')


if __name__ == '__main__':
    start()