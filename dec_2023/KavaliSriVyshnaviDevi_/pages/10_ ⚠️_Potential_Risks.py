import streamlit as st
st.set_page_config(page_title="Potential Risks", page_icon="⚠️")
st.title("Potential Risks")

def display_makerdao_vulnerabilities():
        st.header("MakerDAO Vulnerabilities and Risks")

        st.markdown(
            "While MakerDAO has enhanced the security of its smart contracts, potential vulnerabilities still exist. "
            "Here are some critical areas of concern"
        )

        st.subheader("Issues in Smart Contract Code")
        st.markdown(
        "- **Programming oversights:** Even with a meticulous development process, smart contracts can have coding errors, "
        "leading to fund theft or manipulation of the protocol's functionality.\n"
        "- **Reentrancy attacks:** Exploiting when a function calls an external contract, which calls back before completion, "
        "allowing manipulation of the original contract and fund theft.\n"
        "- **Flash loan attacks:** Leveraging the transitory nature of flash loans to manipulate asset prices, potentially "
        "creating Dai without sufficient collateral."
    )

        st.subheader("Oracle Manipulation")
        st.markdown(
            "- **Centralized oracles:** Dependency on centralized oracles for price data. If compromised, malicious actors could "
            "manipulate oracles to disrupt the Dai peg.\n"
            "- **Oracle downtime:** Unavailability of oracles could impair the Maker Protocol, leading to potential instability."
        )

        st.subheader("Governance Vulnerabilities")
        st.markdown(
            "- **51% attacks:** Potential manipulation of the governance process if a single entity or a group controls a majority of MKR tokens.\n"
            "- **Collusion:** Malicious actors colluding to vote for proposals benefitting them at the expense of other users.\n"
            "- **Flash loan attacks:** Similar to smart contract vulnerabilities, flash loans could be used to manipulate the governance process."
        )

        st.header("Other Potential Risks")
        st.markdown(
            "In addition to smart contract and governance risks, MakerDAO faces other potential challenges:"
        )

        st.subheader("Economic Vulnerabilities")
        st.markdown(
            "- The stability of the Dai peg depends on the broader cryptocurrency market's health. A significant downturn could erode confidence in Dai."
        )

        st.subheader("Legal and Regulatory Uncertainty")
        st.markdown(
            "- The evolving legal and regulatory landscape introduces uncertainty. New regulations might impact the Maker Protocol's operations."
        )

        st.markdown(
        "MakerDAO actively addresses these vulnerabilities through ongoing security audits and continuous protocol enhancements. "
        "The engaged community plays a pivotal role in identifying and mitigating potential risks."
    )

def display_market_risks():
        st.header("Market Risks")
        st.markdown("MakerDAO, operating in the dynamic DeFi space, faces the following market-related risks:")

        st.subheader("Cryptocurrency Market Fluctuations")
        st.markdown(
        "- **MKR and Dai values** are directly influenced by the cryptocurrency market, exposing them to significant price swings and potential investor losses."
    )

        st.subheader("Dai Peg Instability")
        st.markdown(
        "- Despite being designed for a 1:1 peg with the US dollar, market volatility can strain the Dai peg, causing fluctuations that undermine confidence in the protocol."
    )

        st.subheader("Collateral Value Fluctuations")
        st.markdown(
            "- Fluctuations in the value of collateral assets backing Dai can trigger liquidations, impacting the Dai supply and further affecting the peg."
        )

        st.subheader("Regulatory Risks")
        st.markdown("Navigating the regulatory landscape presents its own set of risks:")

        st.markdown(
            "- **Uncertain Regulatory Environment:** Ongoing regulatory evolution introduces uncertainty, potentially affecting Maker Protocol operations and growth."
        )

        st.markdown(
            "- **Potential for Bans or Restrictions:** Some jurisdictions have contemplated or imposed bans on DeFi protocols, potentially reducing demand for MKR and Dai."
        )

        st.markdown(
            "- **AML and KYC Regulations:** Regulatory pressure for AML and KYC compliance could pose challenges for user participation and innovation within the protocol."
        )

        st.header("Beyond Market and Regulatory Risks")
        st.markdown("MakerDAO faces additional challenges")

        st.subheader("Smart Contract Vulnerabilities")
        st.markdown(
            "- Inherent to all smart contracts, Maker Protocol susceptibility to exploitation by malicious actors demands ongoing vigilance to safeguard funds and protocol functionality."
        )

        st.subheader("Governance Risks")
        st.markdown(
            "- The MKR token holders dictate Maker Protocol governance, introducing the risk of control by a select few with self-serving motives, potentially diverging from community interests."
        )

        st.subheader("Economic Risks")
        st.markdown(
            "- Dependent on Dai's widespread adoption, Maker Protocol's sustained success could be jeopardized if Dai fails to gain significant traction, impacting MKR demand and value."
        )

        st.markdown(
        "Despite these challenges, MakerDAO remains a pioneering DeFi protocol, continually evolving to enhance security and functionality. "
        "Investors are advised to grasp the nuanced risks inherent in MKR investments and Maker Protocol engagement."
    )

st.sidebar.title("Navigation")
selected_section = st.sidebar.selectbox("Go to", ["MakerDAO Vulnerabilities", "Market Risks"])

if selected_section == "MakerDAO Vulnerabilities":
    display_makerdao_vulnerabilities()
elif selected_section == "Market Risks":
    display_market_risks()
