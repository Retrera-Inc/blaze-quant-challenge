import streamlit as st
import pandas as pd
import plotly.express as px
import os

def fetch_data(from_address=None, to_address=None):
    # Get the current working directory
    current_directory = os.path.dirname(os.path.realpath(__file__))

    # Construct the file path for the CSV file
    file_path = os.path.join(current_directory, 'from_to_txgrouped.csv')

    try:
        # Read data from the CSV file
        df = pd.read_csv(file_path)

        # If from_address and to_address are provided, apply filters
        if from_address is not None and to_address is not None:
            df = df[(df['UNIQUE_FROM_ADDRESSES'] == from_address) & (df['UNIQUE_TO_ADDRESSES'] == to_address)]

        return df

    except FileNotFoundError:
        st.error("CSV file not found. Please make sure 'from_to_txgrouped.csv' is in the same folder as the script.")
        return pd.DataFrame()  # Return an empty DataFrame if the file is not found

def cc():
    # Fetch entire dataset
    df = fetch_data()

    if df.empty:
        st.warning("No data found in the dataset.")
    else:
        # Display the first 10 entries in Streamlit
        # st.write("First 10 entries of the dataset:")
        # st.write(df.head(10))

        # Create a line graph using Plotly Express
        line_chart = px.line(df, x='TRANSACTION_DATE', y='AVERAGE_TRANSACTION_VALUE', title='Average Transaction Value Over Time')
        st.plotly_chart(line_chart)



