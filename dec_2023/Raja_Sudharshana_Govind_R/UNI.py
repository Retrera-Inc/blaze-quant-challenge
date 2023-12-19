import streamlit as st
import pandas as pd
import datetime as dt
import time as t
import requests
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
from pycoingecko import CoinGeckoAPI


# Create a CoinGecko API client
cg = CoinGeckoAPI()

# Function to fetch UNI token data for the last 365 days
def fetch_uni_data():
    # Get the current timestamp and the timestamp from 365 days ago
    end_timestamp = int(t.time())
    start_timestamp = end_timestamp - 365 * 24 * 60 * 60

    # Get UNI token market chart data
    uni_data = cg.get_coin_market_chart_range_by_id(
        id='uniswap',  # UNI token ID
        vs_currency='usd',
        from_timestamp=start_timestamp,
        to_timestamp=end_timestamp
    )

    # Extract prices, market caps, and volumes
    prices = uni_data.get('prices', [])
    market_caps = uni_data.get('market_caps', [])
    volumes = uni_data.get('total_volumes', [])

    # Create dataframes
    prices_df = pd.DataFrame(prices, columns=['Date', 'Price'])
    market_caps_df = pd.DataFrame(market_caps, columns=['Date', 'Market Cap'])
    volumes_df = pd.DataFrame(volumes, columns=['Date', 'Volume'])

    # Convert timestamps to human-readable dates
    for df in [prices_df, market_caps_df, volumes_df]:
        df['Date'] = df['Date'].apply(lambda x: dt.datetime.fromtimestamp(x / 1000).strftime('%m-%d-%Y'))

    # Set index to 'Date'
    prices_df = prices_df.set_index('Date')
    market_caps_df = market_caps_df.set_index('Date')
    volumes_df = volumes_df.set_index('Date')

    return prices_df, market_caps_df, volumes_df

# Fetch UNI token data
uni_prices, uni_market_caps, uni_volumes = fetch_uni_data()

# Streamlit App
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

import streamlit as st
from pycoingecko import CoinGeckoAPI

# Function to fetch current price of UNI token from CoinGecko API
def fetch_uni_current_price():
    try:
        cg = CoinGeckoAPI()

        # Get the current price
        token_info = cg.get_price(ids='uniswap', vs_currencies=['usd', 'inr'])
        current_price_usd = token_info['uniswap']['usd']
        current_price_inr = token_info['uniswap']['inr']

        return current_price_usd, current_price_inr

    except Exception as e:
        st.error(f"Error fetching current price data: {e}")
        return None, None

# Streamlit app
st.title("UNI Token Price Viewer")

# Button to fetch and display current price
if st.button("Show Current Price"):
    current_price_usd, current_price_inr = fetch_uni_current_price()
    if current_price_usd is not None and current_price_inr is not None:
        st.header(f"Current UNI Token Price")
        st.title(f"USD: ${current_price_usd:.2f}")
        st.title(f"INR: ₹{current_price_inr:.2f}")
    else:
        st.warning("Unable to fetch current price.")

# Display UNI Token Prices
st.subheader('UNI Token Prices Over the Last 365 Days')
st.line_chart(uni_prices)

st.subheader("Market Trends")
st.write("_Uniswap's evolution unfolds through various versions, with Uniswap V3 being the latest milestone. These versions focus on enhancing capital efficiency, providing better execution for traders, and overall infrastructure improvements. The platform's decentralized nature, global accessibility, and user-friendly interface contribute significantly to its continued success._")

st.subheader("Market Cap")
uniswap_markcap = """ _Market capitalization represents the total value of a cryptocurrency in circulation. It is calculated by multiplying the current market price by the total circulating supply, offering a comprehensive metric to gauge the overall market significance and size of a particular digital asset._"""
st.write(uniswap_markcap)
st.latex("Market Cap = Current Market Price * Total Circulating Supply")


# Display UNI Token Market Caps
st.subheader('UNI Token Market Caps Over the Last 365 Days')
st.bar_chart(uni_market_caps)

