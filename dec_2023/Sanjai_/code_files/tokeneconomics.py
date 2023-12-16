import streamlit  as st
import pandas as pd
import matplotlib.pyplot as plt

def token_distribution_analysis():
    st.title("Livepeer Token Distribution: A Comprehensive Overview")

    distribution_description = """
    Livepeer's token distribution plays a pivotal role in shaping the project's trajectory. Understanding how tokens are allocated provides valuable insights into the project's governance, sustainability, and commitment to decentralization.

    **Founders and Early Team (12.35%):**
    - Vesting over 36 months from network launch.
    - Demonstrates a commitment to long-term alignment, with gradual token release to founders and early team members.

    **Pre-sale Purchasers (19%):**
    - Vesting over 18 months from network launch.
    - Purchasers contribute to Livepeer's financial runway, supporting the lean, engineering-focused core team.

    **Crowd (63.437%):**
    - Generated over 3–18 months using the MerkleMine algorithm.
    - Emphasizes a decentralized distribution model, involving the community in the early stages of the project.

    **Grant (0.213%):**
    - Immediately issued to a couple of early advisors and contributors.
    - Acknowledges the contributions of key individuals who played a crucial role in Livepeer's early stages.

    **Long-term Project Endowment (5%):**
    - Reserved for ensuring the longevity of the Livepeer project.
    - Reflects a strategic allocation aimed at securing resources for sustained development and growth.

    **Implications**
    - **Alignment with Contributors:** Vesting schedules for founders, early team, and pre-sale purchasers align incentives, promoting 
      commitment to project success.
    - **Community Engagement:** The MerkleMine algorithm promotes community engagement, involving the crowd in the initial token 
      generation.

    """

    st.write(distribution_description)

def display_market_info(market_cap, trading_vol, fully_diluted_valuation, circulating_supply, total_supply, max_supply):
    st.title("Token Market Information")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Market Cap")
        st.write(f"${market_cap:,}")

        st.subheader("24 Hour Trading Volume")
        st.write(f"${trading_vol:,}")

        st.subheader("Fully Diluted Valuation")
        st.write(f"${fully_diluted_valuation:,}")

    with col2:
        st.subheader("Circulating Supply")
        st.write(f"{circulating_supply:,} Tokens")

        st.subheader("Total Supply")
        st.write(f"{total_supply:,} Tokens")

        st.subheader("Max Supply")
        st.write(f"{max_supply:,} Tokens")


def plot_pie_chart(path):
    df = pd.read_csv(path)

    fig, ax = plt.subplots()
    ax.pie(df['Volume'], labels=df['Category'], autopct='%1.1f%%', startangle=90, colors=['#66b3ff', '#99ff99', '#ffcc99'])
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Display the pie chart using Streamlit
    st.pyplot(fig)


def token_economics_analysis():
    st.title("Token Economics Analysis:")

    market_cap = 188609465
    trading_vol = 31821041
    fully_diluted_valuation = 188609465
    circulating_supply = 30013177
    total_supply = 30013177
    max_supply = 30013177


    display_market_info(market_cap, trading_vol, fully_diluted_valuation, circulating_supply, total_supply,
                        max_supply)

    token_distribution_analysis()
    plot_pie_chart("code_files/Data/LPT-concentration.csv")

    st.image('assets/token-distribution.png')

    st.title("Token Market Analysis")

    analysis_description = """
    **Market Cap and Rank:**
    The market capitalization of Livepeer (LPT) stands at $185,338,625, positioning it at rank 205. Market cap is a key metric 
    reflecting the total value of all circulating tokens. A higher rank signifies a relatively larger market presence.

    **24-Hour Volume:**
    A robust 24-hour trading volume of $54,964,693 indicates active market participation. Higher trading volumes suggest increased 
    liquidity, enhancing the ease of buying and selling.

    **Circulating and Total Supply:**
    With a circulating supply of 30,024,231 tokens and a total supply matching that number, Livepeer demonstrates transparency in its 
    token distribution. A balanced circulating and total supply often contributes to a healthier tokenomics model.

    **Volatility Metrics:**
    The 30 days volatility at 45.34% and 7 days volatility at 21.90% provide insights into the price fluctuation levels. Higher 
    volatility can present both opportunities and risks, attracting traders seeking price movements.

    **Tokenomics Strengths:**
    - **Fair Token Distribution:** Livepeer's equal circulating and total supply suggests a fair initial distribution, reducing  the 
      risk of token concentration in the hands of a few entities.
    - **Liquidity and Trading Activity:** The  24-hour trading volume signals a liquid market, encouraging active trading 
      and efficient price discovery.
    - **Volatility Management:** While the volatility metrics indicate price fluctuations, they also indicating the dynamic market conditions, 
      potentially attracting traders and investors.

    **Considerations and Future Outlook:**
    - **Inflationary Model:** Livepeer's inflationary model, with new tokens generated and allocated over time, aligns with a vision of 
      sustained network participation.
    - **User Incentives:** Transcoders and delegators play crucial roles in the Livepeer network, earning incentives in the form of LPT 
      for their contributions.

    """

    st.write(analysis_description)

    st.title("Vesting Schedule")

    st.write("The vesting schedule for Livepeer (LPT) tokens is 36 months from the network launch. This applies to the 12.35% of tokens allocated to founders and early team members.")
    st.image('assets/token_distribution.png')

    st.title("Insights from Tokenomics analysis")
    st.write('''Livepeer exhibits good tokenomics, featuring a fair distribution, active trading, and mechanisms to incentivize 
    network participants. The market dynamics and volatility metrics add layers to the token's attractiveness, making it an intriguing 
    option for traders and investors''')

