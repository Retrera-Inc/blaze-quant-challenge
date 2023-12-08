import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
from datetime import datetime, timedelta

# Function to fetch Ethereum price data
def fetch_ethereum_data():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=730) # Last two years
    url = f"https://api.coingecko.com/api/v3/coins/ethereum/market_chart/range?vs_currency=usd&from={start_date.timestamp()}&to={end_date.timestamp()}"
    response = requests.get(url)
    data = response.json()
    prices = data["prices"]
    return pd.DataFrame(prices, columns=["Date", "Price"]).set_index("Date")


st.title("Example component 1: Ethereum Price Analysis")
df = fetch_ethereum_data()
df.index = pd.to_datetime(df.index, unit='ms')
st.line_chart(df)
# Additional analysis or features can be added here

