import telebot
from telebot import types

token = '5504182734:AAHlaMsKvJlt0MdQL3QoQn6jfrJnm1k3C28'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hi!')

@bot.message_handler(commands=['start'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton('Добавить')
    markup.add(item1)
    bot.send_message(message.chat.id,'Выберите что вам надо:',reply_markup=markup)

@bot.message_handler(content_types=['text'])
def add_coin_f(message):
    if message.text == "Добавить":
        keyboard = types.InlineKeyboardMarkup()
        buttonBTC = types.InlineKeyboardButton(text = 'BTC', callback_data='btc')
        buttonETH = types.InlineKeyboardButton(text = 'ETH', callback_data='eth')
        keyboard.add(buttonBTC, buttonETH)
        bot.send_message(message.from_user.id, text = 'Choose:', reply_markup=keyboard)


bot.infinity_polling()

