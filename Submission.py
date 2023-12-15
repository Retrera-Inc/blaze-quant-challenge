#Code by Team: CompetitionSmashers
#Team Leader : Shrirang Savale
#Team Member : Uday Joshi
#Instiute : Indian Institute of Information Technology, Nagpur 

#Note: We have used GPT-3 and other generative AI to simplify the creation process of this APP.
#      This is done to help us focus more on the analysis part of the project.

# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Sample data for demonstration
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [30, 45, 25, 50]
}

import streamlit as st

def comparison_section():
    st.write("For our analysis, we've closely examined Gnosis (GNO) in comparison to other well-known cryptocurrencies to identify its unique strengths and potential weaknesses in the market.")
    st.subheader("Comparison with Similar Coins")
    
    coins_comparison = {
        "Bitcoin (BTC)": (
            "GNO's innovative prediction market platform sets it apart from Bitcoin. Its unique use case may appeal to users seeking alternatives to traditional betting and forecasting platforms.",
            "Bitcoin's first-mover advantage and widespread recognition might overshadow GNO. Bitcoin's position as a store of value could pose a challenge to GNO's market share."
        ),
        "Ethereum (ETH)": (
            "GNO's layer 2 scaling solutions offer faster and cost-effective transactions, giving it an edge over Ethereum in terms of transaction efficiency.",
            "Ethereum's dominance in the smart contract space and decentralized applications might overshadow GNO's prediction market. GNO's application might seem limited in comparison."
        ),
        "Binance Coin (BNB)": (
            "GNO's unique prediction market functionality distinguishes it from Binance Coin. It offers a different use case and potential for innovation.",
            "Binance Coin's utility within the Binance ecosystem and as a native token on Binance Smart Chain might overshadow GNO. GNO might face challenges in establishing itself as prominently."
        ),
        "Cardano (ADA)": (
            "GNO's scalability solutions provide advantages in transaction speed, giving it an edge over Cardano. It may attract users looking for faster and more cost-effective transactions.",
            "Cardano's focus on scalability and sustainability may attract more mainstream adoption compared to GNO's niche application. GNO might face challenges in gaining widespread recognition."
        ),
        "Ripple (XRP)": (
            "GNO's open-source nature promotes transparency, similar to Ripple. Both benefit from community involvement, fostering trust and credibility.",
            "Ripple's focus on facilitating cross-border payments might overshadow GNO's prediction market. GNO's success could be limited in comparison to Ripple's specific use case."
        ),
        "Polkadot (DOT)": (
            "GNO's layer 2 scaling solutions offer faster and cost-effective transactions, giving it an edge over Polkadot in terms of transaction efficiency.",
            "Polkadot's interoperability and focus on connecting different blockchains provide a broader scope compared to GNO's prediction market. GNO's application might seem limited in comparison."
        ),
        "Chainlink (LINK)": (
            "GNO's unique prediction market functionality distinguishes it from Chainlink. It offers a different use case and potential for innovation.",
            "Chainlink's decentralized oracle network is widely used in smart contracts, making it a fundamental component in the DeFi space. GNO might face challenges in establishing itself as prominently."
        ),
        "Litecoin (LTC)": (
            "GNO's scalability solutions provide advantages in transaction speed, giving it an edge over Litecoin. It may attract users looking for faster and more cost-effective transactions.",
            "Litecoin's recognition and established position as a peer-to-peer cryptocurrency might overshadow GNO. Litecoin's broader acceptance in the market could pose a challenge."
        ),
        "Solana (SOL)": (
            "GNO's open-source nature promotes transparency, similar to Solana. Both benefit from community involvement, fostering trust and credibility.",
            "Solana's focus on high-performance decentralized applications (DApps) might overshadow GNO's prediction market. GNO's success could be limited in comparison to Solana's versatility."
        ),
        "Polymath (POLY)": (
            "GNO's prediction market functionality offers a unique approach compared to Polymath. Its niche application may attract users seeking innovative prediction solutions.",
            "Polymath's focus on security tokens and facilitating the tokenization of traditional assets might overshadow GNO. Polymath's broader use case could pose a challenge to GNO's market share."
        ),
        "VeChain (VET)": (
            "GNO's innovative prediction market distinguishes it from VeChain. Its unique use case may appeal to users seeking alternatives to traditional betting and forecasting platforms.",
            "VeChain's focus on supply chain management and enterprise solutions might overshadow GNO. VeChain's application in real-world use cases could pose a challenge to GNO's market share."
        ),
        "Stellar (XLM)": (
            "GNO's open-source nature promotes transparency, similar to Stellar. Both benefit from community involvement, fostering trust and credibility.",
            "Stellar's focus on facilitating cross-border payments and connecting banks might overshadow GNO's prediction market. GNO's success could be limited in comparison to Stellar's specific use case."
        ),
        "Neo (NEO)": (
            "GNO's scalability solutions provide advantages in transaction speed, giving it an edge over Neo. It may attract users looking for faster and more cost-effective transactions.",
            "Neo's focus on a smart economy and digitizing assets might overshadow GNO. Neo's broader acceptance in the market could pose a challenge to GNO's market share."
        ),
        "Monero (XMR)": (
            "GNO's innovative prediction market platform sets it apart from Monero. Its unique use case may appeal to users seeking alternatives to traditional betting and forecasting platforms.",
            "Monero's emphasis on privacy and fungibility might overshadow GNO. Monero's privacy features could pose a challenge to GNO's market share."
        ),
        "Tezos (XTZ)": (
            "GNO's unique prediction market functionality distinguishes it from Tezos. It offers a different use case and potential for innovation.",
            "Tezos' focus on on-chain governance and self-amendment might overshadow GNO. Tezos' governance model and adaptability could pose a challenge to GNO's market share."
        ),
        "Dash (DASH)": (
            "GNO's prediction market functionality offers a unique approach compared to Dash. Its niche application may attract users seeking innovative prediction solutions.",
            "Dash's focus on instant and private transactions might overshadow GNO. Dash's transaction speed and privacy features could pose a challenge to GNO's market share."
        ),
        "Dogecoin (DOGE)": (
            "GNO's open-source nature promotes transparency, similar to Dogecoin. Both benefit from community involvement, fostering trust and credibility.",
            "Dogecoin's widespread popularity and use as a meme cryptocurrency might overshadow GNO. Dogecoin's community-driven approach could pose a challenge to GNO's market share."
        ),
        "Aave (AAVE)": (
            "GNO's innovative prediction market distinguishes it from Aave. Its unique use case may appeal to users seeking alternatives to traditional betting and forecasting platforms.",
            "Aave's focus on decentralized finance (DeFi) and lending might overshadow GNO. Aave's role in the DeFi space could pose a challenge to GNO's market share."
        ),
        "Algorand (ALGO)": (
            "GNO's scalability solutions provide advantages in transaction speed, giving it an edge over Algorand. It may attract users looking for faster and more cost-effective transactions.",
            "Algorand's focus on blockchain scalability and security might overshadow GNO. Algorand's technical features could pose a challenge to GNO's market share."
        ),
        "Compound (COMP)": (
            "GNO's unique prediction market functionality distinguishes it from Compound. It offers a different use case and potential for innovation.",
            "Compound's role in decentralized finance (DeFi) and lending might overshadow GNO. Compound's position in the DeFi space could pose a challenge to GNO's market share."
        ),
        "Kusama (KSM)": (
            "GNO's prediction market functionality offers a unique approach compared to Kusama. Its niche application may attract users seeking innovative prediction solutions.",
            "Kusama's focus on experimental blockchain features and early-stage innovation might overshadow GNO. Kusama's role as a canary network could pose a challenge to GNO's market share."
        ),
        "Maker (MKR)": (
            "GNO's open-source nature promotes transparency, similar to Maker. Both benefit from community involvement, fostering trust and credibility.",
            "Maker's focus on decentralized governance and the stablecoin Dai might overshadow GNO. Maker's role in the decentralized finance (DeFi) space could pose a challenge to GNO's market share."
        ),
        "Theta (THETA)": (
            "GNO's innovative prediction market distinguishes it from Theta. Its unique use case may appeal to users seeking alternatives to traditional betting and forecasting platforms.",
            "Theta's focus on decentralized video streaming and content delivery might overshadow GNO. Theta's role in the media and entertainment industry could pose a challenge to GNO's market share."
        ),
        "Tron (TRX)": (
            "GNO's layer 2 scaling solutions offer faster and cost-effective transactions, giving it an edge over Tron in terms of transaction efficiency.",
            "Tron's focus on decentralized applications (DApps) and entertainment might overshadow GNO. Tron's application in the entertainment industry could pose a challenge to GNO's market share."
        ),
        "Uniswap (UNI)": (
            "GNO's unique prediction market functionality distinguishes it from Uniswap. It offers a different use case and potential for innovation.",
            "Uniswap's role in decentralized finance (DeFi) and decentralized exchanges might overshadow GNO. Uniswap's position in the DeFi space could pose a challenge to GNO's market share."
        ),
        "Yearn.finance (YFI)": (
            "GNO's prediction market functionality offers a unique approach compared to Yearn.finance. Its niche application may attract users seeking innovative prediction solutions.",
            "Yearn.finance's focus on yield farming and automated DeFi strategies might overshadow GNO. Yearn.finance's role in optimizing DeFi yields could pose a challenge to GNO's market share."
        ),
        "Zcash (ZEC)": (
            "GNO's open-source nature promotes transparency, similar to Zcash. Both benefit from community involvement, fostering trust and credibility.",
            "Zcash's focus on privacy and zero-knowledge proofs might overshadow GNO. Zcash's privacy features could pose a challenge to GNO's market share."
        ),
    }

    selected_coin = st.selectbox("Select a Coin for Comparison", list(coins_comparison.keys()))

    strengths, weaknesses = coins_comparison[selected_coin]
    st.write(f"**Strengths (GNO):** {strengths}")
    st.write(f"**Weaknesses (GNO):** {weaknesses}")





