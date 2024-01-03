
import streamlit as st

# Sample data
mkr_data = {
    "Introduction": {
        "": "Maker (MKR) is a cryptocurrency and a governance token associated with the MakerDAO platform, which operates on the Ethereum blockchain. MakerDAO is a decentralized autonomous organization (DAO) that enables the creation of a stablecoin called DAI.",
        "Imag":"assets/4.png",
        "Popularity": "As of today, Maker holds the position of #57 in the Coinbase ranking.",
        "Image":"assets/3.png"
    },
    "Maker Protocol":{
        "":"""Within the Maker ecosystem, two cryptocurrencies stand out. The first, known as Dai, represents a crypto-backed currency and serves as the flagship product of the Maker platform. Maker itself operates as a Distributed Autonomous Organization (DAO) on the Ethereum blockchain, aiming to mitigate price fluctuations in its primary stablecoin, Dai, against the US dollar.

This dynamic duo forms the foundation of a streamlined crypto banking system leveraging blockchain technology. This system facilitates seamless international payments and peer-to-peer transfers. Through Maker (alongside Ethereum), a decentralized lending platform emerges, where Ether is locked into smart contracts as collateral. The outcome of this process is the creation of the stablecoin Dai.

The stability of Dai is meticulously maintained through a sophisticated system involving collateralized debt positions, autonomous feedback mechanisms, and incentives for external participants. Once generated, Dai can be effortlessly sent to others, utilized for transactions in goods and services, or held as a secure option for long-term savings. This comprehensive setup embodies a revolutionary approach to decentralized finance, fostering a versatile and efficient financial ecosystem.
""",
        "Image":"assets/maker-protocol.png",
    },
    "Key Metrics": {
        "Market Cap": "₹103.4B",
        "img1":"assets/market-cap.png",
        "Trading Volume": "₹6.97B",
        "img2":"assets/market-volume.png",
        "Price": "₹112,874.91",
        "img3":"assets/price.png",
        "Image":"assets/2.png"
    },
    "Tokenomics": {
        "Token Supply": "Circulating supply: 918,769 coins, Maximum supply: 1,005,577 coins",
        "Distribution": "Founders and projects: 69.50%, Team: 15.0%, Seed Round 1: 4.0%, Seed Round 2: 6.0%, Seed Round 3: 5.5%",
        "Image":"assets/1.png"
    }
}

st.set_page_config(page_title="Overview", page_icon="📈")
st.title("Overview")

st.sidebar.title("Navigation")
section_option = st.sidebar.selectbox("Go to", list(mkr_data.keys()))

for section, content in mkr_data.items():
    if section == section_option:
        st.header(section)
        for key, value in content.items():
            
            if key=="Image" or key=="Imag" or key=="img1" or key=="img2" or key=="img3":
                st.image(value)
            else:
                st.subheader(key)
                st.write(value)
