import streamlit as st
import pandas as pd
import requests
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px
import networkx as nx

# Function to fetch UNI token price data for the specified time range
def fetch_uni_data(time_range):
    start_date, end_date = calculate_time_range(time_range)
    url = f"https://api.coingecko.com/api/v3/coins/uniswap/market_chart/range?vs_currency=usd&from={start_date.timestamp()}&to={end_date.timestamp()}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        prices = data.get("prices", [])
        return pd.DataFrame(prices, columns=["Date", "Price"]).set_index("Date")
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching price data: {e}")
        return pd.DataFrame()


# Function to fetch UNI token market cap data for the specified time range
def fetch_uni_market_cap(time_range):
    start_date, end_date = calculate_time_range(time_range)
    url = f"https://api.coingecko.com/api/v3/coins/uniswap/market_chart/range?vs_currency=usd&from={start_date.timestamp()}&to={end_date.timestamp()}&vs_currency=usd"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        market_caps = data.get("market_caps", [])
        return pd.DataFrame(market_caps, columns=["Date", "Market Cap"]).set_index("Date")
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching market cap data: {e}")
        return pd.DataFrame()


# Function to fetch UNI token volume data for the specified time range
def fetch_uni_volume(time_range):
    start_date, end_date = calculate_time_range(time_range)
    url = f"https://api.coingecko.com/api/v3/coins/uniswap/market_chart/range?vs_currency=usd&from={start_date.timestamp()}&to={end_date.timestamp()}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()

        # Check for potential key names for volume data
        potential_keys = ["total_volumes", "volumes", "total_volumes_chart", "volume_chart"]

        for key in potential_keys:
            if key in data:
                volume_data = pd.DataFrame(data[key], columns=["Date", "Volume"]).set_index("Date")
                return volume_data

        # If none of the potential keys are found
        st.warning(f"Volume data not found in the API response. Potential keys: {potential_keys}")
        return pd.DataFrame()

    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching volume data: {e}")
        return pd.DataFrame()


# Function to calculate start and end date based on the time range
def calculate_time_range(time_range):
    end_date = datetime.now()

    if time_range == "1 day":
        start_date = end_date - timedelta(days=1)
    elif time_range == "1 week":
        start_date = end_date - timedelta(weeks=1)
    elif time_range == "1 month":
        start_date = end_date - timedelta(days=30)
    elif time_range == "1 year":
        start_date = end_date - timedelta(days=365)
    elif time_range == "5 years":
        start_date = end_date - timedelta(days=1825)  # 5 years
    else:
        st.error("Invalid time range selected.")
        return None, None

    return start_date, end_date
# Display Uniswap logo using an online image URL
image_url = "https://dappsndefi.com/wp-content/uploads/2020/09/Uniswap-Logo-Large.png"
st.image(image_url)

# Centered title with increased font size
st.markdown("<h1 style='text-align: center; font-size: 40px;'>UNI Token Analysis</h1>", unsafe_allow_html=True)

# Content about Uniswap
uniswap_info = """
_Uniswap is a decentralized finance (DeFi) protocol built on the Ethereum blockchain, enabling automated and permissionless token swaps. 
It uses liquidity pools and an automated market maker (AMM) mechanism, allowing users to trade various ERC-20 tokens directly 
from their wallets. UNI is the governance token of Uniswap, providing holders with voting rights to influence the platform's development 
and changes. Users can also stake UNI to earn rewards and participate in the decentralized governance of the protocol._
"""
st.write(uniswap_info)

# Allow the user to select the time range for price visualization
price_time_range = st.selectbox("Select Time Range for Price (Line Chart)",
                                ["1 day", "1 week", "1 month", "1 year", "5 years"])

# Fetch UNI token price data for the selected time range
df_price = fetch_uni_data(price_time_range)

# Display line chart for price
df_price.index = pd.to_datetime(df_price.index, unit='ms')
st.line_chart(df_price)

# Add a heading for the bar chart
st.subheader("Market Cap")
uniswap_markcap = """ _Market capitalization represents the total value of a cryptocurrency in circulation. It is calculated by multiplying the current market price by the total circulating supply, offering a comprehensive metric to gauge the overall market significance and size of a particular digital asset._"""
st.write(uniswap_markcap)
st.latex("Market Cap = Current Market Price * Total Circulating Supply")

