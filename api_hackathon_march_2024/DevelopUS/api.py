# api.py
from dotenv import load_dotenv
import os
import requests


def make_api_call(walletAddress: str):
    query = '''
    query WalletData($walletAddress: String!) {
      walletTraits(walletAddress: $walletAddress) {
        walletAddress
        emails
        ethereumTokenPortfolioValue
        polygonTokenPortfolioValue
        nftPortfolioValue
        lastTransactionDate
      }             
      walletScores(walletAddress: $walletAddress) {
        web3ReputationScore
        authenticityScore
      }
    }
    '''
    variable = {
        "walletAddress": walletAddress
    }
    load_dotenv()
    key = os.getenv("API_KEY")
    endpoint = "https://dashboard.withblaze.app/api/graphql-api"
    headers = {
        "Content-Type": "application/json",
        "x-api-key": key
    }
    data = {
        "query": query,
        "variables": variable
    }

    response = requests.post(endpoint, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None
