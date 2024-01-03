import streamlit as st
import requests
from Pages.d_Governance_Mechanism_and_Business_Model import d
from Pages.a_Key_Metrics_and_Market_Comparisions import a
from Pages.b_Tokenomics import b
from Pages.c_On_chain_Data_Insights import c
from Pages.e_Significant_Project_and_Milestones import e
from Pages.f_Social_Activity import f
from Pages.g_Social_Insights import g
from Pages.h_Why_build_on_GNOSIS_Chain import h 
from Pages.i_Evaluation_and_Potential_Risks import i
from Pages.j_Whitepaper_GNO import j 
from Pages.k_Risk_Factor_Analysis import k
from PIL import Image


st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://dynamic-assets.coinbase.com/55746ffc2acea9567c7b3281808e3c2bb6f438af89da07736a6889d716a8016857251c6be9a6e731604910f10b43355b2a80f4e6677f0504adbc77a4a35ba00c/asset_icons/b2d894b2a6f48012d6c76968f05d2012bf0aa0a432a56f7236eda53fd35e70d6.png);
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
                
            }
            [data-testid="stSidebarNav"]::before {
                content: "GNOSIS";
                margin-left: 30px;
                margin-top: 0px;
                font-size: 30px;
                position: relative;
                top: 0px;
            }
            [data-testid="stSidebarNav"]{
                li {display: none;}
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

def default():
    st.title(
        """
    Overview : All about GNO token and GNOSIS-Chain : """
    )
    image_path = "./assets/Attlas_Blog_Phân-tích-token-45.jpg"
    image = Image.open(image_path)
    st.image(image, caption="")

    st.header("""  GNO'S TEAM INFO """)

    

    # API request to get team data
    url = "https://api.tokeninsight.com/api/v1/coins/gnosis/teams"
    headers = {
        "accept": "application/json",
        "TI_API_KEY": "763c8a709bf840299e284d8ee035d8f7",
    }
    response = requests.get(url, headers=headers)

    # Check if the API request was successful
    if response.status_code == 200:
        team_data = response.json()["data"]

        # Display team information
        for member in team_data:
            st.image(member["pic"], width=150)
            st.markdown(f"## {member['name']}")
            st.write(f"**{member['title']}**")
            st.markdown(member["desc"], unsafe_allow_html=True)
            st.write(f"LinkedIn: [{member['name']}]({member['links']['linkedin']})")
            st.markdown("---")  # Add a horizontal line between team members
    else:
        st.error(f"Error: {response.status_code}. Unable to fetch team data.")


    st.markdown(
        """ ### Major aspects of Gnosis Ecosystem :

    - Gnosis is a decentralized platform built on the Ethereum blockchain,which strives to create a global, open prediction market.
    - It operates as a decentralized autonomous organization (DAO),providing infrastructure for various types of decentralized applications (dApps).
    - Gnosis was founded in 2015 with a focus on building prediction markets to enable worldwide access to accurate information.
    - The platform's native cryptocurrency, GNO, is used to operate and govern the platform.
    - Gnosis has a maximum supply of 3,000,000 coins, with a circulating supply of 2,589,588 GNO at the time of writing.
    - Gnosis Chain is secured by over 100k validators around the world.


    The core goal of Gnosis is to build a decentralized platform that allows anyone to participate in the prediction market, to customize information search and to become the standard for predictive assets.
    """
    )
    # ----------------------------------------------------------------------------
    st.markdown(
        """
    ## TimeLine  :

    - The protocol founders, Martin Koppelmann (CEO) and Stefan George (CTO), finally launched Gnosis in 2017
    - Published whitepaper 6/6/2018
    - ( GnosisDAO + Gnosis Chain ) In late 2020, Gnosis announced plans to fully decentralize into a DAO (Decentralized Autonomous Organization).
    - ( xDai + Gnosis ) In November 2021, the xDai and GnosisDAO communities voted to combine their vibrant ecosystems to create the Gnosis Chain.
    - Merged with GBC - December 8,2022
    -  On April 13th, 2023 the Safe team announced that all users on Gnosis Chain can execute sponsored transactions for the next 30 days.

    ## Table of Content :

    - Key Metrics and Market Comparisions
    - Tokenomics
    - On-chain Data Insights
    - Governance Mechanisms and Business Model
    - Significance Project Milestones
    - Social Insights
    - Why build on GNOSIS CHAIN ?
    - Evaluation of Potential Risks and Future Prospects
    - GNO Whitepaper

    """
    )

def key():
    a()
def tokeno():
    b()
def chain():
    c()
def token_model():
    d()
def mile():
    e()
def soc_in():
    g()
def build():
    h()
def evalu():
    i()
def white():
    j()
def rf():
    k()

def main():
    menu = ["Overview",
            "Key Metrics and Market Comparision",
            "Tokenomics",
            "On chain Data Insights",
            "Governance Mechanism and Business Model",
            "Significant Project and Milestones",
            "Social Insights",
            "Why build on GNOSIS Chain",
            "Evaluation and Potential Risks",
            "Analysis", 
            "Whitepaper",]
    choice = st.sidebar.selectbox("Contents", menu, index=0)
    if choice=="Overview":
        default()
    elif choice=="Key Metrics and Market Comparision":
        key()
    elif choice == "Tokenomics":
        tokeno()
    elif choice == "On chain Data Insights":
        chain()
    elif choice == "Governance Mechanism and Business Model":
        token_model()
    elif choice == "Significant Project and Milestones":
        mile()  
    elif choice == "Social Insights":
        soc_in()
    elif choice == "Why build on GNOSIS Chain":
        build()
    elif choice == "Evaluation and Potential Risks":
        evalu()
    elif choice == "Analysis":
        rf()
    elif choice == "Whitepaper":
        white() 
    
    
if __name__ == "__main__":
    main()