import streamlit as st
st.set_page_config(page_title="Competitive Landscape", page_icon="🌐")
st.title("Competitive Landscape")

def display_competition():
        st.header("Competition in the DeFi Sector: MakerDAO")

        st.markdown("MakerDAO stands as a prominent player in the decentralized finance (DeFi) sector, particularly excelling in stablecoins and lending. While it has secured a leading position, it contends with competition from various established and emerging projects within the DeFi ecosystem.")

        st.subheader("Stablecoin Competitors")

        st.markdown("- **Tether (USDT):** The largest stablecoin, backed by traditional assets like cash and government bonds.")
        st.markdown("- **USD Coin (USDC):** Issued by a consortium of financial institutions, USDC is backed by a mix of assets including cash and U.S. Treasury bonds.")
        st.markdown("- **Binance USD (BUSD):** A stablecoin from Binance, backed by a basket of fiat currencies.")
        st.markdown("- **TerraUSD (UST):** An algorithmic stablecoin utilizing on-chain mechanisms and off-chain arbitrage to maintain its peg.")

        st.header("Lending Competitors")

        st.markdown("- **Aave:** A decentralized lending protocol facilitating lending and borrowing of various crypto assets.")
        st.markdown("- **Compound:** Another popular lending protocol with a distinct token distribution model.")
        st.markdown("- **Uniswap:** A decentralized exchange (DEX) providing an alternative liquidity option for crypto assets.")
        st.markdown("- **dYdX:** A decentralized margin trading platform enabling users to leverage their crypto assets for trading.")

def display_strengths_and_weaknesses():
    st.header("Strengths and Weaknesses of MakerDAO")

    st.subheader("Strengths of MakerDAO")
    
    st.markdown("- **First-mover advantage:**\n  MakerDAO, as one of the earliest DeFi protocols, boasts a substantial community and user base.")
    st.markdown("- **Strong brand recognition:**\n  A well-known and respected brand in the DeFi space, providing a competitive edge.")
    st.markdown("- **Decentralized governance:**\n  Governance by MKR token holders empowers users to influence the protocol's direction.")
    st.markdown("- **Multi-collateral Dai:**\n  MakerDAO's flexibility in collateral options enhances its potential user base.")
    st.markdown("- **Focus on stability and security:**\n  A commitment to maintaining the Dai peg's stability and protocol security.")

    st.subheader("Weaknesses of MakerDAO")

    st.markdown("- **Complex user experience:**\n  The Maker Protocol's intricacy may present challenges for new users.")
    st.markdown("- **High gas fees:**\n  Interaction with the protocol can be costly due to elevated gas fees on the Ethereum network.")
    st.markdown("- **Limited scalability:**\n  Current scalability limitations could impede the protocol's growth.")
    st.markdown("- **Regulatory uncertainty:**\n  Potential regulatory scrutiny in the DeFi space may pose challenges for MakerDAO.")

    st.markdown("Despite its challenges, MakerDAO remains a formidable contender in DeFi. Continuous innovation and adaptation will be essential for maintaining a leading position. The success of MakerDAO hinges on its ability to address weaknesses while leveraging strengths to attract and expand its user base.")

st.sidebar.title("Navigation")
selected_section = st.sidebar.selectbox("Go to", ["Competition", "Strengths and Weaknesses"])

if selected_section == "Competition":
    display_competition()
elif selected_section == "Strengths and Weaknesses":
    display_strengths_and_weaknesses()