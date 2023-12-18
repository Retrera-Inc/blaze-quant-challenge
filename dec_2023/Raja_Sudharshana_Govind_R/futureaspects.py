import streamlit as st
import pandas as pd
import requests
import plotly.express as px

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
