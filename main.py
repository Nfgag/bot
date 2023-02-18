import telebot
from telebot import TeleBot

bot = telebot.TeleBot('6184270382:AAF2euCz_zLj9UL7n64ROGM7dfgXiDcE_Kw')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def ger_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, "И тебе привет!", parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"ТВой ID:{message.from_user.id}", parse_mode='html')
    elif message.text == 'photo':
        photo = open('icon.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode='html')


bot.polling(none_stop=True)