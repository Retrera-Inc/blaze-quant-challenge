import streamlit as st
st.set_page_config(page_title="Partnerships", page_icon="🤝")

img_tag = '<img src="{}" style="width:10%; height:10%; padding-bottom:2%" alt="Your Image">'

def display_blockchain_defi():
    st.header("Blockchain and DeFi")

    st.subheader("Chainlink Integration")
    st.markdown("MakerDAO has seamlessly integrated with Chainlink's decentralized oracle network, leveraging it to furnish secure and dependable price data feeds for the Maker Protocol. This integration significantly enhances the stability and transparency of the Dai stablecoin.")
    st.markdown(img_tag.format("https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Chainlink_Logo.png/900px-Chainlink_Logo.png"), unsafe_allow_html=True)

    st.subheader("Aave Collaboration")
    st.markdown("In a collaborative effort with Aave, MakerDAO is exploring opportunities for cross-chain lending and borrowing activities between the Maker and Aave protocols. This venture has the potential to amplify liquidity and expand the user base for both platforms.")
    st.markdown(img_tag.format("https://cryptologos.cc/logos/aave-aave-logo.png"), unsafe_allow_html=True)

    st.subheader("NEAR Protocol Integration")
    st.markdown("MakerDAO has integrated with the NEAR Protocol, enabling access to Dai within the NEAR ecosystem. This integration unlocks novel possibilities for DeFi applications and extends the reach of Dai to a broader audience.")
    st.markdown(img_tag.format("https://cryptologos.cc/logos/near-protocol-near-logo.png"), unsafe_allow_html=True)

def display_traditional_finance():
    st.header("Traditional Finance")

    st.subheader("Société Générale Collaboration")
    st.markdown("MakerDAO's partnership with Société Générale represents a significant stride in bridging the gap between traditional finance and DeFi. This collaboration enables the bank to access Dai for its institutional clients, showcasing the increasing interest in DeFi within established financial institutions.")
    st.markdown(img_tag.format("https://www.societegenerale.com/sites/default/files/logo-societe-generale.png"), unsafe_allow_html=True)

    st.subheader("Visa Integration")
    st.markdown("In an innovative move, MakerDAO has integrated with Visa's network, facilitating Dai payments through Visa cards and digital wallets. This integration markedly broadens the real-world applications of Dai, making it more accessible to mainstream users.")
    st.markdown(img_tag.format("https://logos-world.net/wp-content/uploads/2020/05/Visa-Logo.png"), unsafe_allow_html=True)


    st.subheader("Mastercard Partnership")
    st.markdown("Similar to Visa, MakerDAO is in the process of forming a partnership with Mastercard, allowing Dai payments through Mastercard cards and digital wallets. This collaboration further extends the reach and utility of the Dai stablecoin.")
    st.markdown(img_tag.format("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Mastercard-logo.svg/2560px-Mastercard-logo.svg.png"), unsafe_allow_html=True)

def display_social_impact():
    st.header("Social Impact")

    st.subheader("GiveDirectly Collaboration")
    st.markdown("In a philanthropic effort, MakerDAO collaborates with GiveDirectly to distribute Dai directly to individuals in need during the COVID-19 pandemic. This initiative exemplifies the potential of DeFi for impactful social initiatives.")
    st.markdown(img_tag.format("https://www.givedirectly.org/wp-content/uploads/2020/02/cropped-knowledge_graph_logo-1.jpg"), unsafe_allow_html=True)
    

    st.subheader("Mercy Corps Ventures Partnership")
    st.markdown("In alignment with its commitment to social good, MakerDAO partners with Mercy Corps Ventures to support and invest in promising DeFi startups focusing on financial inclusion. This initiative harnesses the power of DeFi to address global challenges and promote financial access for underserved communities.")
    st.markdown(img_tag.format("https://logowik.com/content/uploads/images/mercy-corps6528.jpg"), unsafe_allow_html=True)
    

# Sidebar navigation
st.sidebar.title("Navigation")

selected_section = st.sidebar.selectbox("Go to", ["Blockchain and DeFi", "Traditional Finance", "Social Impact"])

st.title("Partnerships")

# Display content based on selected section
if selected_section == "Blockchain and DeFi":
    display_blockchain_defi()
elif selected_section == "Traditional Finance":
    display_traditional_finance()
elif selected_section == "Social Impact":
    display_social_impact()