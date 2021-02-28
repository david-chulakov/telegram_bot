import telebot 
from telebot import types
import re
from bs4 import BeautifulSoup
import requests
import random
import os
import time

# токен бота
TOKEN = '1359352161:AAGfRbAcMSKTomuzNGStpWjoiBoD7e58cKY'

# Создаем бота
bot = telebot.TeleBot(TOKEN)

# Метод, который получает и обрабатывает сообщение
@bot.message_handler(commands=['start', 'help'])
def welcome_message(message):
    if message.text == "/start" or message.text == 'start':
        # отправка сообщения 
        bot.send_message(message.from_user.id, "Привет!")
        # Создаем кнопки
        keyboard = types.InlineKeyboardMarkup()
        # Создаем кнопки
        # Кнопка для новостей
        key_news = types.InlineKeyboardButton(text='Новости', callback_data='global_news')
        keyboard.add(key_news)
        # Кнопка для купонов кфс
        key_kfc = types.InlineKeyboardButton(text="Купоны KFC", callback_data='kfc')
        keyboard.add(key_kfc)

        bot.send_message(message.from_user.id, 'Выбери, что бы хотел посмотреть', reply_markup=keyboard)

    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши /start.")
    else: 
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /start.")


# Ответы на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    # Новости программирования 
    if call.data == 'programming':
        bot.send_message(call.message.chat.id, 'Рекоммендации для Давида')
        URL_PROGRAMMING = 'https://tproger.ru/tag/python/'
        page = requests.get(URL_PROGRAMMING)
        soup = BeautifulSoup(page.text, 'html.parser')
        for message in soup.find_all('a', class_="news-link hoverable")[0:3]:
            # bot.send_message(call.message.chat.id, message.get_text())
            bot.send_message(call.message.chat.id, message['href'])

    # Мем
    elif call.data == 'memes':
        URL_MEMES = 'https://vse-shutochki.ru/kartinki-prikolnye'
        page = requests.get(URL_MEMES)
        soup = BeautifulSoup(page.text, 'html.parser')
        memes = soup.find_all('div', class_="post")
        memes = soup.find_all('img')
        for mem in memes[1:10]:
            bot.send_photo(call.message.chat.id, mem['src'])
        
    # Новости бокса/мма
    elif call.data == 'mma':
        bot.send_message(call.message.chat.id, 'Рекоммендации для Лёши')
        URL_MMA = "https://allboxing.ru/mma-news.html"
        page = requests.get(URL_MMA)
        soup = BeautifulSoup(page.text, 'html.parser')
        news = soup.find_all('a', class_="news_element_title")
        for new in news[0:3]:
            bot.send_message(call.message.chat.id, f"https://allboxing.ru/{new['href']}")

    # Новости с хабра 
    elif call.data == 'habr':
        bot.send_message(call.message.chat.id, 'Рекоммендации для Дэна')
        URL_HABR = 'https://habr.com/ru/all/'
        page = requests.get(URL_HABR)
        soup = BeautifulSoup(page.text, 'html.parser')
        news = soup.find_all('a', class_="post__title_link")
        for new in news[0:3]:
            # bot.send_message(call.message.chat.id, new.get_text())
            bot.send_message(call.message.chat.id, new['href'])
    
    # Новости 
    elif call.data == 'news':
        URL_NEWS = 'https://ria.ru/world/'
        page = requests.get(URL_NEWS)
        soup = BeautifulSoup(page.text, 'html.parser')
        news = soup.find_all('a', class_="list-item__title color-font-hover-only")
        for new in news[0:3]:
            bot.send_message(call.message.chat.id, new['href'])

    # Новости музыки
    elif call.data == 'mus':
        bot.send_message(call.message.chat.id, 'Рекоммендации для Арины')
        URL_MUSIC = "https://www.gq.ru/entertainment/music"
        page = requests.get(URL_MUSIC)
        soup = BeautifulSoup(page.text, 'html.parser')
        music_news = soup.find_all('a')
        for html in music_news[17:22:2]:
            bot.send_message(call.message.chat.id, f"https://www.gq.ru{html['href']}")
        
    # Новости культуры
    elif call.data == 'culture':
        bot.send_message(call.message.chat.id, 'Рекоммендации для Димы')
        URL_CULTURE = "https://www.culture.ru/news"
        page = requests.get(URL_CULTURE)
        soup = BeautifulSoup(page.text, 'html.parser')
        culture_news = soup.find_all('a', class_="card-heading_title-link")
        for new in culture_news[0:4]:
            bot.send_message(call.message.chat.id, f"https://www.culture.ru{new['href']}")

        

    # Новостные категории
    elif call.data == 'global_news':
        keyboard_news = types.InlineKeyboardMarkup()
        # Кнопка Программирование
        key_Prog = types.InlineKeyboardButton(text='Программирование', callback_data='programming')
        keyboard_news.add(key_Prog)
        # Кнопка Мем
        key_Meme = types.InlineKeyboardButton(text='Мем', callback_data='memes')
        keyboard_news.add(key_Meme)
        # Кнопка Бокс/ММА
        key_MMA = types.InlineKeyboardButton(text='Бокс/ММА', callback_data='mma')
        keyboard_news.add(key_MMA)
        # Кнопка Музыка
        key_Music = types.InlineKeyboardButton(text='Музыка', callback_data='mus')
        keyboard_news.add(key_Music)
        # Кнопка Хабр
        key_Habr = types.InlineKeyboardButton(text='Хабр', callback_data='habr')
        keyboard_news.add(key_Habr)
        # Кнопка Культура
        key_Cult = types.InlineKeyboardButton(text='Культура', callback_data='culture')
        keyboard_news.add(key_Cult)
        # Кнопка Футбол
        key_football = types.InlineKeyboardButton(text='Футбол', callback_data='football')
        keyboard_news.add(key_football)
        # кнопка Баскетбол
        key_basketball = types.InlineKeyboardButton(text='Басктебол', callback_data='basketball')
        keyboard_news.add(key_basketball)
        # Политика
        key_politic = types.InlineKeyboardButton(text='Политика', callback_data='politic')
        keyboard_news.add(key_politic)
        # Просто новости в мире
        key_news = types.InlineKeyboardButton(text='Просто новости в мире', callback_data='news')
        keyboard_news.add(key_news)

        bot.send_message(call.message.chat.id, 'Выбери, категорию', reply_markup=keyboard_news)
    
    # Новости футбола
    elif call.data == 'football':
        URL_FOOTBALL = 'https://www.sports.ru/football/news'
        page = requests.get(URL_FOOTBALL)
        soup = BeautifulSoup(page.text, 'html.parser')
        footbal_news_htmls = soup.find_all('a', class_="short-text")
        for html in footbal_news_htmls[0:5]:
            bot.send_message(call.message.chat.id, f'https://www.sports.ru{html["href"]}')
        
    # Новости баскетбола
    elif call.data == 'basketball':
        URL_BASKETBALL = 'https://www.sports.ru/nba/news'
        page = requests.get(URL_BASKETBALL)
        soup = BeautifulSoup(page.text, 'html.parser')
        basketball_news_htmls = soup.find_all('a', class_="short-text")
        for html in basketball_news_htmls[0:5]:
            bot.send_message(call.message.chat.id, f'https://www.sports.ru{html["href"]}')

    # Новости политики
    elif call.data == 'politic':
        URL_POLITIC = 'https://ria.ru/politics'
        page = requests.get(URL_POLITIC)
        soup = BeautifulSoup(page.text, 'html.parser')
        politic_news_htmls = soup.find_all('a', class_="list-item__title color-font-hover-only")
        for html in politic_news_htmls[0:5]:
            bot.send_message(call.message.chat.id, html['href'])

    # Кнопка Купоны KFC
    elif call.data == 'kfc':
        i = random.randint(1,10)
        bot.send_message(call.message.chat.id, get_kfc(i))
        keyboard_kfc = types.InlineKeyboardMarkup()
        key_next = types.InlineKeyboardButton(text="Следующий", callback_data='next_kfc')
        keyboard_kfc.add(key_next)
        bot.send_message(call.message.chat.id, "Дальше?", reply_markup=keyboard_kfc)

    # Кнопка Купоны KFC 2
    elif call.data == 'next_kfc':
        i = random.randint(10,20)
        bot.send_message(call.message.chat.id, get_kfc(i))
        keyboard_kfc_next = types.InlineKeyboardMarkup()
        key_next = types.InlineKeyboardButton(text="Следующий", callback_data='kfc')
        keyboard_kfc_next.add(key_next)
        bot.send_message(call.message.chat.id, "Дальше?", reply_markup=keyboard_kfc_next)


def get_kfc(i):
    URL_KFC = "https://kfccpn.ru"
    page = requests.get(URL_KFC)
    soup = BeautifulSoup(page.text, 'html.parser')

    coupons = soup.find_all('div', class_="card-body")
    prices = soup.find_all('div', class_="d-block mb-3")
    descriptions = soup.find_all('div', class_="d-block mb-2")
    imgs = soup.findAll('img', class_="rounded-0 img-fluid ml-2 wp-post-image")

    coupons = [coupon.h3.text for coupon in coupons]
    descriptions = [description.text for description in descriptions]
    prices = [price.span.text for price in prices]
    imgs = [img.get('src') for img in imgs]
    return f"{imgs[i]}\n{coupons[i]}\n{prices[i]}\n{descriptions[i]}"
    
if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True, interval=0)
        except Exception as e:
            time.sleep(3)
            print(e)
