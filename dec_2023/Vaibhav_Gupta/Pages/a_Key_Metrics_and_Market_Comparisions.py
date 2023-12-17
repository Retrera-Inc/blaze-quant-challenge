import streamlit as st
from PIL import Image
import requests
import json
from datetime import datetime
import pandas as pd

def a():
    st.markdown(
        """
    ## Key Metrics and Market Comparisions : 
    """
    )

    # image_path = "./assets/Revenue_ve_transaction_count.png"
    # image = Image.open(image_path)
    # st.image(image, caption=" # Revenue vs transaction_count (from July'23 onwards-)")

    # st.markdown(
    #     """

    # """
    # )

    # image_path = "./assets/GN0_trading_Volume_vs_Revenue.png"
    # image = Image.open(image_path)
    # st.image(image, caption=" # GNO_Trading_Volume_vs_Revenue (from July'23 onwards-)")

    # st.markdown(
    #     """

    # """
    # )

    # image_path = "./assets/Transaction_count_vs_Transaction_per_second.png"
    # image = Image.open(image_path)
    # st.image(
    #     image,
    #     caption=" # Transaction_count_vs_Transaction_per_second (from July'23 onwards-)",
    # )

    # st.markdown(
    #     """
    # | Key metrics    | :             |
    # | -------------  | ------------- |
    # | Ticket         | GNO           |
    # | Blockchain     | Ethereum      |
    # | Token standard | ERC-20        |
    # | Token type     | governance    |
    # | Token supply   | 10,000,000 GNO   |

    # """
    # )


    def plot():
        def update_plot():
            response = requests.get(url, headers=headers)
            data = response.json()["data"]["market_chart"]
            timestamps = [
                datetime.utcfromtimestamp(entry["timestamp"] / 1000) for entry in data
            ]
            prices = [entry["price"] for entry in data]

            df = pd.DataFrame({"Timestamp": timestamps, "Price": prices})

            st.line_chart(df.set_index("Timestamp"))

        # API URL and headers
        url = "https://api.tokeninsight.com/api/v1/history/coins/gnosis"
        headers = {
            "accept": "application/json",
            "TI_API_KEY": "763c8a709bf840299e284d8ee035d8f7",
        }

        st.markdown(
            """
            <style>
            .big-font {
                font-size:25px !important;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<p style='text-align:center; font-size:22px; font-weight:bold;'>Live Analysis ( GnosisDAO) </p>",
            unsafe_allow_html=True,
        )

        # Update the plot every time the app is rerun
        update_plot()


    def ap():

        url = "https://api.tokeninsight.com/api/v1/coins/gnosis"

        headers = {
            "accept": "application/json",
            "TI_API_KEY": "763c8a709bf840299e284d8ee035d8f7",
        }
        data = requests.get(url, headers=headers)
        data = json.loads(data.text)

        name = data["data"]["name"]
        symbol = data["data"]["symbol"]
        rank = data["data"]["rank"]
        logo = data["data"]["logo"]
        rating = data["data"]["rating"]["rating"]
        rating_updated_date = data["data"]["rating"]["update_date"]
        fully_diluted_valuation = data["data"]["market_data"]["price"][0][
            "fully_diluted_valuation"
        ]
        currency = data["data"]["market_data"]["price"][0]["currency"]
        price_latest = data["data"]["market_data"]["price"][0]["price_latest"]
        market_cap_usd = data["data"]["market_data"]["price"][0]["market_cap"]
        circulating_supply = data["data"]["market_data"]["circulating_supply"]
        circulating_supply_percentage = data["data"]["market_data"][
            "circulating_supply_percentage"
        ]
        circulating_supply_percentage_last_updated = data["data"]["market_data"][
            "last_updated"
        ]
        max_supply = data["data"]["market_data"]["max_supply"]
        price_change_24h = data["data"]["market_data"]["price"][0]["price_change_24h"]
        price_change_percentage_24h = data["data"]["market_data"]["price"][0][
            "price_change_percentage_24h"
        ]

        # Streamlit App
        st.title("Gnosis Market Updates : ")

        # widget.draw()

        st.subheader("General Information : ")
        st.write(f"Name: {name}")
        st.write(f"Symbol: {symbol}")
        st.image(logo, caption="", use_column_width=False, width=100)

        timestamp_milliseconds = int(rating_updated_date)
        timestamp_seconds = timestamp_milliseconds / 1000  # Convert to seconds

        # Convert to datetime object
        date_object = datetime.fromtimestamp(timestamp_seconds)

        formatted_date = date_object.strftime("%Y-%m-%d %H:%M:%S")

        st.subheader(f" Market Data (Last Updated: {formatted_date}):")
        st.write(f"- Market Cap (USD): {round(market_cap_usd,2)}$")
        st.write(f"- Circulating Supply: {round(circulating_supply, 2)} Gnosis")
        st.write(f"- Circulating Supply %: {round(circulating_supply_percentage, 2)}")

        timestamp_milliseconds = int(circulating_supply_percentage_last_updated)
        timestamp_seconds = timestamp_milliseconds / 1000  # Convert to seconds

        # Convert to datetime object
        date_object = datetime.fromtimestamp(timestamp_seconds)

        # Format the date as a string
        formatted_date = date_object.strftime("%Y-%m-%d %H:%M:%S")
        st.write(f"- Last Updated: {formatted_date}")
        st.write(f"- Max Supply: {max_supply}")
        # st.write(f"Currency: {currency}")

        st.write(f"- Latest Price: {round(price_latest, 2)}$")
        plot()
        st.write(f"- Fully Diluted Valuation: {round(fully_diluted_valuation ,2 ) } $")
        st.write(f"- Price Change in last 24 Hour: {round(price_change_24h,4)} $")


    ap()
