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
        # Кнопка для Давида
        key_David = types.InlineKeyboardButton(text='Давид', callback_data='programming')
        keyboard.add(key_David)
        # Кнопка для Сани
        key_Canya = types.InlineKeyboardButton(text='Саня', callback_data='memes')
        keyboard.add(key_Canya)
        # Кнопка для Макса
        key_Maks = types.InlineKeyboardButton(text='Макс', callback_data='news')
        keyboard.add(key_Maks)
        # Кнопка для Лёхи
        key_Alexei = types.InlineKeyboardButton(text='Лёха', callback_data='mma')
        keyboard.add(key_Alexei)
        # Кнопка для Арины
        key_Arina = types.InlineKeyboardButton(text='Арина', callback_data='mus')
        keyboard.add(key_Arina)
        # Кнопка для Дэна
        key_Den = types.InlineKeyboardButton(text='Дэн', callback_data='habr')
        keyboard.add(key_Den)
        # Кнопка для Димы
        key_Dima = types.InlineKeyboardButton(text='Дима', callback_data='culture')
        keyboard.add(key_Dima)
        # Создаем кнопки
        # Кнопка для новостей
        key_news = types.InlineKeyboardButton(text='Новости', callback_data='global_news')
        keyboard.add(key_news)
        bot.send_message(message.from_user.id, 'Выбери, что бы хотел посмотреть', reply_markup=keyboard)

    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши /start.")
    else: 
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /start.")



@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    # Новости программирования для Давида
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
        
    # Новости для Лёхи
    elif call.data == 'mma':
        bot.send_message(call.message.chat.id, 'Рекоммендации для Лёши')
        URL_MMA = "https://allboxing.ru/mma-news.html"
        page = requests.get(URL_MMA)
        soup = BeautifulSoup(page.text, 'html.parser')
        news = soup.find_all('a', class_="news_element_title")
        for new in news[0:3]:
            bot.send_message(call.message.chat.id, f"https://allboxing.ru/{new['href']}")

    # Новости с хабра для Дэна
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

    # Кнопка для Арины
    elif call.data == 'mus':
        bot.send_message(call.message.chat.id, 'Рекоммендации для Арины')
        URL_MUSIC = "https://www.gq.ru/entertainment/music"
        page = requests.get(URL_MUSIC)
        soup = BeautifulSoup(page.text, 'html.parser')
        music_news = soup.find_all('a')
        for html in music_news[17:22:2]:
            bot.send_message(call.message.chat.id, f"https://www.gq.ru{html['href']}")
        

    elif call.data == 'culture':
        bot.send_message(call.message.chat.id, 'Рекоммендации для Димы')
        URL_CULTURE = "https://www.culture.ru/news"
        page = requests.get(URL_CULTURE)
        soup = BeautifulSoup(page.text, 'html.parser')
        culture_news = soup.find_all('a', class_="card-heading_title-link")
        for new in culture_news[0:4]:
            bot.send_message(call.message.chat.id, f"https://www.culture.ru{new['href']}")

        

    # Новостные категории для любого пользователя
    elif call.data == 'global_news':
        keyboard_news = types.InlineKeyboardMarkup()
        # Кнопка для новостей футбола
        key_football = types.InlineKeyboardButton(text='Футбол', callback_data='football')
        keyboard_news.add(key_football)
        # кнопка для новостей баскетбола
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

    
    
if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True, interval=0)
        except Exception as e:
            time.sleep(3)
            print(e)
