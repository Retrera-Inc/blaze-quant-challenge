import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime
st.header("Tokenomics")
uni_swap_tok="""_Tokenomics refers to the economic model and structure governing a cryptocurrency. It encompasses factors such as token distribution, supply mechanisms, and associated policies, providing insights into the token's utility, governance, and overall design._"""
st.write(uni_swap_tok)
st.latex("Total Token Supply=Circulating Supply+Locked/Reserved Tokens+Burned Tokens")
st.write("This formula calculates the total number of tokens, including those in circulation, reserved for specific purposes, and those that have been burned or destroyed.")
st.latex("Token Distribution Percentage=(Number of Tokens in a Wallet or Category /Total Token Supply ) ×100")
st.write("This formula calculates the percentage of tokens held by a specific category, such as team members, investors, or the community.")
st.latex("Inflation Rate=(Newly Created Tokens/Current Total Token Supply)*100")
st.write("This formula calculates the percentage increase in the token supply due to new tokens being created (applies to inflationary tokens)")
# Function to fetch UNI tokenomics data from the API


import streamlit as st
import pandas as pd
import plotly.express as px
import requests

# Function to fetch UNI token supply data from the CryptoCompare API
def fetch_uni_token_supply(api_key):
    try:
        url = f"https://min-api.cryptocompare.com/data/coins/markets?vs_currency=usd&ids=uniswap&order=market_cap_desc&sparkline=false&api_key={api_key}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()

        if not data or "circulating_supply" not in data:
            st.warning("UNI token supply data is not available.")
            return None

        # Extract relevant token supply data
        token_supply = data["circulating_supply"]

        return token_supply

    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching UNI token supply data from the CryptoCompare API: {e}")
        return None

# Function to visualize metrics
def visualize_metrics(token_distribution):
    # Horizontal Bar Chart for Token Distribution
    df_token_distribution = pd.DataFrame(list(token_distribution.items()), columns=["Category", "Percentage"])
    fig_bar_horizontal = px.bar(df_token_distribution, x="Percentage", y="Category", orientation='h',
                                text="Percentage", title="Token Distribution", labels={"Percentage": "Percentage"})
    fig_bar_horizontal.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    st.plotly_chart(fig_bar_horizontal)

# Replace "YOUR_CRYPTOCOMPARE_API_KEY" with your actual CryptoCompare API key
api_key = "da649765151f98b2bde0e0818556fed1c590feed5c4c1013d3fee4ce034cb831"

# Placeholder values, replace with actual data
token_distribution = {"Team": 10, "Liquidity Pools": 20, "Community": 70}

# Visualize metrics
visualize_metrics(token_distribution)

st.write("Note: The data is fetched from the CryptoCompare API and for demonstration purposes.")

