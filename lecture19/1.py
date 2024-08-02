from bs4 import BeautifulSoup
import requests

url = 'https://news.ycombinator.com/'
content = requests.get(url).content
soup = BeautifulSoup(content, 'html.parser')

headlines = soup.find_all('span', class_='titleline')

for headline in headlines:
    print(headline.text)