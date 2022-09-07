from pybit import inverse_perpetual


def btc_price():
    session_unauth = inverse_perpetual.HTTP(
      endpoint="https://api-testnet.bybit.com"
    )
    info = session_unauth.latest_information_for_symbol(
      symbol="BTCUSD")

    new_info = info["result"]   

    dict = new_info[0]
    price = dict['last_price']
    return price

def eth_price():
    session_unauth = inverse_perpetual.HTTP(
      endpoint="https://api-testnet.bybit.com"
    )
    info = session_unauth.latest_information_for_symbol(
      symbol="ETHUSD")

    new_info = info["result"]   

    dict = new_info[0]
    price = dict['last_price']
    return price

print(eth_price())