# Allow the user to select the time range for market cap visualization
time_range_market_cap = st.selectbox("Select Time Range for Market Cap",
                                     ["1 day", "1 week", "1 month", "1 year", "5 years"])
# Fetch UNI token market cap data for the selected time range
df_market_cap = fetch_uni_market_cap(time_range_market_cap)
# Display bar chart for market cap with space between bars
df_market_cap.index = pd.to_datetime(df_market_cap.index, unit='ms')
st.bar_chart(df_market_cap, width=1.0)  # Adjust the width as needed

st.subheader("Trading Volume")
uniswap_tradvol = """_Trading volume quantifies the total amount of a cryptocurrency traded within a specified time frame, typically 24 hours. This metric is crucial for assessing market liquidity and gauging the level of interest or activity in a particular digital asset._"""
st.write(uniswap_tradvol)
st.latex("Trading Volume=Total  Quantity  of  Cryptocurrency  Traded")
# Allow the user to select the time range for volume visualization
volume_time_range = st.selectbox("Select Time Range for Volume", ["1 day", "1 week", "1 month", "1 year", "5 years"])

# Fetch UNI token volume data for the selected time range
volume_data = fetch_uni_volume(volume_time_range)

# Check if volume data is available before creating the candlestick chart
if not volume_data.empty:
    # Candlestick chart for trading volume
    fig = go.Figure(data=[go.Candlestick(x=volume_data.index,
                                         open=volume_data['Volume'],
                                         high=volume_data['Volume'],
                                         low=volume_data['Volume'],
                                         close=volume_data['Volume'])])

    fig.update_layout(
        title="Trading Volume",
        xaxis_title="Date",
        yaxis_title="Volume",
        xaxis_rangeslider_visible=False,
        width=800,
        height=400
    )
    st.plotly_chart(fig)
else:
    st.warning("Volume data is not available for the selected time range.")


# Function to fetch UNI revenue data from an API
def fetch_uni_revenue_data():
    try:
        # Define the time range (adjust this according to your needs)
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)  # Example: last 30 days

        # Define the API URL
        api_url = f"https://api.coingecko.com/api/v3/coins/uniswap/market_chart/range?vs_currency=usd&from={start_date.timestamp()}&to={end_date.timestamp()}"

        # Make the API request
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()

        # Assuming the API returns data in the format similar to revenue_data
        return data

    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching UNI revenue data from the API: {e}")
        return None


# Display UNI revenue model pie chart
st.subheader("Revenue Model")
uniswap_rev="""_The revenue model outlines how a cryptocurrency project generates income. This includes sources such as transaction fees, staking rewards, or other mechanisms, providing insights into the financial sustainability and long-term viability of the project._"""
st.write(uniswap_rev)

st.latex("Revenue = Number of Transactions*Average Transaction Fee")
st.write(""" Transaction Fee Revenue Model: In this model, revenue is generated by charging users a fee for each transaction on the blockchain. The total revenue is calculated by multiplying the number of transactions by the average fee per transaction.""")
st.latex("Revenue = Total Staked Amount*Annual Staking Reward Rate")
st.write(""" Staking Reward Revenue Model: In a staking-based revenue model, users lock up their tokens (stake) to support network operations and, in return, receive rewards. The total revenue is calculated by multiplying the total staked amount by the annual staking reward rate.""")

# Function to display UNI revenue model pie chart
def display_revenue_pie_chart(revenue_data):
    try:
        # Process revenue_data and create a DataFrame
        # Replace this with your actual data processing logic

        # Sample data for illustration
        data = {'Component': ['Transaction Fees', 'Staking Rewards', 'Governance', 'Other'],
                'Percentage': [60, 20, 10, 10]}

        df_revenue = pd.DataFrame(data)

        # Create a pie chart using Plotly Express
        fig = px.pie(df_revenue, values='Percentage', names='Component', title='UNI Revenue Model')

        # Display the pie chart
        st.plotly_chart(fig)

    except Exception as e:
        st.error(f"An error occurred: {e}")


# Call the function to fetch data and display the chart
revenue_data = fetch_uni_revenue_data()
if revenue_data is not None:
    display_revenue_pie_chart(revenue_data)
else:
    st.warning("Revenue data is not available.")


