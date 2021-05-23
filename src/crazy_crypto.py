"""Script for monitoring highly volatile crypto.

The script loads the data from coinlore api. 
As of v0.1.0 we're looking only into eth, doge, and btc.
The script prints the current value and 24h percent change
for these crytpo.
Takes limit order arguments and prints action needed if 
the current value drops below the limit order.

Current version:v0.1.0
"""
import sys
import argparse
import requests
import json
from datetime import datetime


def load_data(data, crypt):
    """Load data into dicts"""
    data['price'] = float(crypt['price_usd'])
    data['pc_24h'] = float(crypt['percent_change_24h'])


def get_data():
    """Get data from API and store in dicts"""
    try:
    	r = requests.get("https://api.coinlore.net/api/tickers/")
    except Exception as e:
    	sys.exit(e)

    response = json.loads(r.text)
    utc_time = datetime.utcfromtimestamp(response['info']['time']).strftime('%Y-%m-%d %H:%M:%S')

    # placeholder for the data
    eth_data = {}
    dog_data = {}
    btc_data = {}

    for crypt in response['data']:
        if crypt['symbol'] in {'ETH', 'DOGE', 'BTC'}:
            if crypt['symbol'] == 'ETH':
                load_data(eth_data, crypt)
            elif crypt['symbol'] == 'DOGE':
                load_data(dog_data, crypt)
            elif crypt['symbol'] == 'BTC':
                load_data(btc_data, crypt)

    return eth_data, dog_data, btc_data, utc_time


def crypto_deets(deets, amt_args):
    """Get crypto details"""
    eth_data, dog_data, btc_data, time = deets[0], deets[1], deets[2], deets[3]
    eth_p, pc_eth = eth_data['price'], eth_data['pc_24h']
    dog_p, pc_dog = dog_data['price'], dog_data['pc_24h']
    btc_p, pc_btc = btc_data['price'], btc_data['pc_24h']

    # helpers for neat printing
    pp = ' ' * 5
    arrow = lambda pc: u'\u2191' if str(pc)[0] != '-' else u'\u2193'

    print(f'!!! ALERT !!!')
    print(f"Date: {time.split(' ')[0]}")
    print(f"Time: {time.split(' ')[1].strip()} UTC")
    print('------------INFO-------------')
    print("{:.13s} | {:.10s} {}".format('eth: ' + str(eth_p) + pp, '%: ' + str(pc_eth) + pp, arrow(pc_eth)))
    print("{:.13s} | {:.10s} {}".format('dog: ' + str(dog_p) + pp, '%: ' + str(pc_dog) + pp, arrow(pc_dog)))
    print("{:.13s} | {:.10s} {}".format('btc: ' + str(btc_p) + pp, '%: ' + str(pc_btc) + pp, arrow(pc_btc)))
    print('--------Action needed--------')
    c = 0
    if eth_p <= amt_args.eth_amt:
        print(f'ETH  - BTFD | Limit passed: {amt_args.eth_amt}')
        c += 1
    if dog_p <= amt_args.dog_amt:
        print(f'DOGE - BTFD | Limit passed: {amt_args.dog_amt}')
        c += 1
    if btc_p <= amt_args.btc_amt:
        print(f'BTC  - BTFD | Limit passed: {amt_args.btc_amt}')
        c += 1
    if c == 0:
        print('NONE')


def get_args():
    """Parse amount limit arguments"""
    parser = argparse.ArgumentParser(description='Help decide trade')
    parser.add_argument('-e', '--eth_amt', default=2000.0, type=float, metavar='', help='ETH-limit')
    parser.add_argument('-d', '--dog_amt', default=0.10, type=float, metavar='', help='DOGE-limit')
    parser.add_argument('-b', '--btc_amt', default=50000.0, type=float, metavar='', help='BTC-limit')
    args = parser.parse_args()
    return args


def main():
    """Crazy crypto entry point"""
    amt_args = get_args()
    deets = get_data()
    crypto_deets(deets, amt_args)


if __name__ == '__main__':
    main()
