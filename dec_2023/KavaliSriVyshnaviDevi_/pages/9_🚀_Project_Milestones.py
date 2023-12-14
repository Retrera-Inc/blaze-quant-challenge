import streamlit as st
st.set_page_config(page_title="Project Milestones", page_icon="🚀")
st.title("Project Milestones")

def display_key_achievements():
        st.header("Key Achievements")

        st.subheader("Multi-Collateral Dai (MCD)")

        st.markdown("**Broadened Collateral Spectrum:** MCD now boasts an expanded array of collateral types, including WBTC, USDC, and LINK. This strategic diversification not only enriches the collateral landscape but also enhances capital efficiency.")

        st.markdown("**Adaptive Stability Fees:** In a testament to its adaptability, MakerDAO has implemented dynamic adjustments to stability fees. These alterations, guided by market conditions and risk parameters, uphold the steadfastness of the Dai peg while fostering a robust demand for borrowing Dai.")

        st.subheader("Dai Savings Rate (DSR)")

        st.markdown("**Elevated DSR:** A judicious increase in the Dai Savings Rate serves as a compelling incentive for users to stow away their Dai, contributing substantively to the protocol's stability.")

        st.markdown("**Liquidations Across Vault Types:** The integration of liquidations across all vault types serves as a robust risk mitigation measure, effectively minimizing the likelihood of collateral shortages and safeguarding the Dai peg.")

        st.subheader("Governance Advancements")

        st.markdown("**Swift Executive Votes:** The introduction of executive votes expedites the implementation of sanctioned governance proposals without necessitating additional polling rounds. This procedural refinement not only accelerates the governance process but also heightens the protocol's responsiveness.")

        st.markdown("**On-chain Governance Eminence:** Achieving a pinnacle in decentralization, all governance functions are now seamlessly executed on-chain. This pivotal move obviates the need for external voting platforms, further fortifying the decentralized ethos of the protocol.")

def display_innovations_and_collaborations():
        st.header("Innovations and Collaborations")

        st.subheader("Technical Refinements")

        st.markdown("**Reduction in Gas Fees:** Noteworthy reductions in gas fees have been achieved through strategic optimizations to the core smart contracts, rendering user interactions with the protocol more cost-effective.")

        st.markdown("**Enhanced Scalability:** The protocol's scalability has undergone improvements through the fine-tuning of the Dai Savings Rate (DSR) contract and the introduction of features such as liquidations for various vault types.")

        st.markdown("**Augmented Security Measures:** Several security upgrades, encompassing refined smart contract audits and the integration of additional on-chain oracles, contribute to bolstering the overall security framework.")

        st.subheader("Community Endeavors")

        st.markdown("**Developer Portal Launch:** The introduction of a new developer portal aims to furnish developers with essential resources and tools, facilitating the creation of applications on the Maker Protocol.")

        st.markdown("**Multilingual Accessibility:** The MakerDAO website and documentation are now accessible in multiple languages, broadening the protocol's reach to a more diverse audience.")

        st.markdown("**Educational Support:** A diverse array of educational resources is available to assist users in comprehending the intricacies of the Maker Protocol and optimizing its utilization.")

        st.subheader("Collaborations and Partnerships")

        st.markdown("**Chainlink Integration:** Integration with Chainlink's oracle network ensures the provision of secure and reliable price data feeds for the Maker Protocol.")

        st.markdown("**Aave Collaboration:** The collaborative effort with Aave explores promising opportunities in cross-chain lending and borrowing.")

        st.markdown("**NEAR Protocol Integration:** Integration with NEAR brings Dai into the NEAR ecosystem, fostering interoperability.")

        st.markdown("**Société Générale Partnership:** The partnership enables the bank to extend Dai offerings to its institutional clientele.")

        st.markdown("**Visa and Mastercard Integrations:** Collaborations with Visa and Mastercard enable Dai payments through their extensive networks.")

        st.markdown("**GiveDirectly and Mercy Corps Ventures Collaborations:** These partnerships actively support and promote social impact initiatives.")

st.sidebar.title("Navigation")
selected_section = st.sidebar.selectbox("Go to", ["Key Achievements", "Innovations and Collaborations"])

if selected_section == "Key Achievements":
    display_key_achievements()
elif selected_section == "Innovations and Collaborations":
    display_innovations_and_collaborations()