# Add a section for Fees with a waterfall chart
st.header("Fees")
uniswap_fees="""_Fees in the cryptocurrency context represent charges incurred by users for various actions, such as transactions or smart contract executions. Understanding fee structures is crucial for users and investors to assess the cost implications of utilizing a blockchain platform._"""
st.write(uniswap_fees)
st.latex("Transaction Fee=Number of Transactions×Average Transaction Fee per Transaction")
st.write("""The total transaction fee is calculated by multiplying the number of transactions by the average fee charged per transaction.""")
st.latex("Gas Fee=Gas Price×Gas Limit")
st.write(""" The total gas fee is calculated by multiplying the gas price (the price of each unit of gas) by the gas limit (the maximum amount of gas units allowed for the transaction).""")

# Function to fetch UNI token fees data from the CoinGecko API
def fetch_uni_fees():
    try:
        # Make an API request to fetch UNI token fees data
        url = "https://api.coingecko.com/api/v3/coins/uniswap/market_chart"
        params = {
            'vs_currency': 'usd',
            'days': 30,  # You can adjust the number of days as needed
        }
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()

        # Assuming the API returns data in a format containing fees information
        fees_data = {
            "Transaction Fees": data.get("total_transaction_fees", 0),
            "Staking Rewards": -data.get("staking_rewards", 0),
            "Other Fees": -data.get("other_fees", 0),
        }

        return pd.DataFrame(list(fees_data.items()), columns=["Source", "Amount"])

    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching fees data from the API: {e}")
        return pd.DataFrame()

# Function to display UNI token fees in a waterfall chart
def display_fees_waterfall_chart():
    # Fetch UNI fees data from the API
    df_fees = fetch_uni_fees()

    # Check if fees data is available before creating the waterfall chart
    if not df_fees.empty:
        # Create a waterfall chart using Plotly
        fig_fees = go.Figure(go.Waterfall(
            x=df_fees["Source"],
            y=df_fees["Amount"],
            textposition="outside",
            connector={"line": {"color": "rgb(63, 63, 63)"}},
        ))

        fig_fees.update_layout(title_text='UNI Fees', showlegend=False)
        st.plotly_chart(fig_fees)

    else:
        st.warning("Fees data is not available.")

# Display UNI fees waterfall chart
display_fees_waterfall_chart()

st.header("On-chain data insights")
st.write("""_On-chain data insights involve a detailed analysis of information recorded on a blockchain. This includes transaction history, smart contract interactions, and other relevant data, offering valuable visibility into user behavior, network health, and the overall functioning of the blockchain._""")

# Function to fetch UNI token on-chain data insights from the CryptoCompare API
def fetch_uni_on_chain_data(api_key):
    try:
        # Make an API request to fetch UNI token on-chain data insights (historical transactions)
        url = f"https://min-api.cryptocompare.com/data/v2/histoday?fsym=UNI&tsym=USD&limit=30&api_key={api_key}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()

        # Assuming the API returns historical transaction data
        transaction_data = data.get("Data", {}).get("Data", [])

        if not transaction_data:
            return pd.DataFrame()

        # Extract relevant transaction data
        df_transaction_data = pd.DataFrame(transaction_data)
        df_transaction_data['time'] = pd.to_datetime(df_transaction_data['time'], unit='s')
        df_transaction_data = df_transaction_data[['time', 'volumeto']]

        return df_transaction_data

    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching UNI on-chain data insights from the CryptoCompare API: {e}")
        return pd.DataFrame()

# Function to display UNI token on-chain data insights in a line chart
def display_on_chain_data_line_chart(api_key):
    # Fetch on-chain data insights from the API
    df_data_insights = fetch_uni_on_chain_data(api_key)

    # Check if data insights are available before creating the line chart
    if not df_data_insights.empty:
        # Display line chart for on-chain data insights
        fig_data_insights = go.Figure()
        fig_data_insights.add_trace(go.Scatter(x=df_data_insights["time"], y=df_data_insights["volumeto"], mode='lines+markers', name='Transaction Volume'))
        fig_data_insights.update_layout(title_text='UNI On-chain Data Insights', xaxis_title='Time', yaxis_title='Transaction Volume (USD)')

        st.plotly_chart(fig_data_insights)

    else:
        st.warning("On-chain data insights are not available.")

# Replace "YOUR_CRYPTOCOMPARE_API_KEY" with your actual CryptoCompare API key
api_key = "da649765151f98b2bde0e0818556fed1c590feed5c4c1013d3fee4ce034cb831"

# Display UNI on-chain data insights line chart
display_on_chain_data_line_chart(api_key)

