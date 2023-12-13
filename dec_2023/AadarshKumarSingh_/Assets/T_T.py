import streamlit as st
import pandas as pd
import plotly.express as px
import os

def cc():
    # Specify the encoding when reading the CSV file
    df = pd.read_csv('Assets/Transaction_Timeline.csv', encoding='utf-8')

    # Try to infer the datetime format
    try:
        df['TRANSACTION_DATE'] = pd.to_datetime(df['TRANSACTION_DATE'], errors='coerce')
    except ValueError as e:
        st.error(f"Error: {e}. Please check the format of the 'TRANSACTION_DATE' column.")

    # Plotting using Plotly Express
    fig = px.line(df, x='TRANSACTION_DATE', y='AVERAGE_GAS_PRICE', title='Date vs Average Gas Price')
    
    # Set the x-axis to show both date and year
    fig.update_xaxes(
        dtick="M1",
        tickformat="%Y-%m-%d",
        ticklabelmode="period"
    )
    
    # Display the plot using Streamlit
    st.plotly_chart(fig)

    # Display the dataframe
    # st.dataframe(df.head(10))

# Call the function

