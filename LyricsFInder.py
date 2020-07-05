from bs4 import BeautifulSoup
import requests

keyWord = input("Enter The Song And Artist Name:") + ' lyrics'

url = f'https://www.google.com/search?hl=en&q={keyWord}'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0'}

src = requests.get(url, headers=headers).text
soup = BeautifulSoup(src, 'lxml')

links = []

for div in soup.findAll('div', class_='rc'):
    contentBox = div.find('div', class_='r')
    try:
        links.append(contentBox.a['href'])
    except AttributeError:
        pass

for link in links:
    if 'https://www.azlyrics.com/lyrics' in link:
        try:
            src2 = requests.get(link).text
            soup2 = BeautifulSoup(src2, 'lxml')

            divs = soup2.findAll('div', class_=None)

            for div in divs:
                print(div.text.strip())

            print(f'Lyrics Url : {link}')

        except NameError:
            print("Song Not Found")