import requests
from bs4 import BeautifulSoup

#get information from page
res = requests.get('https://news.ycombinator.com/news')
print(res.text)
