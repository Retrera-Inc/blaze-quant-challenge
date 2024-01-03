import streamlit as st

st.set_page_config(page_title="Token Incentives And Associated Risks", page_icon="🪙")

st.title("Token Incentives and Associated Risks")

# Navigation bar
st.sidebar.title("Navigation")

nav_selection = st.sidebar.selectbox("Go to", [ "Incentives and Staking", "Governance Responsibilities", "Risk Parameters", "Risks and Mitigation"])

# Sections
intro_text = """
"""

incentives_text = """
The Maker (MKR) token plays a crucial role in the governance of the Maker Protocol. Here's a summary of the token-based incentives, staking mechanisms, and governance responsibilities:

## Token-Based Incentives and Staking Mechanisms

**Voting Authority:**
MKR token holders have the power to be part of the decision-making process for changes to the Maker Protocol, with each MKR token representing a voting right. Additionally, MKR holders can vote on different governance actions, such as introducing new collateral assets, adjusting risk parameters, changing the Dai Savings Rate, initiating an Emergency Shutdown, and upgrading the system.

**Proposal Submissions:**
Proposals for an MKR vote can still be made by anyone, not just MKR holders.

**Activation of Governance Security Module (GSM):**
MKR holders can activate the Governance Security Module, introducing a delay of up to 24 hours for approved modifications to become effective. This delay acts as a protective measure against potentially harmful governance proposals, affording MKR holders the opportunity to initiate a Shutdown in case of necessity.
"""

governance_responsibilities_text = """
### Governance Responsibilities

1. **Allocation of Funds:**
   MKR token holders possess the ability to designate funds from the Maker Buffer for essential infrastructure requirements, encompassing Oracle infrastructure and research related to collateral risk management. Maker Buffer funds derive from Stability Fees, Liquidation Fees, and various other revenue streams.

2. **Flexibility and Upgradability:**
   The governance framework is intentionally crafted to exhibit adaptability and a capacity for upgrades. MKR holders wield the power to determine more sophisticated iterations of Proposal Contracts as the system evolves.
"""

risk_parameters_text = """
### Risk Parameters Controlled by Maker Governance

The following risk parameters are controlled by Maker Governance:

- **Debt Ceiling Management:**
  Governs the upper limit of debt creation allowable for a specific collateral type.

- **Stability Fee Regulation:**
  Dictates the annual percentage yield applied to generated Dai against a Vault's collateral.

- **Liquidation Ratio and Penalty Framework:**
  Liquidation Ratio assesses anticipated price volatility, while Liquidation Penalty represents the surcharge incurred during a Liquidation event.

- **Auction Duration Parameters:**
  Encompasses specifications regarding the duration of Collateral auctions, Debt and Surplus auction durations, Auction Bid Duration, and Auction Step Size.
"""

risks_mitigation_text = """
### Risks and Mitigation

**Security Breaches:**
Countermeasures encompass rigorous security measures such as Formal Verification, comprehensive security audits, bug bounty programs, and ongoing surveillance to mitigate potential malicious attacks.

**Unforeseen Market Events:**
Mitigation strategies involve meticulous protocol design, incorporating elements like the Governance Security Module, Liquidation Ratio, Debt Ceilings, Emergency Shutdown, and the cultivation of sound governance practices to guard against Black Swan events.

**Market Fluctuations and Pricing Discrepancies:**
Mitigation efforts revolve around fostering market stability and efficiency by incentivizing Keepers. Additionally, the Emergency Shutdown serves as a final recourse in the event of pricing errors or market irrationality.

**User Retention Challenges:**
Mitigation involves the provision of comprehensive documentation and resources to facilitate the onboarding process for users with varying levels of experience.

**Safeguarding Against Maker Foundation Dissolution:**
MKR token holders are incentivized to proactively prepare for the potential dissolution of the Maker Foundation, ensuring the sustained governance and funding of the Maker Protocol.

**Mitigating Risks Associated with Experimental Technology:**
Strategies for risk mitigation encompass thorough technical audits and continuous monitoring to identify and address potential weaknesses, vulnerabilities, or bugs in the system.
"""

conclusion_text = """
### Conclusion

In conclusion, MKR token holders assume a pivotal role in shaping and safeguarding the integrity of the Maker Protocol, emphasizing responsible governance, risk management, and the enduring stability of the system. The outlined mechanisms and duties exemplify a deliberate strategy in addressing potential risks inherent in decentralized finance.
"""

# Display selected section
# if nav_selection == "Introduction":
#     st.markdown(intro_text)
if nav_selection == "Incentives and Staking":
    st.markdown(incentives_text, unsafe_allow_html=True)
elif nav_selection == "Governance Responsibilities":
    st.markdown(governance_responsibilities_text, unsafe_allow_html=True)
elif nav_selection == "Risk Parameters":
    st.markdown(risk_parameters_text, unsafe_allow_html=True)
elif nav_selection == "Risks and Mitigation":
    st.markdown(risks_mitigation_text, unsafe_allow_html=True)
# elif nav_selection=="Conclusion":
#     st.markdown(conclusion_text, unsafe_allow_html=True)