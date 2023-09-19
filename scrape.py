import requests
from bs4 import BeautifulSoup

#get information from page
res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
votes = soup.select('.score')
print(votes[0].get('id'))