st.subheader("Trading Volume")
uniswap_tradvol = """_Trading volume quantifies the total amount of a cryptocurrency traded within a specified time frame, typically 24 hours. This metric is crucial for assessing market liquidity and gauging the level of interest or activity in a particular digital asset._"""
st.write(uniswap_tradvol)
st.latex("Trading Volume=Total  Quantity  of  Cryptocurrency  Traded")

# Display UNI Token Trade Volume (Candlestick Chart)
st.subheader('UNI Token Trade Volume Over the Last 365 Days')
fig = go.Figure(data=[go.Candlestick(x=uni_volumes.index,
                open=uni_volumes['Volume'],
                high=uni_volumes['Volume'],
                low=uni_volumes['Volume'],
                close=uni_volumes['Volume'])])
fig.update_layout(xaxis_title='Date', yaxis_title='Volume')
st.plotly_chart(fig)


st.subheader("Risks Evaluation")
uniswar_ri = """_The evaluation of potential risks involves identifying, analyzing, and understanding various risks and challenges associated with a cryptocurrency project. This comprehensive assessment helps stakeholders make informed decisions and develop strategies to manage uncertainties effectively._"""
st.write(uniswar_ri)
st.latex("Risk Severity=Likelihood×Impact")


# Function to fetch UNI risk evaluation data from the CoinGecko module
def fetch_uni_risk_evaluation():
    # Define start_date and end_date
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)  # One year ago

    try:
        # Fetch data from the CoinGecko module
        cg = CoinGeckoAPI()
        data = cg.get_coin_market_chart_range_by_id(id='uniswap', vs_currency='usd',
                                                     from_timestamp=start_date.timestamp(),
                                                     to_timestamp=end_date.timestamp())

        # Extract relevant data from the CoinGecko module response
        risk_evaluation_data = {
            "Risk Factor": ["Market Volatility", "Regulatory Compliance", "Smart Contract Risk", "Competition",
                            "Liquidity Risk"],
            "Score": [8, 6, 7, 5, 9],
        }

        return pd.DataFrame(risk_evaluation_data)

    except Exception as e:
        st.error(f"Error fetching UNI risk evaluation data from the CoinGecko module: {e}")
        return None


# Function to display UNI risk evaluation radar chart
def display_risk_evaluation_radar_chart(risk_evaluation_data):
    try:
        # Assuming the CoinGecko module returns data in the format similar to risk_evaluation_data
        df_risk_evaluation = pd.DataFrame(risk_evaluation_data)

        # Create a radar chart using Plotly Express
        fig_risk_evaluation = px.line_polar(df_risk_evaluation, r='Score', theta='Risk Factor', line_close=True)

        st.plotly_chart(fig_risk_evaluation)

        st.write("Note: The radar chart represents the evaluation of potential risks in UNI token.")

    except Exception as e:
        st.error(f"An error occurred: {e}")


# Fetch UNI risk evaluation data from the CoinGecko module
risk_evaluation_data = fetch_uni_risk_evaluation()

# Check if the DataFrame is not empty before calling the function
if not risk_evaluation_data.empty:
    display_risk_evaluation_radar_chart(risk_evaluation_data)
else:
    st.warning("Risk evaluation data is empty.")


st.subheader("Revenue Model")
uniswap_rev = """_The revenue model outlines how a cryptocurrency project generates income. This includes sources such as transaction fees, staking rewards, or other mechanisms, providing insights into the financial sustainability and long-term viability of the project._"""
st.write(uniswap_rev)

st.latex("Revenue = Number of Transactions * Average Transaction Fee")
st.write(""" Transaction Fee Revenue Model: In this model, revenue is generated by charging users a fee for each transaction on the blockchain. The total revenue is calculated by multiplying the number of transactions by the average fee per transaction.""")
st.latex("Revenue = Total Staked Amount * Annual Staking Reward Rate")
st.write(""" Staking Reward Revenue Model: In a staking-based revenue model, users lock up their tokens (stake) to support network operations and, in return, receive rewards. The total revenue is calculated by multiplying the total staked amount by the annual staking reward rate.""")

