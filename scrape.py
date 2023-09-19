import requests
from bs4 import BeautifulSoup
import pprint

#get information from page
res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline > a')
subtext = soup.select('.subtext')

#sort list by votes in descending order
def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

#create function that receives links and votes
def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        #grab title of each link
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            #just show the points without the text after
            points = int(vote[0].getText().replace(' points', ''))
            #only get output with points at last 100
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

#make the output neater to read
pprint.pprint(create_custom_hn(links, subtext))
