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
    item1=types.KeyboardButton('Realtime rates')
    markup.add(item1)
    bot.send_message(message.chat.id,'Click the button below :)',reply_markup=markup)

def add_button(token: str, callback: str) -> types.InlineKeyboardButton:
    keyboard_button = types.InlineKeyboardButton(text = token, callback_data= callback)
    return keyboard_button


@bot.message_handler(content_types=['text'])
def add_coin_f(message):
    if message.text == "Realtime rates":
        keyboard = types.InlineKeyboardMarkup()

        buttonBTC = add_button('BTC', 'BTC')
        buttonETH = add_button('ETH', 'ETH')
        buttonSol = add_button('Solana', 'SOL')
        buttonLTC = add_button('LiteCoin', 'LTC')
        buttonBIT = add_button('BitDAO', 'BIT')
        buttonXRP = add_button('Ripple', 'XRP')

        keyboard.add(buttonBTC, buttonETH, buttonSol, buttonLTC, buttonBIT, buttonXRP)
        bot.send_message(message.from_user.id, text = 'Сhoose a cryptocurrency to see the price', reply_markup= keyboard)
        

@bot.callback_query_handler(func=lambda callback: callback.data)
def call_back_btc(callback):
    token = callback.data
    price = bybit.Price(token)
    end_price = price.check_price()
    message_price = f'{token} price = {end_price}'
    bot.send_message(callback.message.chat.id, message_price)


bot.infinity_polling()