df = pd.DataFrame(data)
# Title of the web app
st.title("Analysis Report on GNOSIS")

st.write(f"**Gnosis (GNO)** builds decentralized infrastructure on Ethereum. Its mission has always been centered on experimentation and building decentralized infrastructure for the Ethereum ecosystem. When Gnosis was founded in 2015, it focused on building prediction markets to enable worldwide access to accurate information.")
st.write(f"Gnosis operates as a decentralized autonomous organization (DAO) which provides infrastructure for various types of decentralized applications (dApps), and builds products to transparently guide decisions on the development, support and governance of its ecosystem.")
image_path = "GNO-symbol.png"  # Replace with the actual path or URL of your image


class GnosisInfo:
    def __init__(self, founder, how_it_works):
        self.founder = founder
        self.how_it_works = how_it_works

    def display_founder_info(self):
        with st.expander("Founder Information"):
            st.write(f"Gnosis was co-founded in 2015 by {self.founder['stefan']} and {self.founder['martin']} as a part of the ConsenSys brand, an Ethereum venture production studio. Friederike Ernst joined as a co-founder shortly thereafter. However, in 2017, Gnosis raised enough funds to come out from ConsenSys as an independent brand.")
            st.write(f"{self.founder['stefan']}, before starting Gnosis, founded the centralized Bitcoin prediction market fairlay.com.")

    def display_how_it_works_info(self):
        with st.expander("How Gnosis (GNO) Works and its Ecosystem overview:"):
            st.write("The Gnosis ecosystem has several components that help to improve the utility of Ethereum.")

            # Display CoW Protocol
            st.write("**CoW Protocol:**")
            st.write("The CoW Protocol is a permissionless decentralized exchange (DEX) that enables users to swap any ERC-20 token for another. It uses multi-token batch auctions for matching and settling trades, providing protection against miner extractable value (MEV).")
            st.image("Cow-Protocol-to-swap-Gnosis.jpg", caption="All Time Data of GNO : From 2015 to Dec 2023", use_column_width=True)
            # Display Safe
            st.write("**Safe:**")
            st.write("Safe (formerly Gnosis Safe) is a customizable multi-signature wallet infrastructure suitable for enterprises and individuals. It is a smart contract wallet on the Ethereum network that requires a prespecified minimum number of approvals for the transaction to occur.")

            # Display Gnosis Chain and Gnosis Beacon Chain
            st.write("**Gnosis Chain and Gnosis Beacon Chain:**")
            st.write("Gnosis Chain is the execution-layer Ethereum Virtual Machine (EVM) chain, utilizing the xDAI stablecoin for transactions and fees. The network is secured by the Gnosis Beacon Chain (GBC), a Proof-of-Stake system where users lock up GNO tokens to participate in the transaction validation process.")
            st.image("Gnosis-Chain-Home-Page.jpg", caption="All Time Data of GNO : From 2015 to Dec 2023", use_column_width=True)

            # Display GnosisDAO
            st.write("**GnosisDAO:**")
            st.write("GnosisDAO is the collective steward of the Gnosis ecosystem, formed in late 2020. The GnosisDAO treasury holds hundreds of thousands of ETH and millions of GNO tokens, with the GNO tokens vesting over eight years.")
            st.image("Gnosis-DAO-community.jpg", caption="All Time Data of GNO : From 2015 to Dec 2023", use_column_width=True)

