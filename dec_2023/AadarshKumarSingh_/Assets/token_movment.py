

import streamlit as st
import pandas as pd

def tm():
    # Load addresses from the CSV file
    addresses_df = pd.read_csv('unique_addresses.csv')
    print ("a")
    st.set_page_config(layout="wide")

    # Display the total number of unique addresses
    total_unique_addresses = len(addresses_df['ADDRESS'].unique())

    highlighted_text = f"<h1 style='text-align: center; color: cyan;'>Total Unique Addresses: {total_unique_addresses}</h1>"
    st.markdown(highlighted_text, unsafe_allow_html=True)
    # Display the list of addresses
    st.write("List of Unique Addresses involved with this token:")
    st.dataframe(addresses_df, width=1200, height=600)
    

