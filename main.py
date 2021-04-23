import requests
import os
import argparse

from dotenv import load_dotenv
from urllib.parse import urlparse


def get_link():
    parser = argparse.ArgumentParser(description='''
        Алоха! Данная программа принимает один параметр - ссылку, 
        и возвращает либо сокращенную ссылку, 
        либо кол-во переходов по сокращенной ссылке.''')
    parser.add_argument('link', help='Ваша ссылка')
    args = parser.parse_args()
    return args.link

def shorten_link(url, headers, params):
    response = requests.post(url, headers=headers, json=params)
    response.raise_for_status()
    bitlink = response.json()['id']
    return bitlink


def count_clicks(url, headers, params):
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    clicks_count = response.json()
    return clicks_count['total_clicks']


def is_link_short(url, headers, short_link_fragments): 
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{short_link_fragments}', headers=headers)
    return response.ok


def start():
    load_dotenv()
    bitly_token = os.getenv('BITLY_TOKEN')

    bitly_url = 'https://api-ssl.bitly.com/v4/shorten'
    #link = input('Введите ссылку\n')
    link_fragments = urlparse(get_link())
    short_link_fragments = f'{link_fragments.netloc}{link_fragments.path}'

    payload = {
        'long_url': get_link()
    }

    headers = {
        'Authorization': bitly_token,
    }

    click_url = f'https://api-ssl.bitly.com/v4/bitlinks/{short_link_fragments}/clicks/summary'

    params = {
        'unit': 'day'
    }


    if is_link_short(get_link(), headers, short_link_fragments):
        try:
            print('Количество переходов по ссылке:', count_clicks(click_url, headers, params))
        except requests.exceptions.HTTPError:
            print('*** ERROR * ERROR *ERROR ***\nВы ввели неверную сокращенную ссылку')
    else:
        try:
            print('Битлинк>>>', shorten_link(bitly_url, headers, payload))	
        except requests.exceptions.HTTPError:
            print('*** ERROR * ERROR * ERROR ***\nВы ввели неверную ссылку')


if __name__ == '__main__':
    start()