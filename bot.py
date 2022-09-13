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

def Button(token, call):
    keyboard_button = types.InlineKeyboardButton(text = token, callback_data= call)
    return keyboard_button


@bot.message_handler(content_types=['text'])
def add_coin_f(message):
    if message.text == "Realtime rates":
        keyboard = types.InlineKeyboardMarkup()

        buttonBTC = Button('BTC', 'BTC')
        buttonETH = Button('ETH', 'ETH')
        buttonSol = Button('Solana', 'SOL')
        buttonLTC = Button('LiteCoin', 'LTC')
        buttonBIT = Button('BitDAO', 'BIT')
        buttonXRP = Button('Ripple', 'XRP')

        keyboard.add(buttonBTC, buttonETH, buttonSol, buttonLTC, buttonBIT, buttonXRP)
        bot.send_message(message.from_user.id, text = 'Сhoose a cryptocurrency to see the price', reply_markup= keyboard)
        

@bot.callback_query_handler(func=lambda callback: callback.data)
def call_back_btc(callback):
    token = callback.data
    price = bybit.Price(token)
    end_price = price.check_price()
    message_price = f'{token} price = {end_price}'
    bot.send_message(callback.message.chat.id, message_price)



    # if callback.data == 'btc':
    #     price_crypto = bybit.btc_price()
    #     message_price = 'BitCoin price = ' + price_crypto
    # elif callback.data == 'eth':
    #     price_crypto = bybit.eth_price()
    #     message_price = 'Ethereum price = ' + price_crypto  
    # elif callback.data == 'sol':
    #     price_crypto = bybit.sol_price()
    #     message_price = 'Solana price = ' + price_crypto    
    # elif callback.data == 'ltc':
    #     price_crypto = bybit.ltc_price()
    #     message_price = 'LiteCoin price = ' + price_crypto   
    # elif callback.data == 'xrp':
    #     price_crypto = bybit.xrp_price()
    #     message_price = 'Ripple price = ' + price_crypto
    # elif callback.data == 'bit':
    #     price_crypto = bybit.bit_price()
    #     message_price = 'BitDAO price = ' + price_crypto                
    # bot.send_message(callback.message.chat.id, message_price)
    
    

bot.infinity_polling()

