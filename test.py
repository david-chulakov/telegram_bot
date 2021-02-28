from bs4 import BeautifulSoup
import requests
import re
import os
import random
from PIL import Image

URL_PROGRAMMING = 'https://tproger.ru/tag/python/'
URL_MEMES = 'https://vse-shutochki.ru/kartinki-prikolnye'


def get_prog_news():
    page = requests.get(URL_PROGRAMMING)
    soup = BeautifulSoup(page.text, 'html.parser')
    message = soup.find_all('div', class_="news-row")[0].get_text() + '\n' + soup.find_all('div', class_="news-row")[1].get_text() + '\n' + soup.find_all('div', class_="news-row")[3].get_text()
    
    return message

def get_memes():
    page = requests.get(URL_MEMES)
    soup = BeautifulSoup(page.text, 'html.parser')
    clean_jpg_urls = []
    memes = soup.find_all('div', class_="post")
    memes = soup.find_all('img')
    return memes[1]['src']
    


URL_FOOD = 'https://www.russianfood.com/reading/clauses/'
def get_food():
    page = requests.get(URL_FOOD)
    soup = BeautifulSoup(page.text, 'html.parser')
    recipes = soup.find_all('a', class_="title")
    return recipes[0].get_text()


def get_habr():
    URL_HABR = 'https://habr.com/ru/all/'
    page = requests.get(URL_HABR)
    soup = BeautifulSoup(page.text, 'html.parser')
    news = soup.find_all('a', class_="post__title_link")
    for new in news[0:3]:
        print(new.get_text())
        print(new['href'])


def get_news():
    URL_NEWS = 'https://ria.ru/world/'
    page = requests.get(URL_NEWS)
    soup = BeautifulSoup(page.text, 'html.parser')
    news = soup.find_all('a', class_="list-item__title color-font-hover-only")
    for new in news[0:3]:
        return new['href']

def get_cat():
    all_files_in_directory = os.listdir('images/cats')
    file = random.choice(all_files_in_directory)
    doc = open('/images/cats' + '/' + file, 'rb')
    return all_files_in_directory

def convert_to_pdf():
    image1 = Image.open(r'images/cats/1.jpg')
    im1 = image1.convert('RGB')
    im1.save(r'pdf/1.pdf')


def get_music():
    URL_MUSIC = "https://www.gq.ru/entertainment/music"
    page = requests.get(URL_MUSIC)
    soup = BeautifulSoup(page.text, 'html.parser')
    music_news = soup.find_all('a')
    urls = []
    for html in music_news[17:22:2]:
        print(f"https://www.gq.ru{html['href']}")
        

def get_mma():
    URL_MMA = "https://allboxing.ru/mma-news.html"
    page = requests.get(URL_MMA)
    soup = BeautifulSoup(page.text, 'html.parser')
    news = soup.find_all('a', class_="news_element_title")
    for new in news[0:3]:
        return new['href']
    
def get_cult():
    URL_CULTURE = "https://www.culture.ru/news"
    page = requests.get(URL_CULTURE)
    soup = BeautifulSoup(page.text, 'html.parser')
    culture_news = soup.find_all()
    for new in culture_news[0:4]:
        print(f"https://www.culture.ru{new['href']}")

def get_kfc():
    URL_KFC = "https://kfccpn.ru"
    page = requests.get(URL_KFC)
    soup = BeautifulSoup(page.text, 'lxml')

    coupons = soup.find_all('div', class_="card-body")
    prices = soup.find_all('div', class_="d-block mb-3")
    descriptions = soup.find_all('div', class_="d-block mb-2")
    imgs = soup.findAll('img', class_="rounded-0 img-fluid ml-2 wp-post-image")

    coupons = [coupon.h3.text for coupon in coupons]
    descriptions = [description.text for description in descriptions]
    prices = [price.span.text for price in prices]
    imgs = [img.get('src') for img in imgs]
    
    return imgs[0]

print(get_kfc())