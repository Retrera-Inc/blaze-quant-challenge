import streamlit as st
import requests

def get_token_balance(wallet_address):
    api_url = "https://api.etherscan.io/api"
    contract_address = "0x967da4048cD07aB37855c090aAF366e4ce1b9F48"
    api_key = "9I3NV1PZBMF73HRHR2DHQPSJ6EIH4UH5CQ"

    payload = {
        "module": "account",
        "action": "tokenbalance",
        "contractaddress": contract_address,
        "address": wallet_address,
        "tag": "latest",
        "apikey": api_key
    }

    response = requests.get(api_url, params=payload)

    if response.status_code == 200:
        data = response.json()
        status = data.get("status")
        message = data.get("message")

        if status == "1" and message == "OK":
            result = data.get("result")
            return result
        else:
            return f"Error: {message}"
    else:
        return f"Error: Unable to connect to the API (Status code: {response.status_code})"

def m():
    st.subheader("OCEAN Token Balance Checker")

    # Get wallet address from user input
    wallet_address = st.text_input("Enter Ethereum Wallet Address: ")
    st.write("for ex :- 0x744727A6fC563f54Fd0f6F0442c0BD1E212011f9")

    if st.button("Check Balance"):
        if wallet_address:
            result = get_token_balance(wallet_address)
            result = float(result) / 1e18
            st.write(f"Token Balance: {result}")
        else:
            st.warning("Please enter a valid Ethereum Wallet Address.")

