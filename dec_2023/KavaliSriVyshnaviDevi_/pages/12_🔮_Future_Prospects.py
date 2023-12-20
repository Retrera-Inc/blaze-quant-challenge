import streamlit as st
st.set_page_config(page_title="Future Prospects", page_icon="🔮")
st.title("Future Prospects")

st.sidebar.title("Navigation")

selected_section = st.sidebar.selectbox("Go to", ["Roadmap", "Market Potential"])

if selected_section == "Roadmap":
    st.header("Roadmap")
    st.markdown("The future development path for MKR is centered around crucial areas, some of them being:")
    st.markdown(" - **Decentralized Stablecoin Ecosystem:**  MKR aspires to emerge as the premier governance token for a decentralized stablecoin ecosystem. This involves advancing the Maker Protocol, diversifying collateral options, and seamlessly integrating with other DeFi applications.")
    st.markdown(" - **Enhanced Governance:**  MakerDAO is consistently seeking avenues to refine its governance processes. This encompasses streamlining MKR holders' participation in governance, bolstering transparency, and ensuring the overall stability of the Maker system.")
    st.markdown(" - **Scaling the Maker Protocol:**  Confronting scalability challenges, the Maker Protocol is undergoing intensive efforts to enhance throughput and efficiency.")
    st.markdown(" - **Research and Development:**  A steadfast commitment to ongoing research and development underscores MakerDAO's pursuit of continual improvement for the Maker Protocol, along with exploration of novel use cases for MKR.")

elif selected_section == "Market Potential":
    st.header("Market Potential")
    st.markdown("MKR exhibits substantial market potential, strategically positioned to seize a significant portion of the rapidly growing global stablecoin market. The surge in popularity of DeFi applications further propels demand for MKR, bolstered by the following factors:")
    st.markdown(" - **Strong DAI Demand:**  DAI, revered as one of the most popular and trusted stablecoins, propels increased demand for MKR as it governs the Maker Protocol.")
    st.markdown(" - **Growing DeFi Adoption:**  The escalating prominence of DeFi applications, particularly those reliant on stablecoins like DAI, generates additional demand for MKR.") 
    st.markdown(" - **Limited Token Supply:**  MKR's constrained token supply enhances its value as demand surges.")
    st.markdown(" - **Robust Community Support:**  Fortified by a dedicated and engaged community, MKR benefits from active advocacy, furthering its token and underlying technology.")

    st.markdown("However, challenges on the horizon for MKR encompass:")
    st.markdown(" - **Competition:**  The landscape features various stablecoins and DeFi platforms vying for market share.")
    st.markdown(" - **Regulatory Dynamics:**  In the ever-evolving regulatory environment for cryptocurrencies, uncertainties may pose challenges for MKR and other crypto assets.")
    st.markdown(" - **Technical Hurdles:**  Addressing scalability and ensuring stability stand out as substantial challenges for scaling the Maker Protocol.")
    st.markdown("In conclusion, MKR's market potential is robust, contingent on the adept navigation of challenges and the successful execution of its roadmap by the team.")
