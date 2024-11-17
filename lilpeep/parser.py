import requests
from bs4 import BeautifulSoup as bs

def req_apple(url):
    response = requests.get(url)
    html = response.content

    if response.status_code == 200:
        soup = bs(html,"html.parser")

    result_apple = soup.find_all(class_= "mp text")
    text =  '\n'.join(paragraph.text for paragraph in result_apple)
    with open("chart", 'w', encoding='utf-8') as file:
        file.write(text)

def req_itunes(url):
    response = requests.get(url)
    html = response.content

    if response.status_code == 200:
        soup = bs(html, "html.parser")

    result_itunes = soup.find_all(class_="mp text")
    text = "\n".join(paragraph.text for paragraph in result_itunes)
    with open("chart_itunes", "w", encoding="utf-8") as file:
        file.write(text)