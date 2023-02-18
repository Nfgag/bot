import telebot
from telebot import types

bot = telebot.TeleBot('6184270382:AAF2euCz_zLj9UL7n64ROGM7dfgXiDcE_Kw')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['photo'])
def ger_user_photo(message):
    bot.send_message(message.chat.id, 'Вау, крутое фото')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить вебсайт", url="https://itproger.com"))
    bot.send_message(message.chat.id, "Перейдите на сайт", reply_markup=markup)


@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('Веб-сайт')
    start = types.KeyboardButton('start')

    markup.add(website, start)
    bot.send_message(message.chat.id, "Перейдите на сайт", reply_markup=markup)


bot.polling(none_stop=True)
