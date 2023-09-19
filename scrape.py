import requests
from bs4 import BeautifulSoup

#get information from page
res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline > a')
votes = soup.select('.score')

#create function that receives links and votes
def create_custom_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):
        #grab title of each link
        title = links[idx].getText()
        href = links[idx].get('href', None)
        #just show the points without the text after
        points = int(votes[idx].getText().replace(' points', ''))
        print(points)
        hn.append({'title': title, 'link': href})
    return hn

create_custom_hn(links, votes)