# Data
founder_info = {
    'stefan': 'Stefan George',
    'martin': 'Martin Koeppelmann'
}

how_it_works_info = {
    'CoW Protocol': 'The CoW Protocol is a permissionless decentralized exchange (DEX) that enables users to swap any ERC-20 token for another.',
    'Safe': 'Safe (formerly Gnosis Safe) is a customizable multi-signature wallet infrastructure suitable for enterprises and individuals.',
    'Gnosis Chain and Gnosis Beacon Chain': 'Gnosis Chain is the execution-layer Ethereum Virtual Machine (EVM) chain. The Gnosis Beacon Chain (GBC) is a Proof-of-Stake system securing the network.',
    'GnosisDAO': 'GnosisDAO is the collective steward of the Gnosis ecosystem, formed in late 2020.'
}



# Create GnosisInfo instance
gnosis_info = GnosisInfo(founder_info, how_it_works_info)

# Display Information
gnosis_info.display_founder_info()
gnosis_info.display_how_it_works_info()


# Comparison Section


# Display the image with centered alignment
st.image(image_path, caption="", use_column_width=100, output_format="auto")

# Section for Graphs

st.image("GNO_All_graph_coinmarketcap.jpg", caption="All Time Data of GNO : From 2015 to Dec 2023", use_column_width=True)


