'''
    author: Zitian(Daniel) Tong
    date: 19:51 2019-05-04 2019
    editor: PyCharm    
    email: danieltongubc@gmail.com 
'''

import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.johnlewis.com/canon-eos-rp-compact-system-camera-4k-ultra-hd-26-2mp-wi-fi-bluetooth-oled-evf-3-inch-vari-angle-touch-screen-with-ef-mount-adapter-body-only/p4019543'
tag_name = 'p'
query = {'class': 'price price--large'}

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content,'html.parser')
element = soup.find(tag_name, query)
string_price = element.text.strip()

pattern = re.compile(r'(\d+,?\d*\.\d\d)')
match = pattern.search(string_price)
found_price = match.group(1)
without_commas = found_price.replace(',','')
print(float(without_commas))



url = 'https://www.amazon.com/Samsung-MicroSD-Adapter-MB-ME128GA-AM/dp/B06XWZWYVP/ref=lp_16225007011_1_2?s=computers-intl-ship&ie=UTF8&qid=1559057470&sr=1-2'
tag_name = 'span'
query = {'class': 'a-span12'}

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content,'html.parser')
print(soup)
element = soup.find(tag_name, query)
print(element)
string_price = element.text.strip()

pattern = re.compile(r'(\d+,?\d*\.\d\d)')
match = pattern.search(string_price)
found_price = match.group(1)
without_commas = found_price.replace(',','')
print(float(without_commas))