# Function to fetch UNI revenue data from the CoinGecko module
def fetch_uni_revenue_data():
    try:
        # Define the time range (adjust this according to your needs)
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)  # Example: last 30 days

        # Fetch data from the CoinGecko module
        cg = CoinGeckoAPI()
        data = cg.get_coin_market_chart_range_by_id(id='uniswap', vs_currency='usd',
                                                     from_timestamp=start_date.timestamp(),
                                                     to_timestamp=end_date.timestamp())

        # Assuming the CoinGecko module returns data in the format similar to revenue_data
        return data

    except Exception as e:
        st.error(f"Error fetching UNI revenue data from the CoinGecko module: {e}")
        return None


# Function to display UNI revenue model pie chart
def display_revenue_pie_chart(revenue_data):
    try:
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



st.subheader("Future Aspects")
uniswap_fa = """_Future prospects involve assessing the anticipated growth, adoption, and success of a cryptocurrency project. This forward-looking analysis aids investors and stakeholders in understanding the project's long-term viability and potential trajectory in the evolving blockchain landscape_"""
st.write(uniswap_fa)
st.latex("Future Price=Current Price×(1 + Expected Percentage Growth)")
st.write("This formula provides a basic estimation of the future price based on an assumed percentage growth rate.")
st.latex("Future Market Cap=Future Price×Total Circulating Supply")
st.write("This formula estimates the future market capitalization based on the projected future price and the total circulating supply.")

# Function to fetch UNI token historical price data from the CryptoCompare API
def fetch_uni_historical_price(api_key):
    try:
        # Make an API request to fetch UNI token historical price data
        url = f"https://min-api.cryptocompare.com/data/v2/histoday?fsym=UNI&tsym=USD&limit=365&api_key={api_key}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()

        # Assuming the API returns historical price data
        historical_data = data.get("Data", {}).get("Data", [])

        if not historical_data:
            return pd.DataFrame()

        # Extract relevant historical price data
        df_historical_price = pd.DataFrame(historical_data)
        df_historical_price['time'] = pd.to_datetime(df_historical_price['time'], unit='s')
        df_historical_price = df_historical_price[['time', 'close']]

        return df_historical_price

    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching UNI historical price data from the CryptoCompare API: {e}")
        return pd.DataFrame()

# Function to display UNI token historical price data in a line chart
def display_historical_price_line_chart(api_key):
    # Fetch historical price data from the API
    df_historical_price = fetch_uni_historical_price(api_key)

    # Check if historical price data is available before creating the line chart
    if not df_historical_price.empty:
        # Display line chart for historical price using Plotly Express
        fig_historical_price = px.line(df_historical_price, x='time', y='close', title='UNI Historical Price',
                                        labels={'close': 'Closing Price (USD)'})
        st.plotly_chart(fig_historical_price)

    else:
        st.warning("Historical price data is not available.")

# Replace "YOUR_CRYPTOCOMPARE_API_KEY" with your actual CryptoCompare API key
api_key = "da649765151f98b2bde0e0818556fed1c590feed5c4c1013d3fee4ce034cb831"

# Display UNI historical price line chart
display_historical_price_line_chart(api_key)

st.write("Note: The displayed historical price data is for demonstration purposes. Adjustments may be needed based on the specific future aspects you are interested in.")

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
st.write("_Uniswap's unique features, such as self-governance, global accessibility, and pseudonymity, make it a cornerstone in the decentralized exchange landscape. The analysis of price variations and market trends reveals the platform's resilience and adaptability. With each version, Uniswap not only maintains a significant market cap but also reflects the trust of its community and its ability to navigate the dynamic DeFi ecosystem.For investors and users seeking decentralized, efficient, and community-driven trading, Uniswap stands tall, offering a rich history of innovation and a steadfast commitment to user empowerment. As the DeFi landscape continues to evolve, Uniswap remains a key player, shaping the future of decentralizedfinance._")


