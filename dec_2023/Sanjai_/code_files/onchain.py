import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def plot_nvt_ratio(path):
    df = pd.read_csv(path)
    df["DateTime"] = pd.to_datetime(df["DateTime"])
    st.line_chart(df.set_index("DateTime")["NVT Ratio"])

    last_24h_change = df['NVT Ratio'].pct_change().iloc[-1] * 100

    _week_low = df['NVT Ratio'].min()
    all_time_high = df['NVT Ratio'].max()
    all_time_low = df['NVT Ratio'].min()

    st.header("Metrics")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(f"Last 24h Change: {last_24h_change:.2f}%")
        st.subheader(f"52-Week Low: {_week_low}")

    with col2:
        st.subheader(f"All Time High: {all_time_high}")
        st.subheader(f"All Time Low: {all_time_low}")



def plot_average_transaction_price(path):
    df = pd.read_csv(path)
    df["DateTime"] = pd.to_datetime(df["DateTime"])

    st.line_chart(df.set_index("DateTime")["Average Transaction Size"])

    df['7-Day Average'] = df['Price'].rolling(window=7).mean()
    df['7-Day High'] = df['Price'].rolling(window=7).max()
    df['7-Day Low'] = df['Price'].rolling(window=7).min()

    last_24h_change = df['Price'].pct_change().iloc[-1] * 100
    _7_day_average = df['7-Day Average'].iloc[-1]
    _7_day_high = df['7-Day High'].max()
    _7_day_low = df['7-Day Low'].min()

    st.header("Metrics")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(f"Last 24h Change: {last_24h_change:.2f}%")
        st.subheader(f"7-Day Average: ${_7_day_average:.2f}")

    with col2:
        st.subheader(f"7-Day High: ${_7_day_high:.2f}")
        st.subheader(f"7-Day Low: ${_7_day_low:.2f}")



def plot_volatility_vs_price(path):
    df = pd.read_csv(path)
    df["DateTime"] = pd.to_datetime(df["DateTime"])

    df['30-Day High'] = df['Price'].rolling(window=30).max()
    df['30-Day Low'] = df['Price'].rolling(window=30).min()


    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Volatility"], df["Price"], label='Volatility vs. Price', color='b')
    ax.plot(df["DateTime"], df['30-Day High'], label='30-Day High', linestyle='--', color='orange')
    ax.plot(df["DateTime"], df['30-Day Low'], label='30-Day Low', linestyle='--', color='green')

    ax.set_xlabel("Volatility")
    ax.set_ylabel("Price")
    ax.set_title("Volatility vs. Price Over Time")
    ax.legend()

    plt.xticks(rotation=45)
    st.pyplot(fig)
    _30_day_high = df['30-Day High'].max()
    _30_day_low = df['30-Day Low'].min()

    st.header("Metrics")
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"30-Day High: {_30_day_high:.2f}%")
    with col2:
        st.write(f"30-Day Low: {_30_day_low:.2f}%")


def plot_new_addresses(path):
    df = pd.read_csv(path)
    df["DateTime"] = pd.to_datetime(df["DateTime"])

    df['7-Day NA Change (%)'] = df['New Addresses'].pct_change(periods=7) * 100

    fig, ax1 = plt.subplots(figsize=(10, 6))

    color = 'tab:blue'
    ax1.set_xlabel("Date")
    ax1.set_ylabel("New Addresses", color=color)
    ax1.plot(df["DateTime"], df["New Addresses"], marker='o', linestyle='-', color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel("7-Day NA Change (%)", color=color)
    ax2.plot(df["DateTime"], df["7-Day NA Change (%)"], marker='o', linestyle='-', color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    ax1.set_title("New Addresses and 7-Day NA Change Over Time")

    plt.xticks(rotation=45)

    st.pyplot(fig)

    st.header("Metrics")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("New Addresses")
        st.write(f"Max New Addresses: {df['New Addresses'].max()}")
        st.write(f"Min New Addresses: {df['New Addresses'].min()}")
    with col2:
        st.subheader("7-Day NA Change (%)")
        st.write(f"Max 7-Day NA Change: {df['7-Day NA Change (%)'].max()}")
        st.write(f"Min 7-Day NA Change: {df['7-Day NA Change (%)'].min()}")


def plot_transactions_vs_price(path):
    df = pd.read_csv(path)
    df["DateTime"] = pd.to_datetime(df["DateTime"])
    df['7-Day Average'] = df['Number of Transactions'].rolling(window=7).mean()
    df['7-Day High'] = df['Number of Transactions'].rolling(window=7).max()
    df['7-Day Low'] = df['Number of Transactions'].rolling(window=7).min()
    st.line_chart(df.set_index("DateTime")[["Number of Transactions", "Price"]])
    st.subheader("Metrics")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(f"7-Day Average: {df['7-Day Average'].iloc[-1]:.2f}$")

    with col2:
        st.write(f"7-Day High: {df['7-Day High'].iloc[-1]:.2f}$")

    with col3:
        st.write(f"7-Day Low: {df['7-Day Low'].iloc[-1]:.2f}$")

def change_font_color(element, text, font_color):
    st.markdown(f'<{element} style="color: {font_color};">{text}</{element}>', unsafe_allow_html=True)

def onchain_analysis():


    change_font_color('h1',"Network Value to Transaction (NVT) Ratio Plot",'#50B8E7')
    plot_nvt_ratio("code_files/Data/NVT-Ratio.csv")


    change_font_color('h1',"Average Transaction size",'#50B8E7')
    plot_average_transaction_price("code_files/Data/average-transaction-price.csv")


    change_font_color('h1','Volatile VS Price','#50B8E7')
    plot_volatility_vs_price("code_files/Data/volatile-price.csv")


    change_font_color('h1','New Active Address Creation in Chain','#50B8E7')
    plot_new_addresses("code_files/Data/Daily-Active-Addresses.csv")


    change_font_color("h1","Transaction Vs Price",'#50B8E7')
    plot_transactions_vs_price("code_files/Data/number-of-transaction.csv")