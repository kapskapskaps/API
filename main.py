import requests
import os

from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()
TOKEN = os.getenv('TOKEN')

def start():
	url_bitly = 'https://api-ssl.bitly.com/v4/shorten'
	Link = input('Введите ссылку\n')
	fragments_link = urlparse(Link)
	fragments_link = fragments_link.netloc + fragments_link.path + fragments_link.params + fragments_link.query + fragments_link.fragment

	url_load = {
		'long_url': Link
	}

	headers = {
		'Authorization':TOKEN,
	}

	url_click = f'https://api-ssl.bitly.com/v4/bitlinks/{fragments_link}/clicks/summary'

	params = {
		'unit':'day'
	}


	def shorten_link(token, link):
		response = requests.post(url_bitly, headers=token, json=link)
		response.raise_for_status()
		bitlink = response.json()['id']
		return bitlink


	def count_clicks(token, link):
		response = requests.get(url_click, headers=token, params=link)
		response.raise_for_status()
		clicks_count = response.json()
		return clicks_count['total_clicks']


	if fragments_link.startswith('bit.ly'):
		try:
			print('Количество переходов по ссылке:', count_clicks(headers,params))
		except requests.exceptions.HTTPError:
			print('*** ERROR * ERROR *ERROR ***\nВы ввели неверную сокращенную ссылку')
	elif fragments_link.startswith('bit.ly')==False:
		try:
			print('Битлинк', shorten_link(headers, url_load))	
		except requests.exceptions.HTTPError:
			print('*** ERROR * ERROR * ERROR ***\nВы ввели неверную ссылку')


if __name__ == '__main__':
	start()



