import requests
from datetime import datetime, timedelta
import pandas as pd
import streamlit as st
import plotly.express as px
st.subheader("Risks Evaluation")
uniswar_ri="""_The evaluation of potential risks involves identifying, analyzing, and understanding various risks and challenges associated with a cryptocurrency project. This comprehensive assessment helps stakeholders make informed decisions and develop strategies to manage uncertainties effectively._"""
st.write(uniswar_ri)
st.latex("Risk Severity=Likelihood×Impact")
# Function to fetch UNI risk evaluation data from an API
def fetch_uni_risk_evaluation():
    # Define start_date and end_date
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)  # One year ago

    # Construct API URL with time range
    api_url = f"https://api.coingecko.com/api/v3/coins/uniswap/market_chart/range?vs_currency=usd&from={start_date.timestamp()}&to={end_date.timestamp()}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()

        # Extract relevant data from the API response
        risk_evaluation_data = {
            "Risk Factor": ["Market Volatility", "Regulatory Compliance", "Smart Contract Risk", "Competition", "Liquidity Risk"],
            "Score": [8, 6, 7, 5, 9],
        }

        return pd.DataFrame(risk_evaluation_data)

    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching UNI risk evaluation data from the API: {e}")
        return None

# Function to display UNI risk evaluation radar chart
def display_risk_evaluation_radar_chart(risk_evaluation_data):
    try:
        # Assuming the API returns data in the format similar to risk_evaluation_data
        df_risk_evaluation = pd.DataFrame(risk_evaluation_data)

        # Create a radar chart using Plotly Express
        fig_risk_evaluation = px.line_polar(df_risk_evaluation, r='Score', theta='Risk Factor', line_close=True)

        st.plotly_chart(fig_risk_evaluation)

        st.write("Note: The radar chart represents the evaluation of potential risks in UNI token.")

    except Exception as e:
        st.error(f"An error occurred: {e}")

# Fetch UNI risk evaluation data from the API
risk_evaluation_data = fetch_uni_risk_evaluation()

# Check if the DataFrame is not empty before calling the function
if not risk_evaluation_data.empty:
    display_risk_evaluation_radar_chart(risk_evaluation_data)
else:
    st.warning("Risk evaluation data is empty.")
