import urllib.request  as http
import json
import datetime
from time import strftime


API_URL = "https://api.binance.com"
PING = '/api/v3/ping'
TIME = '/api/v3/time'
TRADE = '/api/v3/trades'
BRIDGE = 'USDT'


def test_binance_api():
    resp = http.urlopen(API_URL+PING).read()
    print(resp)


def get_time_from_binance():
    print("Getting the time...")
    resp = http.urlopen((API_URL+TIME)).read().decode("ascii")
    respDict = json.loads(resp)
    print(respDict["serverTime"])


def get_trades(symbol='BTC', bridge=BRIDGE):
    resp = http.urlopen(f"{API_URL}{TRADE}?symbol={symbol}{bridge}").read().decode("ascii")
    respList = json.loads(resp)
    for trade in respList:
        print(strftime(str(trade['time'])))
        print(trade['qty'])
        print(trade['price'])

    return respList


test_binance_api()
get_time_from_binance()
get_trades()

transactions = get_trades()
tfirst = transactions[0]['time']
tlast = transactions[-1]['time']
dt = (tlast - tfirst) / 1000
print('Transaction per seconde: ', )