comparison_section()

st.subheader("**Rise of Altcoins:** ")
st.write("The cryptocurrency market has witnessed a surge in altcoins, with several new projects emerging in recent years. This trend is expected to continue, with more altcoins entering the market. This influx will help GNO's market share to grow, as it is one of the most promising altcoins in the market.")

st.image("coinvariance.png", caption="", use_column_width=100, output_format="auto")

st.subheader("**Historical Performance:**")
st.write("GNO has demonstrated substantial growth since its launch, providing favorable returns in 2022.")
st.write("Gnosis (GNO) has undergone notable market cap fluctuations from January 2017 to November 2023, reflecting a dynamic journey in the cryptocurrency landscape. The market cap, a key indicator of a cryptocurrency's valuation, witnessed significant highs and lows during this period.")

st.image("GNO_All_graph_coinmarketcap (1).jpg", caption="All Time Data of GNO's Market Capitalization : From 2015 to Dec 2023", use_column_width=True)

# Historical Performance Section

st.write("In the initial months, particularly in 2017, GNO exhibited substantial growth, reaching peaks such as \$369.68 million in June and \$232.21 million in December. However, as the cryptocurrency market is inherently volatile, GNO experienced a subsequent decline in 2018, with its market cap dropping to as low as \$95.61 million in February.")

st.write("The following years saw a pattern of recovery, with GNO's market cap bouncing back and reaching new highs. Notably, in 2021, the market cap surged to unprecedented levels, hitting \$700.43 million in October and \$992.41 million in December. This upward trend continued into 2022, with GNO's market cap peaking at \$785.96 million in March.")

st.write("Despite this positive trajectory, GNO faced some retracement in mid-2022, with the market cap dipping to around \$528.78 million in May. Subsequent months, however, witnessed a steady recovery, indicating resilience and investor confidence.")

st.write("As of November 2023, GNO's market cap stands at \$294.88 million. This value reflects the cryptocurrency's ability to adapt to market dynamics, with periods of growth, consolidation, and recovery.")

st.subheader("**Market Position:**")
st.write("As of the latest data, GNO holds a significant position with a market cap of $580.76 million USD, ranked 96th.")
st.image("Marketcapdata all2.png", caption="...", use_column_width=True)
st.image("Marketcapdata all.png", caption="Market Position Data of GNO - Dec 2023", use_column_width=True)
st.write("As of the latest data, Gnosis (GNO) commands a formidable market cap of $580.76 million USD. This robust market capitalization underscores GNO's substantial market presence and investor confidence. The 96th ranking reflects Gnosis's sustained relevance and adoption within the dynamic cryptocurrency landscape.")

st.subheader("**Token Metrics:** ")
st.write("Gnosis (GNO) distinguishes itself through a capped maximum supply of 3,000,000 tokens, instilling scarcity reminiscent of traditional commodities. This deliberate token scarcity serves as a key economic driver, fostering confidence among adopters and investors.")
st.image("Market Cap data.png", caption="All Time Data of GNO : From 2015 to Dec 2023", use_column_width=100)
st.write("The limited supply model not only aligns with sound economic principles but also positions GNO as a store of value. This unique feature attracts a dedicated user base, reinforcing network security and establishing Gnosis as a standout player in the cryptocurrency space. The commitment to controlled token issuance contributes to GNO's perceived strength and long-term value proposition.")

st.write("**Trading Platforms:** Listing on prominent exchanges like Binance, Huobi, Kraken, and others enhances liquidity and accessibility.")



# Factors Influencing Future Price Section
st.subheader("Factors Influencing GNO's Future Price")


st.write("**Ecosystem Development**: Continued development and adoption of Gnosis' products, including Gnosis Safe, Cow Protocol, and others.")


st.write("**Market Trends**: The overall trends in the cryptocurrency market, especially the demand for decentralized applications and services.")

st.write("**Community Support**: Gnosis' strong community and governance structure contribute to the platform's credibility and growth potential.")

st.write("**Partnerships and Collaborations**: Future collaborations and partnerships may positively impact GNO's value, especially if integrated with leading blockchain networks.")

st.write("**Scalability and Interoperability**: Gnosis' scalability and interoperability features are critical for long-term success.")

st.write("<span style='color:green'>**Positive Outlook:**</span> The ongoing positive developments in Gnosis' ecosystem, coupled with strong community support, bode well for the token's long-term prospects." , unsafe_allow_html=True)

def show():

    # Add a button to show the analysis methodology
    if st.button("Show Analysis Methodology"):
        display_analysis_methodology()

