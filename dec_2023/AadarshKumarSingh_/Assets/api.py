import streamlit as st
import requests
import json
import Assets.widget as widget 
from Assets.balance import m
from datetime import datetime
from Assets.graph_api import plot



def ap():
    url = "https://api.tokeninsight.com/api/v1/coins/ocean-protocol"
    headers = {
        "accept": "application/json",
        "TI_API_KEY": "27b2a3d576f54c72bb339b9641ee042a"
    }



    data = requests.get(url, headers=headers)
    data = json.loads(data.text)

    name = data['data']['name']
    symbol = data['data']["symbol"]
    rank = data['data']["rank"]
    logo = data['data']["logo"]
    rating = data['data']['rating']['rating']
    rating_updated_date = data['data']['rating']['update_date']
    fully_diluted_valuation = data["data"]["market_data"]["price"][0]["fully_diluted_valuation"]
    currency = data["data"]["market_data"]["price"][0]["currency"]
    price_latest = data["data"]["market_data"]["price"][0]["price_latest"]
    market_cap_usd = data["data"]["market_data"]["price"][0]["market_cap"]
    circulating_supply = data["data"]["market_data"]["circulating_supply"]
    circulating_supply_percentage = data["data"]["market_data"]["circulating_supply_percentage"]
    circulating_supply_percentage_last_updated = data["data"]["market_data"]["last_updated"]
    max_supply = data["data"]["market_data"]["max_supply"]
    price_change_24h = data["data"]["market_data"]["price"][0]["price_change_24h"]
    price_change_percentage_24h = data["data"]["market_data"]["price"][0]["price_change_percentage_24h"]

    # Streamlit App
    st.title("Ocean Protocol Information")

    widget.draw()

    st.subheader("General Information")
    st.write(f"Name: {name}")
    st.write(f"Symbol: {symbol}")
    st.image(logo, caption="Ocean Protocol", use_column_width=False, width=100)

    st.subheader("Rating Information by tokeninsight")
    st.write(f"- Rating: {rating}")

    timestamp_milliseconds = int(rating_updated_date)
    timestamp_seconds = timestamp_milliseconds / 1000  # Convert to seconds

    # Convert to datetime object
    date_object = datetime.fromtimestamp(timestamp_seconds)

    # Format the date as a string
    formatted_date = date_object.strftime('%Y-%m-%d %H:%M:%S')
    st.write(f"- Rating Update : {formatted_date}")

    st.subheader("Market Data")
    st.write(f"- Rank: {rank}")
    st.write(f"- Market Cap (USD): {market_cap_usd}$")
    st.write(f"- Circulating Supply: {circulating_supply} Ocean")
    st.write(f"- Circulating Supply %: {circulating_supply_percentage}")

    timestamp_milliseconds = int(circulating_supply_percentage_last_updated)
    timestamp_seconds = timestamp_milliseconds / 1000  # Convert to seconds

    # Convert to datetime object
    date_object = datetime.fromtimestamp(timestamp_seconds)

    # Format the date as a string
    formatted_date = date_object.strftime('%Y-%m-%d %H:%M:%S')
    st.write(f"- Last Updated: {formatted_date}")
    st.write(f"- Max Supply: {max_supply}")
    # st.write(f"Currency: {currency}")
    st.write(f"- Latest Price: {price_latest}$")
    plot()
    st.write(f"- Fully Diluted Valuation: {fully_diluted_valuation}$")
    st.write(f"- Price Change in last 24 Hour: {price_change_24h}$")


    m()
    # Optional: Display raw JSON data
    with st.expander("Raw JSON Data"):
        st.json(data)


