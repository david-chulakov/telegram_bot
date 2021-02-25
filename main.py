import telebot 

TOKEN = '1359352161:AAGfRbAcMSKTomuzNGStpWjoiBoD7e58cKY'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def welcome_message(message):
    bot.send_message(message.from_user.id, "Привет!")

bot.polling(none_stop=True, interval=0)