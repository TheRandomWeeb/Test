from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.usdebtclock.org/index.html').text

soup = BeautifulSoup(html_text, 'lxml')
price = soup.find('div', id='layer29')
print(price.span)