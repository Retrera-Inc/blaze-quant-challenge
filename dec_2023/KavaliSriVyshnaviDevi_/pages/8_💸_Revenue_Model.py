import streamlit as st
st.set_page_config(page_title="Revenue Model", page_icon="💸")
st.title("Revenue Model")

def display_primary_revenue_stream():
    st.header("Primary Revenue Stream")

    st.subheader("Stability Fees")
    st.markdown("MakerDAO primarily generates revenue through stability fees, which contribute to approximately 80% of its total income. These fees are essentially interest rates applied to users who generate DAI by collateralizing assets within the MakerDAO system.")
    st.markdown("The annualized interest rate, typically around 2%, serves a dual purpose by providing revenue for the platform and helping stabilize the value of DAI at its targeted peg of 1 USD.")

    st.subheader("Numerical Examples")

    st.markdown("To provide a numerical context, let's consider an example: if a user takes out a \\$1,000 DAI loan collateralized with ETH, the 2% annual stability fee amounts to \\$20. This fee is incurred as a part of the repayment process when the borrower retrieves their collateral.")
    st.markdown("Importantly, these stability fees are collected in MKR, the native token of MakerDAO, reinforcing the integral role of MKR in the platform's revenue model and governance structure.")
    st.markdown("This mechanism aligns the interests of the platform and its users, as the fees contribute to both the sustainability of MakerDAO and the stability of the DAI stablecoin.")

def display_other_revenue_streams():
    st.header("Other Revenue Streams")


    st.subheader("Dai Savings Rate")
    st.markdown("MakerDAO may explore the Dai Savings Rate, an interest rate on deposited DAI ranging between 0.5% to 1%. This presents an additional income source derived from loan interest or DeFi protocol fees.")

    st.subheader("Maker Platform Fees")
    st.markdown("Contemplated fees for specific governance actions could be set at approximately $10 to $50 per transaction, contributing to the overall revenue diversification.")

    st.subheader("Challenges and Considerations")
    st.markdown("- The challenge lies in diversifying revenue streams while concurrently upholding the stablecoin peg of DAI to the US dollar.")
    st.markdown("- The implementation of new revenue streams necessitates community consensus through MKR token holder votes.")

    st.subheader("Additional Facts")
    st.markdown("- MakerDAO maintains a substantial treasury reserve of MKR, and the potential sale of MKR could serve as an additional income source, contingent upon community approval.")
    st.markdown("- Real-world assets (RWAs) within the RWA portfolio presently contribute up to 79% of MakerDAO's existing fee revenue.")

    st.markdown("In summary, MakerDAO's revenue model centers on stability fees, providing a numerical breakdown of fees collected in MKR. The potential for revenue expansion through the Dai Savings Rate and Maker Platform Fees underscores the importance of diversification for long-term sustainability and the continued growth of the Maker Protocol. It's noteworthy that community engagement and consensus play a pivotal role in shaping and implementing these revenue strategies.")

st.sidebar.title("Navigation")
selected_section = st.sidebar.selectbox("Go to", ["Primary Revenue Stream", "Other Revenue Streams"])

if selected_section == "Primary Revenue Stream":
    display_primary_revenue_stream()
elif selected_section == "Other Revenue Streams":
    display_other_revenue_streams()