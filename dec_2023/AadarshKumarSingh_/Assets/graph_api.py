import requests
import pandas as pd
from datetime import datetime
import streamlit as st

# Function to make the API call and update the plot
def plot():
    def update_plot():
        response = requests.get(url, headers=headers)
        data = response.json()["data"]["market_chart"]
        timestamps = [datetime.utcfromtimestamp(entry["timestamp"] / 1000) for entry in data]
        prices = [entry["price"] for entry in data]

        df = pd.DataFrame({"Timestamp": timestamps, "Price": prices})

        st.line_chart(df.set_index('Timestamp'))

    # API URL and headers
    url = "https://api.tokeninsight.com/api/v1/history/coins/ocean-protocol"
    headers = {
        "accept": "application/json",
        "TI_API_KEY": "27b2a3d576f54c72bb339b9641ee042a"
    }

    # Set up the Streamlit app
    # The `markdown` function in the code is used to display text in Markdown format in the
    # Streamlit app. Markdown is a lightweight markup language that allows you to format text with
    # headers, lists, links, and other formatting options. In this case, the `markdown` function is
    # used to display the text "**Real-time Prices of Ocean Protocol (OCEAN)**" as a header in the
    # Streamlit app.
    st.markdown("""
        <style>
        .big-font {
            font-size:25px !important;
        }
        </style>
        """, unsafe_allow_html=True)
    st.markdown('<p class="big-font">Real-time Prices of Ocean Protocol (OCEAN)</p>', unsafe_allow_html=True)
    # Update the plot every time the app is rerun
    update_plot()

    # Use 'st' functions to create the app layout
    st.set_option('deprecation.showPyplotGlobalUse', False)  # To suppress Matplotlib deprecation warning
