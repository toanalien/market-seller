import ccxt
import pprint
from dotenv import load_dotenv
import os

load_dotenv()
pp = pprint.PrettyPrinter(indent=4)

APIKEY = os.environ.get('APIKEY')
APISECRET = os.environ.get('APISECRET')

binance = ccxt.binance({
    'apiKey': APIKEY,
    'secret': APISECRET,
})

balance = binance.fetch_balance()['free']


def to_btc(balance):
    for key in balance.keys():
        if balance[key] > 0 and key != 'BTC':
            try:
                result = binance.createMarketSellOrder(
                    key + '/BTC', balance[key])
                print(key, balance[key])
            except:
                pass
            print("****")


def to_usdt(balance):
    for key in balance.keys():
        if balance[key] > 0 and key != 'USDT':
            try:
                result = binance.createMarketSellOrder(
                    key + '/USDT', balance[key])
                print(key, balance[key])
            except:
                pass
            print("****")
