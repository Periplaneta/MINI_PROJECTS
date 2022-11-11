import requests 
from bs4 import BeautifulSoup


response = requests.get('https://thehackernews.com/').text
soup = BeautifulSoup(response, features= ('html.parser'))
headlines = []
summary = []

headers = soup.find_all('div', attrs={'class':'clear home-right'})
for header in headers:
    headlines.append(header.h2.text)
summaries = soup.find_all('div', attrs={'class':'home-desc'})
for summari in summaries:
    summary.append(summari.text)

csv = {
    'headlines': headlines,
    'summary': summary
}

import pandas as pd
data = pd.DataFrame(csv)
print(data)
















