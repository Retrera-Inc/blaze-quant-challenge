import warnings
warnings.filterwarnings('ignore')
import requests
import streamlit as st
import mplfinance as mpf
import pandas as pd
import datetime
import numpy as np
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt

def change_font_color(element, text, font_color):
    st.markdown(f'<{element} style="color: {font_color};">{text}</{element}>', unsafe_allow_html=True)

def fetch_crypto_price(symbol):
    api_url = f'https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        return data.get(symbol, {}).get('usd')
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

def fetch_market_data(symbol, days=30):
    api_url = f'https://api.coingecko.com/api/v3/coins/{symbol}/market_chart'
    params = {
        'vs_currency': 'usd',
        'days': days,
        'interval': 'daily',
    }

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        st.error(f"Failed to fetch data. Status code: {response.status_code}")
        return None

def plot_historical_prices(data):
    prices = data['prices']
    prices = np.array(prices)
    timestamps = [datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d') for timestamp in prices[:, 0]]

    df_prices = pd.DataFrame({'Date': timestamps, 'Price (USD)': prices[:, 1]})
    df_prices['Date'] = pd.to_datetime(df_prices['Date'])

    st.subheader('Historical Prices')
    st.line_chart(df_prices.set_index('Date'))

def plot_market_cap(data):
    market_caps = data['market_caps']
    market_caps = np.array(market_caps)
    timestamps = [datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d') for timestamp in market_caps[:, 0]]

    df_market_caps = pd.DataFrame({'Date': timestamps, 'Market Cap (USD)': market_caps[:, 1]})
    df_market_caps['Date'] = pd.to_datetime(df_market_caps['Date'])

    st.subheader('Market Cap Trend')
    st.line_chart(df_market_caps.set_index('Date'))

def plot_candlestick_chart(df):

    df['Vol.'] = df['Vol.'].str.replace('K', 'e3').str.replace('M', 'e6').map(pd.eval).astype('int64')
    df['Change %'] = df['Change %'].str.rstrip('%').astype('float') / 100.0

    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    df.rename(columns={'Price': 'Close'}, inplace=True)
    mpf.plot(df,
             type='candle',
             style='yahoo',
             title='Candlestick Chart',
             ylabel='Price',
             mav=(10, 20),
             figratio=(10, 6))

    st.pyplot()

def analyze_price_trend(data):
    prices = data.get('prices', [])
    if not prices:
        return "No sufficient data for analysis."
    closing_prices = [price[1] for price in prices]
    price_change_percentage = ((closing_prices[-1] - closing_prices[0]) / closing_prices[0]) * 100
    if price_change_percentage > 0:
        return "bullish"
    elif price_change_percentage < 0:
        return "bearish"
    else:
        return "neutral"


def analyze_market_cap(data):
    market_cap_data = data.get('market_caps', [])
    if not market_cap_data:
        return "No sufficient data for analysis."
    market_caps = [cap[1] for cap in market_cap_data]
    market_cap_change_percentage = ((market_caps[-1] - market_caps[0]) / market_caps[0]) * 100

    if market_cap_change_percentage > 0:
        return "growth"
    elif market_cap_change_percentage < 0:
        return "decline"
    else:
        return "stability"

def calculate_moving_average(path, window_size):
    data=pd.read_csv(path)
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    data.sort_index(inplace=True)
    data['SMA'] = data['Price'].rolling(window=window_size).mean()

    st.line_chart(data[['Price', 'SMA']])

    last_price = data['Price'].iloc[-1]
    last_ma = data['SMA'].iloc[-1]

    if last_price > last_ma:
        st.write("The current price is above the Moving Average, suggesting a potential uptrend.")
    elif last_price < last_ma:
        st.write("The current price is below the Moving Average, indicating a potential downtrend.")
    else:
        st.write("The current price is at the Moving Average, and the trend is relatively neutral.")

def display_market_info(market_cap, trading_vol, fully_diluted_valuation, circulating_supply, total_supply, max_supply):
    st.title("Token Market Information")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Market Cap")
        st.write(f"${market_cap:,}")

        st.subheader("24 Hour Trading Volume")
        st.write(f"${trading_vol:,}")

        st.subheader("Fully Diluted Valuation")
        st.write(f"${fully_diluted_valuation:,}")

    with col2:
        st.subheader("Circulating Supply")
        st.write(f"{circulating_supply:,} Tokens")

        st.subheader("Total Supply")
        st.write(f"{total_supply:,} Tokens")

        st.subheader("Max Supply")
        st.write(f"{max_supply:,} Tokens")


def plot_correlation_matrix(path):
    df = pd.read_csv(path)
    correlation_matrix = df.pivot(index='Coin', columns='Symbol', values='BTC Correlation')
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')

    plt.title("Correlation Matrix with LPT")
    st.pyplot()



def tech_analysis():
    lpt_price = fetch_crypto_price('livepeer')
    change_font_color('h1','Current Market Price of LPT in RealTime','white')
    change_font_color('h1', f'{lpt_price}$', '#50b8e7')

    change_font_color('h1', 'LPT Market Cap Visualization', 'white')
    symbol = st.text_input('Enter Symbol for Token (e.g., livepeer)', 'livepeer')
    days = st.slider('Select Number of Days for Analysis', min_value=7, max_value=365, value=30)
    market_data = fetch_market_data(symbol, days)

    if market_data:
        st.subheader(f'Market Insights for {symbol.upper()} in the Last {days} Days')
        plot_historical_prices(market_data)
        price_trend = analyze_price_trend(market_data)

        historical_price_analysis = (
            f"Over the past {days} days, {symbol.upper()} has demonstrated a {price_trend} trend in historical prices. "
            f"This suggests a {price_trend} market sentiment, with the token's value {'increasing' if price_trend == 'bullish' else 'decreasing' if price_trend == 'bearish' else 'remaining stable'}."
        )

        st.write(f"**Historical Price Analysis:**\n{historical_price_analysis}\n\n")

        plot_market_cap(market_data)
        market_cap_trend = analyze_market_cap(market_data)
        market_cap_analysis = (
            f"The market capitalization of {symbol.upper()} has exhibited significant {market_cap_trend} over the same period. "
            f"This notable increase in market cap indicates a {market_cap_trend} interest in the token, potentially driven by heightened adoption or positive market sentiment."
        )

        st.write(f"**Market Cap Analysis:**\n{market_cap_analysis}\n\n")

    st.title("Candlestick Chart App")

    df = pd.read_csv('code_files/Data/LPT_1Y.csv')

    plot_candlestick_chart(df)

    st.title('Moving Average')

    window_size = st.slider("Select Moving Average Window Size", min_value=1, max_value=30, value=5)

    calculate_moving_average('code_files/Data/LPT_1Y.csv', window_size)

    st.title("Correlation of LPT token with other coins")

    plot_correlation_matrix("code_files/Data/LPT_Correlation_Matrix.csv")
    market_cap = 188609465
    trading_vol = 31821041
    fully_diluted_valuation = 188609465
    circulating_supply = 30013177
    total_supply = 30013177
    max_supply = 30013177
    display_market_info(market_cap, trading_vol, fully_diluted_valuation, circulating_supply, total_supply,
                        max_supply)


