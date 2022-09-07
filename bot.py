import telebot
from telebot import types
import bybit

token = '5504182734:AAHlaMsKvJlt0MdQL3QoQn6jfrJnm1k3C28'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hi!')

@bot.message_handler(commands=['start'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton('cryptocurrency rates')
    markup.add(item1)
    bot.send_message(message.chat.id,'Click the button below :)',reply_markup=markup)

@bot.message_handler(content_types=['text'])
def add_coin_f(message):
    if message.text == "cryptocurrency rates":
        keyboard = types.InlineKeyboardMarkup()
        buttonBTC = types.InlineKeyboardButton(text = 'BTC', callback_data='btc')
        buttonETH = types.InlineKeyboardButton(text = 'ETH', callback_data='eth')
        keyboard.add(buttonBTC, buttonETH)
        bot.send_message(message.from_user.id, text = 'Сhoose a cryptocurrency to see the price', reply_markup=keyboard)
        

@bot.callback_query_handler(func=lambda callback: callback.data)
def call_back_btc(callback):
    if callback.data == 'btc':
        price_btc = bybit.btc_price()
        message_btc = 'btc price = ' + price_btc
    elif callback.data == 'eth':
        price_btc = bybit.eth_price()
        message_btc = 'eth price = ' + price_btc        
    else:
        pass
    bot.send_message(callback.message.chat.id, message_btc)
    
    

bot.infinity_polling()

