import requests
from dotenv import load_dotenv
load_dotenv()
import os
API_KEY =os.getenv("BLAZEAI_API_KEY")


BLAZE_API_URL = "https://dashboard.withblaze.app/api/graphql-api"




QUERY = """
query WalletTraits($walletAddress: String!){
    walletTraits(walletAddress: $walletAddress){
        ethereumTokenPortfolioValue
        polygonTokenPortfolioValue
        nftPortfolioValue
        arbitrumTokenPortfolioValue
        bscTokenPortfolioValue
        baseTokenPortfolioValue
        optimismTokenPortfolioValue
        washCategory
        volumeCategory
        activityCategory
        lastTransactionDate
    }
}
"""



def fetch_data_for_wallet(wallet_address):

    headers = {
        'Content-Type': 'application/json',
        'x-api-key': API_KEY
    }


    request_body = {"query": QUERY, "variables": {"walletAddress": wallet_address}}

    try:

        response = requests.post(BLAZE_API_URL, json=request_body, headers=headers)
        response.raise_for_status()  # Raise an exception for 4XX and 5XX status codes
        return response.json().get("data", {}).get("walletTraits", {})
    except requests.exceptions.RequestException as e:
        print(f"Error executing GraphQL query: {e}")
        return None



def get_walletportfolio(wallet_address):
    # wallet_address = "0x690B9A9E9aa1C9dB991C7721a92d351Db4FaC990"


    wallet_data = fetch_data_for_wallet(wallet_address)
    if wallet_data:

        ethereum_token_value = wallet_data.get("ethereumTokenPortfolioValue")
        polygon_token_value = wallet_data.get("polygonTokenPortfolioValue")
        nft_value = wallet_data.get("nftPortfolioValue")
        arbitrum_token_value = wallet_data.get("arbitrumTokenPortfolioValue")
        bsc_token_value = wallet_data.get("bscTokenPortfolioValue")
        base_token_value = wallet_data.get("baseTokenPortfolioValue")
        optimism_token_value = wallet_data.get("optimismTokenPortfolioValue")
        wash_category = wallet_data.get("washCategory")
        volume_category = wallet_data.get("volumeCategory")
        activity_category = wallet_data.get("activityCategory")
        last_transaction_date = wallet_data.get("lastTransactionDate")



        wallet_info = {
            "ethereumTokenPortfolioValue": ethereum_token_value,
            "polygonTokenPortfolioValue": polygon_token_value,
            "nftPortfolioValue": nft_value,
            "arbitrumTokenPortfolioValue": arbitrum_token_value,
            "bscTokenPortfolioValue": bsc_token_value,
            "baseTokenPortfolioValue": base_token_value,
            "optimismTokenPortfolioValue": optimism_token_value,
            "washCategory": wash_category,
            "volumeCategory": volume_category,
            "activityCategory": activity_category,
            "lastTransactionDate": last_transaction_date
        }

        # Print or use the dictionary as needed
        print("Wallet Info:", wallet_info)

        return wallet_info

# a=get_walletportfolio("0x690B9A9E9aa1C9dB991C7721a92d351Db4FaC990")