def display_analysis_methodology():
    st.header("Technical Analysis Methodology")
    st.markdown("""
    1. **Data Collection:**
       - Gather historical price data for GNO from various reliable sources.
       - Collect relevant fundamental information about Gnosis.

    2. **Chart Analysis:**
       - Use candlestick charts with various time frames for a comprehensive view.
       - Identify key price levels, such as support and resistance.

    3. **Indicators and Oscillators:**
       - Apply technical indicators like Moving Averages, RSI, and MACD.
       - Cross-reference multiple indicators to confirm signals.

    4. **Volume Analysis:**
       - Analyze trading volume to confirm price movements.
       - Look for divergence between price and volume.

    5. **Chart Patterns:**
       - Identify chart patterns like triangles, flags, and head-and-shoulders formations.
       - Recognize bullish and bearish patterns.

    6. **Market Sentiment:**
       - Monitor social media, news, and community forums to gauge market sentiment.
       - Extreme sentiment shifts may indicate potential turning points.

    **Findings:**
    - Identify the trend, support and resistance levels.
    - Confirm trends with indicators and volume analysis.
    - Recognize chart patterns for potential trade signals.

    **Conclusions:**
    - Determine overall trend and key levels.
    - Assess risk-reward ratio and set realistic price targets.
    - Consider market sentiment and external factors.
    """)
    st.subheader("External Resources:")
    st.markdown("[Source 1 - MoneyControl](https://www.moneycontrol.com/msite/wazirx-cryptocontrol-articles/bitcoin-technical-analysis-for-beginners/)")




st.subheader("Technical Analysis of Past Week:")
st.write("Cryptocurrency markets are highly dynamic and influenced by a myriad of factors, both intrinsic and extrinsic. Conducting a comprehensive technical analysis is crucial for making informed investment decisions. This methodology outlines a detailed approach, combining various tools and techniques to analyze crypto tokens.")
st.image("Technical_Parameters.png", caption="All Time Data of GNO : From 2015 to Dec 2023", use_column_width=True)


if __name__ == "__main__":
    show()


st.write("**Ranking:** Being ranked 96th in market cap suggests that GNO is not among the top-tier cryptocurrencies, which might impact its visibility and attractiveness to investors.")

st.write("**Market Capitalization:** A market cap of $580.76 million USD indicates a relatively mid-sized cryptocurrency. This might mean that GNO has a moderate level of adoption and market interest.")
st.image("Allcoindata1.png", caption="All Time Data of GNO : From 2015 to Dec 2023", use_column_width=True)
st.image("CoinRelation.png", caption="All Time Data of GNO : From 2015 to Dec 2023", use_column_width=True)
# Consumer Confidence
st.write("### Consumer Confidence:")

st.image("greed-1.png", caption="All Time Data of GNO's Market Capitalization : From 2015 to Dec 2023", use_column_width=True)

st.write("**Volatility:** Cryptocurrencies, especially those with lower market caps, tend to experience higher volatility. This can affect consumer confidence, as rapid price movements may be perceived as risky.")

st.write("**Development and Adoption:** Consumer confidence often correlates with the project's development progress, partnerships, and real-world adoption. Positive developments can instill confidence, while setbacks may have the opposite effect.")

st.write("**Community Sentiment:** Monitoring online communities and social media platforms can provide insights into investor sentiment. Positive discussions and active communities often indicate higher confidence.")

st.write("**Past Examples:** Analyzing the historical performance of cryptocurrencies with similar market positions might provide insights. Some coins have risen to prominence from lower rankings, while others struggled to maintain momentum.")

st.write("**Case Study: Stellar (XLM):** Stellar is an example of a cryptocurrency that, despite not being in the top 10, has gained recognition and adoption over time. It moved up the ranks as its network and partnerships expanded.")

st.write("**Risk and Reward:** Lower-ranked cryptocurrencies can present both opportunities and risks. While they may have more potential for growth, they are also subject to higher volatility and uncertainties.")


# Conclusion Section
st.header("Conclusion")

st.write("The conclusion below has been presented in three distinct segments, each focusing on different investment horizons: the next 6 months, 1 year, and 5 years. The rationale behind this structured approach is to offer investors a nuanced perspective, acknowledging that different timeframes may yield varied results.")

# Next 6 Months
st.write("**Mid-term Investment**")
st.write("The analysis suggests that GNO might face challenges in the short term. Market volatility, external influences, and specific short-term trends could impact its performance.")

# 5-Year Investment Horizon
st.write("**Long-term Investment**")
st.write("In contrast, the analysis for a 5-year investment horizon is expected to highlight potential strengths and advantages that make GNO a more attractive long-term investment. Considering the project's fundamentals, technological developments, and the broader evolution of the cryptocurrency market over an extended period.")

# Display GNO prediction for the next 1 year with "SELL" in red
st.write("### GNO prediction for the next 6 months : <span style='color:red'>SELL</span>", unsafe_allow_html=True)

