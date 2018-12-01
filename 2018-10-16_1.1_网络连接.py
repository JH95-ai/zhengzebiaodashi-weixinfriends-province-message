# -*-coding:utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen('https://pythonscraping.com/pages/page1.html')
print(html.read())