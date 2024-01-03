import streamlit as st
from PIL import Image

def g():
    # with open("style.css") as f:
    #     st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

    st.markdown(
        """
    ## Market Analysis Based on Social Insights  :


    """
    )

    image_path = "./assets/prediction_theory.png"
    image = Image.open(image_path)
    st.image(image, caption="")

    st.subheader("Based on the above graph analysis we can conclude some imp aspects : ")

    st.markdown(
        """Some important key mentions regarding the terms : 
                
                -        - Price Pridiction : Gnosis price forecast for December 22, 2023 based on the last 30 days movements .
                - Volatility : 30 day variation in a price of a particular asset .
                - 50-Day SMA : (Simple Moving Average as on  Dec 17,2023) 
                - 14-Day RSI : 14 -Day Relative Strength Index 
                - Fear & Greed Index : Refering to the current sentiment of the market . (0-24 : Extreme Fear ; 25-49 Fear ; 50 : Neutral ; 51-75 : Greed ; 76 -100 : Extreme Greed  )
                - Green Days : Number of green days in the past 30 days .
                - 200-Day SMA : 200 - Day Simple Moving Average .

                According to the current Gnosis price prediction, the price of Gnosis is predicted to drop by -3.15% and reach $ 212.39 by December 22, 2023. According to these technical indicators, the current sentiment is Neutral while the Fear & Greed Index is showing 73 (Greed). 
                Gnosis recorded 13/30 (43%) green days with 8.99% price volatility over the last 30 days. Based on these Gnosis forecast, it's now a good time to buy Gnosis.
                
                """
    )

    image_path = "./assets/up_down_analysis.png"
    image = Image.open(image_path)
    st.image(image, caption=" Some POS-NEG aspects of GNOSIS predictions")

    st.subheader("Some Major Advancements in these gone months : ")

    st.markdown(
        """          - Gnosis Pay : Gnosis Pay promises to deliver something DeFi’s faithful have envisioned for years: a decentralised, crypto-based payments network.On the surface, Gnosis Pay aims to function no differently than the Visa-based debit cards millions use for everyday purchases. But under the hood, it uses blockchain tech instead of banks and the Swift system to facilitate payments.

                    - Gnosis has made 14 investments. Their latest investment was in Kinetex Network as part of their Seed on November 11, 2023.
                    - Gnosis has 1 portfolio exit. Their latest portfolio exit was Safe on July 11, 2022.
                    - Gnosis has 10 strategic partners and customers. Gnosis recently partnered with OriginTrail on August 8, 2023.
                    """
    )

    image_path = "./assets/Comepition_Analysis.jpeg"
    image = Image.open(image_path)
    st.image(image, caption=" Market Comparisions VS GNO ")

    st.markdown(
        """

    1. Kujira(KUJI) is a finance, blockchain, and software development platform that builds DApps for crypto users. The whitepaper states that this platform aims to make DeFi generate income irrespective of the market being up or down and help retail traders tap potentials beyond exchange, staking, and ICOs and be at par with the big traders. Kujira has chosen Terra as a base of its DApp because Terra seeks to include advanced protocols, developments, and opportunities for providing beneficial products. 

    2. PancakeSwap(CAKE) is a decentralized finance (DeFi) blockchain app that enables its users to swap crypto tokens. The PancakeSwap platform allows users to trade without requiring them to go through a centralized exchange. The PancakeSwap platform aims to provide an opportunity for users to trade and earn crypto on the Binance Smart Chain within seconds.
    3. ApeCoin (APE) is an ERC-20 token used within the APE ecosystem. ApeCoin is the ecosystem’s governance token, allowing ApeCoin holders to participate in ApeCoin DAO. ApeCoin will also be used to access games, merchandise, events, and services.
    4. ROSE is a cryptocurrency that powers Oasis Protocol, a layer one blockchain that aims to be privacy-preserving and scalable. Oasis Protocol enables fast transaction speeds and the creation of private smart contracts. The ROSE token is used to pay for transaction fees and for staking to validate Oasis Protocol’s proof of stake blockchain.
    5.FET is an Ethereum token that powers Fetch.ai, a decentralized machine learning platform for applications such as asset trading, gig economy work, and energy grid optimization. Fetch.ai’s first decentralized finance application helps Uniswap users automate trading according to predefined conditions.
    6. SEI is the native token of the Sei blockchain network. Sei was designed to provide developers with the infrastructure needed to build efficient and secure decentralized exchanges. SEI tokens can be used to pay network gas fees and participate in governance. SEI tokens can also be staked to secure the network.


    """
    )
