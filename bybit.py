from pybit import inverse_perpetual


class Price():

  def __init__(self, token):
   self.token = token
  
  def check_price(self):
    session_unauth = inverse_perpetual.HTTP(
      endpoint="https://api-testnet.bybit.com"
    )
    info = session_unauth.latest_information_for_symbol(
      symbol=f"{self.token}USD")

    new_info = info["result"]   

    dict = new_info[0]
    price = dict['last_price']
    return price

r = Price('BTC')
print(r.check_price())