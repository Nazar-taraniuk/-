import requests
from bs4 import BeautifulSoup as bs

def req():
    url = "https://kworb.net/apple_songs/index.html"

    response = requests.get(url)
    html = response.content

    if response.status_code == 200:
        soup = bs(html,"html.parser")

    result = soup.find_all(class_= "mp text")
    text =  '\n'.join(paragraph.text for paragraph in result)
    with open("chart", 'w', encoding='utf-8') as file:
        file.write(text)
