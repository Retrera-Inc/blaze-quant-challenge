import streamlit as st
st.set_page_config(page_title="Smart Contracts", page_icon="📜")
st.title("Smart Contracts")

def display_recent_transformations():
    st.header("Recent Transformations")

    st.subheader("Core Protocol Advancements")

    st.markdown("**Multi-Collateral Dai (MCD):** Unveiled in November 2020, MCD revolutionizes the landscape by allowing users to collateralize various crypto assets, mitigating the risk of Dai instability linked to a single asset's price fluctuations.")

    st.markdown("**Dynamic Stability Fees:** Inaugurated in June 2022, this groundbreaking feature dynamically adjusts Dai's stability fee, responding to market conditions and the circulating supply of Dai. This adaptive mechanism ensures the steadfast peg between Dai and the US dollar.")

    st.markdown("**Governance Module V2:** Launched in April 2023, this pivotal upgrade refines the governance process, enhancing efficiency and transparency. It introduces innovative features like token-weighted voting and on-chain polls, elevating the governance experience for participants.")

    st.subheader("Other Advancements and Progress")

    st.markdown("**DeFi Protocol Integration:** MKR has seamlessly integrated into various DeFi protocols, broadening its utility and enriching its value proposition within the decentralized finance landscape.")

    st.markdown("**Institutional Adoption:** Witnessing a surge in adoption from institutional investors, MKR attains further legitimacy and experiences heightened demand, solidifying its status within the cryptocurrency realm.")

    st.markdown("**Burn Mechanisms:** MakerDAO strategically implements burn mechanisms, effectively reducing the circulating supply of MKR. This strategic move aims to potentially enhance the token's long-term value.")

def display_community_proposals():
    st.header("Community Proposals")

    st.subheader("Recent Community Proposals")

    st.markdown("**Block Size Increase**")
    st.markdown("   - **Proposal:** Expand the block size from 1 MB to 2 MB.")
    st.markdown("   - **Rationale:** Enhance transaction throughput and reduce confirmation times.")
    st.markdown("   - **Status:** Approved with a 75% majority.")
    st.markdown("   - **Implementation:** Scheduled for February 2024.")

    st.markdown("**Governance Model Transformation**")
    st.markdown("   - **Proposal:** Introduce a novel governance model based on Delegated Proof-of-Stake (DPoS).")
    st.markdown("   - **Rationale:** Improve community participation and decision-making processes.")
    st.markdown("   - **Status:** Under review by the core team; ongoing community discussions.")
    st.markdown("   - **Implementation:** Timeline yet to be determined.")

    st.markdown(" **Token Burning Mechanism**")
    st.markdown("   - **Proposal:** Implement a burning mechanism to decrease the total Marker token supply.")
    st.markdown("   - **Rationale:** Enhance the scarcity of Marker tokens, potentially appreciating their value.")
    st.markdown("   - **Status:** Rejected due to community concerns about potential price manipulation.")

    st.subheader("Upcoming Community Proposals")

    st.markdown(" **Lightning Network Integration**")
    st.markdown("   - **Proposal:** Integrate with the Lightning Network for expedited and cost-effective transactions.")
    st.markdown("   - **Rationale:** Improve scalability and facilitate micropayments.")
    st.markdown("   - **Expected Submission Date:** December 15, 2023.")

    st.markdown("**Decentralized Exchange (DEX) Launch**")
    st.markdown("   - **Proposal:** Launch a decentralized exchange (DEX) on the Marker blockchain.")
    st.markdown("   - **Rationale:** Provide a secure and trustless platform for trading Marker tokens and other cryptocurrencies.")
    st.markdown("   - **Expected Submission Date:** Early 2024.")

    st.markdown(" **Privacy-Focused Protocol Development**")
    st.markdown("   - **Proposal:** Fund the development of a privacy-focused protocol for Marker transactions.")
    st.markdown("   - **Rationale:** Enhance user privacy and anonymity.")
    st.markdown("   - **Expected Submission Date:** Q2 2024.")

st.sidebar.title("Navigation")
selected_section = st.sidebar.selectbox("Go to", ["Recent Transformations", "Community Proposals"])

if selected_section == "Recent Transformations":
    display_recent_transformations()
elif selected_section == "Community Proposals":
    display_community_proposals()

