import streamlit as st
from PIL import Image
import requests
import plotly.express as px
import pandas as pd

def b():
    st.markdown(
        """
                
    ## Tokenomics :

    The max supply of GNO was initially capped at 10,000,000 to be fully vested in April 2021. However, on 4th May 2022, the Proposal to reduce Gnosis total supply was passed to cap supply at 3 million GNO.

    """
    )
    # image_path = "./assets/content_GNO_Allocation_(1).png"
    # image = Image.open(image_path)
    # st.image(image, caption="Image Source: Token Terminal")

    # API request to get data
    url = "https://api.tokeninsight.com/api/v1/coins/gnosis/tokenomics"
    headers = {
        "accept": "application/json",
        "TI_API_KEY": "763c8a709bf840299e284d8ee035d8f7",
    }
    response = requests.get(url, headers=headers)

    # Check if the API request was successful
    if response.status_code == 200:
        data = response.json()["data"]["token_distributions"]

        # Create a DataFrame for the pie chart
        df = pd.DataFrame(data)

        # Create a pie chart
        fig = px.pie(df, values="percentage", names="holder", title="  Token Distributions")

        # Display the pie chart
        st.plotly_chart(fig)

        # Display additional information
        # st.subheader("Introduction:")
        st.markdown(response.json()["data"]["intro"], unsafe_allow_html=True)
    else:
        st.error(f"Error: {response.status_code}. Unable to fetch data.")


    st.markdown(
        """

    The Initial token distribution of GNO is as follows:

    - 95.80% is allocated to Gnosis Vault, Founders & Project
    - 4.20% is allocated to ICO Investors


    The use of these proceeds are:
    - 5% is allocated to marketing
    - 15% is allocated to operations 
    - 20% is allocated to legal
    - 60% is allocated to core development
    """
    )
    st.markdown(""" # Retrieve Coin Markets """)


    # API request to get data
    url = "https://api.tokeninsight.com/api/v1/coins/gnosis/markets"
    headers = {
        "accept": "application/json",
        "TI_API_KEY": "763c8a709bf840299e284d8ee035d8f7",
    }
    response = requests.get(url, headers=headers)

    # Check if the API request was successful
    if response.status_code == 200:
        data = response.json()["data"]["markets"]

        # Create a DataFrame for the bar chart
        df = pd.DataFrame(data)

        # Create a bar chart
        fig = px.bar(
            df,
            x="exchange_name",
            y="price_latest",
            title=" GnosisDAO Prices on Different Exchanges",
            labels={"price_latest": "Latest Price (USD)"},
            height=500,
        )

        # Customize the layout
        fig.update_layout(xaxis_title="Exchange Name", yaxis_title="Latest Price (USD)")

        # Display the bar chart
        st.plotly_chart(fig)

        # Display additional information
        st.subheader("Gnosis-DAO Overview:")
        st.write(f"Name: {response.json()['data']['name']}")
        st.write(f"Total Markets: {response.json()['data']['page_info']['total_results']}")
    else:
        st.error(f"Error: {response.status_code}. Unable to fetch data.")
    st.markdown(
        """ 
    ### Some of the major exchanges :

    - Uphold : This is one of the top exchanges for United States & UK residents that offers a wide range of cryptocurrencies. Germany & Netherlands are prohibited.

    - Paybis is a global company offering services to residents from 180+ countries, including Canada, Europe, UK, & USA.

    - Kraken : Founded in 2011, Kraken is one of the most trusted names in the industry with over 9,000,000 users, and over $207 billion in quarterly trading volume.

    - Binance : Accepts Australia, Singapore, and most of the world. Canadian & USA residents are prohibited.

    - WazirX : This exchange is part of the Binance Group, which ensures a high standard of quality.  It is the best exchange for residents of India.

        """
    )

    st.markdown(
        """
    ### Major Funding Rounds :

    - 12.5M was raised in a Token Sale in April 2017 where the team raised 250,000 ETH.
    The sale was conducted as a Dutch auction which had a limit of $12.5 million raised or nine million GNO sold,
    whichever came first. 
    The 12.5 million cap was reached selling 418,777 GNO.

    """
    )