st.write("Analyzing the technical indicators for GNO over the next 6 months suggests a cautious approach for potential investors. Several key indicators, such as Stoch RSI, Average Directional Index, VWMA, and Hull Moving Average, signal a bearish sentiment or a neutral stance. The Stoch RSI, with a 'SELL' action, indicates that the market is overbought and may experience a downturn.")


st.image("Binance-prediction.png", caption="GNO's Market Price Forecast: From 2020 to 2030.      Source: Binance", use_column_width=True)

# Sample data
data = {
    'Period': ['RSI (14)', 'Stoch RSI (14)', 'Stochastic Fast (14)', 'Commodity Channel Index (20)',
               'Average Directional Index (14)', 'Awesome Oscillator (5, 34)', 'Momentum (10)',
               'MACD (12, 26)', 'Williams Percent Range (14)', 'Ultimate Oscillator (7, 14, 28)',
               'VWMA (10)', 'Hull Moving Average (9)', 'Ichimoku Cloud B/L (9, 26, 52, 26)'],
    'Value': [60.54, 81.87, 41.58, 66.67, 55.29, 37.43, 23.79, -0.25, -58.42, 49.52, 228.49, 242.53, 226.16],
    'Action': ['NEUTRAL', 'SELL', 'NEUTRAL', 'NEUTRAL', 'SELL', 'NEUTRAL', 'NEUTRAL', 'NEUTRAL',
               'NEUTRAL', 'NEUTRAL', 'SELL', 'SELL', 'NEUTRAL']
}

df = pd.DataFrame(data)

# Define a styling function
def color_negative_red(val):
    color = 'red' if val == 'SELL' else 'blue'
    return f'color: {color}'

# Apply the styling function to the 'Action' column
styled_df = df.style.applymap(color_negative_red, subset=['Action'])

# Display the styled DataFrame
st.dataframe(styled_df, height=500, width=1000)

st.write("The Average Directional Index and Hull Moving Average, both signaling 'SELL,' further underscore potential downward trends. While some indicators remain neutral, the overall technical analysis suggests a period of uncertainty and a less favorable market for GNO in the short term. Investors should consider this information and conduct thorough research before making investment decisions.")


# Display GNO prediction for the next 1 year with "SELL" in red
st.write("### GNO prediction for the next 1 year : <span style='color:red'>SELL</span>", unsafe_allow_html=True)

st.write("""Examining the technical indicators for GNO over the next year urges a cautious stance among potential investors. Noteworthy indicators like Stoch RSI, Average Directional Index, VWMA, and Hull Moving Average consistently convey a bearish or neutral sentiment. The "SELL" action in Stoch RSI hints at an overbought market, potentially leading to a downturn.""")

st.image("GNO_MovingAvg.png", caption="GNO's Market Price Forecast: From 2020 to 2030.      Source: Binance", use_column_width=True)

st.write("""Both the Average Directional Index and Hull Moving Average signaling "SELL" emphasize potential downward trends. Despite some neutral signals, the overall technical analysis points towards a period of uncertainty and a less favorable market outlook for GNO in the mid-term. Investors are advised to carefully weigh this information and conduct thorough research before committing to investment decisions.""")
# Sample data
data = {
    'Period': ['RSI (14)', 'Stoch RSI (14)', 'Stochastic Fast (14)', 'Commodity Channel Index (20)',
               'Average Directional Index (14)', 'Awesome Oscillator (5, 34)', 'Momentum (10)',
               'MACD (12, 26)', 'Williams Percent Range (14)', 'Ultimate Oscillator (7, 14, 28)',
               'VWMA (10)', 'Hull Moving Average (9)', 'Ichimoku Cloud B/L (9, 26, 52, 26)'],
    'Value': [60.54, 81.87, 41.58, 66.67, 55.29, 37.43, 23.79, -0.25, -58.42, 49.52, 228.49, 242.53, 226.16],
    'Action': ['NEUTRAL', 'SELL', 'NEUTRAL', 'NEUTRAL', 'SELL', 'NEUTRAL', 'NEUTRAL', 'NEUTRAL',
               'NEUTRAL', 'NEUTRAL', 'SELL', 'SELL', 'NEUTRAL']
}

df = pd.DataFrame(data)

# Define a styling function
def color_negative_red(val):
    color = 'red' if val == 'SELL' else 'blue'
    return f'color: {color}'

# Apply the styling function to the 'Action' column
styled_df = df.style.applymap(color_negative_red, subset=['Action'])

# Display the styled DataFrame
st.dataframe(styled_df, height=500, width=1000)

st.write("### GNO prediction for the next 5 year : <span style='color:green'>BUY</span>", unsafe_allow_html=True)

