import telebot
from telebot import types
import bybit

token = ''

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

@bot.message_handler(content_types=['text'])
def add_coin_f(message):
    if message.text == "Realtime rates":
        keyboard = types.InlineKeyboardMarkup()
        buttonBTC = types.InlineKeyboardButton(text = 'BTC', callback_data='btc')
        buttonETH = types.InlineKeyboardButton(text = 'ETH', callback_data='eth')
        buttonSOL = types.InlineKeyboardButton(text = 'Solana', callback_data='sol')
        buttonLTC = types.InlineKeyboardButton(text = 'LiteCoin', callback_data='ltc')
        buttonBIT = types.InlineKeyboardButton(text = 'BitDAO', callback_data='bit')
        buttonXRP = types.InlineKeyboardButton(text = 'Ripple', callback_data='xrp')
        keyboard.add(buttonBTC, buttonETH, buttonSOL, buttonLTC, buttonBIT, buttonXRP)
        bot.send_message(message.from_user.id, text = 'Сhoose a cryptocurrency to see the price', reply_markup=keyboard)
        

@bot.callback_query_handler(func=lambda callback: callback.data)
def call_back_btc(callback):
    if callback.data == 'btc':
        price_crypto = bybit.btc_price()
        message_price = 'BitCoin price = ' + price_crypto
    elif callback.data == 'eth':
        price_crypto = bybit.eth_price()
        message_price = 'Ethereum price = ' + price_crypto  
    elif callback.data == 'sol':
        price_crypto = bybit.sol_price()
        message_price = 'Solana price = ' + price_crypto    
    elif callback.data == 'ltc':
        price_crypto = bybit.ltc_price()
        message_price = 'LiteCoin price = ' + price_crypto   
    elif callback.data == 'xrp':
        price_crypto = bybit.xrp_price()
        message_price = 'Ripple price = ' + price_crypto
    elif callback.data == 'bit':
        price_crypto = bybit.bit_price()
        message_price = 'BitDAO price = ' + price_crypto                
    else:
        pass
    bot.send_message(callback.message.chat.id, message_price)
    
    

bot.infinity_polling()

