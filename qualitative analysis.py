# analysis.py

import requests
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

def fetch_market_data(token_symbol):
    # Placeholder function to fetch market data from CoinGecko API
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={token_symbol.lower()}&vs_currencies=usd'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return {"current_price": data[token_symbol.lower()]["usd"]}
    else:
        return {"error": "Unable to fetch market data"}

def fetch_on_chain_data(token_symbol):
    # Placeholder function to fetch on-chain data
    # Replace this with actual code to retrieve on-chain data
    return {"transactions": 10000, "holders": 5000}

def calculate_percentage_change(old_value, new_value):
    return ((new_value - old_value) / old_value) * 100 if old_value != 0 else 0

def perform_sentiment_analysis(text):
    # Placeholder for sentiment analysis using nltk
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)["compound"]
    
    if sentiment_score >= 0.05:
        return "Positive"
    elif sentiment_score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def analyze_token(token_symbol, qualitative_info=None):
    market_data = fetch_market_data(token_symbol)
    on_chain_data = fetch_on_chain_data(token_symbol)

    # Additional quantitative analysis
    old_price = 900  # Placeholder for previous day's closing price
    price_change_percentage = calculate_percentage_change(old_price, market_data.get("current_price", 0))

    market_cap = market_data.get("current_price", 0) * on_chain_data.get("holders", 0)

    # Qualitative analysis
    community_sentiment = perform_sentiment_analysis(qualitative_info) if qualitative_info else "Not available"

    analysis_results = {
        "Token Symbol": token_symbol,
        "Current Price (USD)": market_data.get("current_price", "N/A"),
        "Price Change (24h)": f"{price_change_percentage:.2f}%",
        "Total Transactions": on_chain_data.get("transactions", "N/A"),
        "Total Holders": on_chain_data.get("holders", "N/A"),
        "Market Cap": f"${market_cap:,.2f}",
        "Community Sentiment": community_sentiment,
    }

    return analysis_results