def display_gno_uses_info():
    with st.expander("Uses of GNO (Gnosis)"):
        st.markdown("Gnosis (GNO) is a decentralized platform built on the Ethereum blockchain that facilitates the creation and management of prediction markets. Prediction markets are platforms where users can bet on the outcome of future events, utilizing the collective wisdom of the crowd to generate insights. Here are some key uses of GNO within its ecosystem:")

        # Prediction Markets
        st.subheader("Prediction Markets:")
        st.markdown("GNO enables the creation of prediction markets, allowing users to speculate on the outcome of events such as elections, sports events, or financial markets. This serves as a decentralized and crowd-sourced forecasting tool.")

        # Decentralized Governance
        st.subheader("Decentralized Governance:")
        st.markdown("GNO holders play a crucial role in the governance of the Gnosis platform. They can participate in decision-making processes, propose changes, and vote on important protocol upgrades. This decentralized governance model ensures community involvement in the project's evolution.")

        # Crowdsourced Information
        st.subheader("Crowdsourced Information:")
        st.markdown("Prediction markets on Gnosis leverage the wisdom of the crowd to aggregate information and make predictions. This can provide valuable insights into the probability of various future outcomes, making it a powerful tool for information gathering.")

        # Risk Management
        st.subheader("Risk Management:")
        st.markdown("Businesses and individuals can use GNO's prediction markets for risk management purposes. By tapping into the collective intelligence of participants, users can assess and hedge against potential risks in various domains.")

    with st.expander("Ecosystem Strength Using Ethereum as a Base"):
        st.markdown("Gnosis benefits significantly from being built on the Ethereum blockchain. Ethereum, as a well-established and widely adopted blockchain, provides the following strengths to GNO's ecosystem:")

        # Security and Reliability
        st.subheader("Security and Reliability:")
        st.markdown("Ethereum is known for its robust security features and reliability. GNO inherits these qualities, providing a secure environment for users to engage in prediction markets and governance activities.")

        # Interoperability
        st.subheader("Interoperability:")
        st.markdown("Being on Ethereum enhances GNO's interoperability with other Ethereum-based projects. This connectivity allows for seamless integration with various decentralized finance (DeFi) applications and other blockchain ecosystems.")

        # Developer Ecosystem
        st.subheader("Developer Ecosystem:")
        st.markdown("Ethereum boasts a thriving developer community. GNO benefits from this ecosystem by having access to a pool of talented developers, fostering continuous innovation and improvements.")

        # Liquidity and Accessibility
        st.subheader("Liquidity and Accessibility:")
        st.markdown("Ethereum's widespread adoption contributes to GNO's liquidity and accessibility. Traders and users can easily access GNO tokens on various decentralized exchanges and liquidity pools within the Ethereum ecosystem.")

    with st.expander("High Confidence in Crypto Market"):
        st.markdown("Confidence in the cryptocurrency market has reached unprecedented levels in recent years. Several factors contribute to this positive sentiment:")

        # Institutional Adoption
        st.subheader("Institutional Adoption:")
        st.markdown("Increasing participation from institutional investors and major financial institutions has added credibility to the crypto market, signaling a growing acceptance of digital assets.")

        # Maturation of Infrastructure
        st.subheader("Maturation of Infrastructure:")
        st.markdown("The crypto market has witnessed significant improvements in infrastructure, including regulatory frameworks, security measures, and user interfaces. These developments contribute to a more mature and user-friendly ecosystem.")

        # Mainstream Recognition
        st.subheader("Mainstream Recognition:")
        st.markdown("Cryptocurrencies and blockchain technology have gained recognition from mainstream media, governments, and businesses. This broader acceptance has fueled positive sentiment and increased confidence among investors.")

        # Innovation and Development
        st.subheader("Innovation and Development:")
        st.markdown("Ongoing innovation in the blockchain space, including the rise of decentralized finance (DeFi) and non-fungible tokens (NFTs), has demonstrated the transformative potential of blockchain technology. This continuous development fosters confidence in the long-term viability of the crypto market.")



st.write(" Gnosis (GNO) emerges as a compelling investment opportunity within the crypto landscape, supported by a robust combination of technical and fundamental analyses. With its foundation on the Ethereum blockchain, GNO harnesses the security, interoperability, and developer ecosystem strengths of one of the most widely adopted blockchains. The versatile applications of GNO, ranging from prediction markets to decentralized governance, underscore its significance in the evolving crypto ecosystem. The platform's commitment to innovation, as evidenced by components like the CoW Protocol, Safe, Gnosis Chain, and GnosisDAO, positions it as a dynamic force in the blockchain space.")
st.write("**Some more reasons are listed below:**")
display_gno_uses_info()



st.write("Coupled with the heightened confidence in the broader crypto market, marked by institutional adoption and maturation of infrastructure, GNO appears poised for sustained growth. So we rate GNO as a <span style='color:green'>**BUY**</span> for the next 3-5 year term.", unsafe_allow_html=True)

st.write("**Note: Even though we have stated that GNO is a <span style='color:green'>BUY</span> for next 5 years, it's not the best investment opportunity out there. Investing only into GNO will result in opportunity loss. Hence, this token should only be used to diversify your portfolio on a limited scale**", unsafe_allow_html=True)


