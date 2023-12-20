import requests
import pandas as pd
from flipside import Flipside

def fetch_ethereum_data():
  flipside = Flipside("87e697cf-e55f-4a7f-b549-3595e41736a5",
                      "https://api-v2.flipsidecrypto.xyz")
  sql = """SELECT hour :: date, avg(price) FROM ethereum.price.ez_hourly_token_prices WHERE lower(token_address) = lower('0xe28b3B32B6c345A34Ff64674606124Dd5Aceca30') and hour :: date >= '2020-01-01' group by 1 order by 1;"""
  query_result_set = flipside.query(sql)
  df = pd.DataFrame(query_result_set.rows)
  df[0] = pd.to_datetime(df[0])
  data_as_list_of_lists = df[[0, 1]].to_numpy().tolist()
  return pd.DataFrame(data_as_list_of_lists, columns=["Date", "Price"]).set_index("Date")

def get_historical_prices(symbol, timeframe, limit=2000):
    base_url = 'https://min-api.cryptocompare.com/data'
    endpoint = '/v2/histoday'  # You can change this to other timeframes if needed

    params = {
        'fsym': symbol.split('/')[0],  # From symbol
        'tsym': symbol.split('/')[1],  # To symbol
        'limit': limit,
        'aggregate': 1,
        'e': 'CCCAGG'  # Exchange parameter (CCCAGG is a composite index)
    }

    response = requests.get(base_url + endpoint, params=params)
    data = response.json()['Data']['Data']

    return data


def get_max_price(symbol, timeframe, limit=2000):
    data = get_historical_prices(symbol, timeframe, limit)
    max_price = max(entry['high'] for entry in data)
    return max_price

def tokel_position():
    API_KEY = 'd40ab02a-61db-4917-9901-422599d74475'
    headers = {
        'X-CMC_PRO_API_KEY': API_KEY
    }
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    r = requests.get(url, headers=headers)

    token_info = []

    if r.status_code == 200:
        data = r.json()
        for d in data['data']:
            symbol = d['symbol']
            token_info.append({
                'symbol': symbol,
                'price': d['quote']['USD']['price'],
                'rank': d['cmc_rank'],
                'market_cap': d['quote']['USD']['market_cap'],
                'volume_24h': d['quote']['USD']['volume_24h'],
                'circulating_supply': d['circulating_supply'],
                'percent_change_1h': d['quote']['USD']['percent_change_1h'],
                'percent_change_24h': d['quote']['USD']['percent_change_24h'],
                'percent_change_7d': d['quote']['USD']['percent_change_7d'],
                'volume_change_24h': d['quote']['USD']['volume_change_24h']   
            })
    inj_info = [[info['price'],info['rank'], info['market_cap'], info['volume_24h'], info['circulating_supply'], info['percent_change_1h'], info['percent_change_24h'], info['percent_change_7d'], info['volume_change_24h']]
                for info in token_info if info['symbol'] == 'INJ']
    return inj_info[0]

def format_large_number(number):
    powers = ["", "K", "M", "B", "T"]  # You can extend this list based on your needs

    # Determine the appropriate power of 10
    exponent = 0
    while number >= 1000:
        number /= 1000.0
        exponent += 1

    # Format the number with the appropriate power of 10
    formatted_number = f"{number:.2f}{powers[exponent]}"

    return formatted_number