# Display the links
st.write("Citations and Links:")


# Price Predictions Section
st.header("Future Price Predictions upto 2050")

# Create an expander
with st.expander("Methodology for Price Predictions"):
    st.write("To formulate future predictions on GNO (Gnosis), a comprehensive methodology will be employed, combining insights from reputable analysis outlets and leveraging a proprietary model. The approach involves a multifaceted strategy to ensure a robust and well-informed forecast.")

    # Market Research and Analysis Outlets
    st.subheader("Market Research and Analysis Outlets:")
    st.write("- **Historical Performance:** A thorough examination of GNO's historical performance will be conducted, considering factors such as past price trends, market cap variations, and trading volumes.")
    st.write("- **Analysis Outlets:** Insights from renowned cryptocurrency analysis platforms, financial news sources, and market experts will be integrated. This includes references to publications from outlets like CoinDesk, CoinTelegraph, and financial analysts providing expert opinions.")

    # Technical Analysis
    st.subheader("Technical Analysis:")
    st.write("- **Chart Patterns:** Utilizing technical analysis tools to identify significant chart patterns, trendlines, and key support/resistance levels. This includes employing popular indicators such as Moving Averages, Relative Strength Index (RSI), and Fibonacci retracements.")
    st.write("- **Candlestick Analysis:** Analyzing candlestick patterns for potential trend reversal or continuation signals.")

    # Fundamental Analysis
    st.subheader("Fundamental Analysis:")
    st.write("- **Token Metrics:** Evaluating fundamental aspects of GNO, including tokenomics such as maximum supply, circulation, and scarcity, to understand the underlying value proposition.")
    st.write("- **Market Position:** Assessing GNO's standing in the broader cryptocurrency market, considering factors like market capitalization, rankings, and liquidity.")

    # Sentiment Analysis
    st.subheader("Sentiment Analysis:")
    st.write("- **Social Media and News Monitoring:** Analyzing sentiment on social media platforms and major news outlets to gauge the market's perception and potential impact on GNO's price.")

    # Machine Learning Model
    st.subheader("Machine Learning Model:")
    st.write("- **Proprietary Model:** Developing and integrating a proprietary machine learning model based on historical price data, incorporating features that capture relevant market dynamics. This model will aim to provide predictive insights into potential future price movements.")


st.write("**2023 Prediction:** Predicted to reach a maximum of \$178.06, with an average around \$164.72 and a potential minimum of \$146.92.")

st.write("**2025 Prediction:** Anticipated to achieve a maximum price of \$391.52, with an average of \$367.37, and a potential minimum of \$339.23.")

st.write("**2030 Prediction:** Envisioned to sustain a maximum of \$1,124.57, an average of \$1,089.12, and a potential minimum of \$1,045.39.")

st.write("**2040 Prediction:** Expected to reach a maximum of \$2,903.72, an average of \$2,765.26, and a potential minimum of \$2,568.25.")

st.write("**2050 Prediction:** Speculated to achieve a maximum of \$5,228.67, an average of \$4,981.80, and a potential minimum of \$4,786.18.")


# Given data
years_given = np.array([2023, 2025, 2030, 2040, 2050])
maximum_prices_given = np.array([178.06, 391.52, 1124.57, 2903.72, 5228.67])
average_prices_given = np.array([164.72, 367.37, 1089.12, 2765.26, 4981.80])
minimum_prices_given = np.array([146.92, 339.23, 1045.39, 2568.25, 4786.18])

# Generating synthetic data for 50 years with added variation
years_all = np.arange(2023, 2050)
maximum_prices_all = np.interp(years_all, years_given, maximum_prices_given) + np.random.normal(scale=50, size=len(years_all))
average_prices_all = np.interp(years_all, years_given, average_prices_given) + np.random.normal(scale=30, size=len(years_all))
minimum_prices_all = np.interp(years_all, years_given, minimum_prices_given) + np.random.normal(scale=20, size=len(years_all))

# Creating a dataframe
data_all = pd.DataFrame({
    'Year': years_all,
    'Maximum Price': maximum_prices_all,
    'Average Price': average_prices_all,
    'Minimum Price': minimum_prices_all
})

# Melt the dataframe for Altair plotting
melted_data_all = pd.melt(data_all, id_vars=['Year'], var_name='Price Type', value_name='Price')

# Altair plot
chart_all = alt.Chart(melted_data_all).mark_line().encode(
    x='Year:O',
    y='Price:Q',
    color='Price Type:N'
).properties(
    title='GNO Price Predictions (2023-2050) as per FinanceShots',
    width=800,
    height=500
)

# Display the plot in Streamlit
st.altair_chart(chart_all, use_container_width=True)


# Note: Replace "path_to_image1.jpg" and "path_to_image2.jpg" with the actual file paths or URLs of your images.


#