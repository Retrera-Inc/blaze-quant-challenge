import streamlit as st
from PIL import Image

def h():
    image_path = "./assets/Gnosis-Chain-Deep-Dive-Why-Build-on-Gnosis-Chain-1536x864.png"
    image = Image.open(image_path)
    st.image(image, caption="")


    st.markdown(
        """
                
    ## Why build on GNOSIS CHAIN ? 
                
    Gnosis Chain is kept secure by a geographically diverse network of 160,000+ validators. 
    This diverse and international set of validators in combination with a focus on community-driven governance ensures that Gnosis Chain stays neutral in its operations and true to its original values. 

    Gnosis Chain is governed by a DAO. Consequently, this means anyone can participate in the decision-making processes regarding the development and future of the network.     

    Some of the main benefits and reasons why you should build on this network: 

    - Globally Secured: Gnosis Chain is fortified by 160,000+ validators worldwide. 
    - Cost-Efficient: Experience efficient operations at the low cost of just $0.000099 per 100K gas.
    - 100% Uptime: Keep your dapps running without any issues thanks to Gnosis Chain’s 100% uptime. 
    - Swift Performance: With Gnosis Chain’s impressive five-second block time, you can experience rapid transaction confirmations to ensure your projects perform at the top level.
    - EVM-Compatibility: Gnosis Chain is EVM-compatible. Consequently, when working with this network, you can use Ethereum tools, smart contracts, and wallets you’re familiar with.
    - Decentralized Lending and Collateral Management: Gnosis chain enables the lending of ether and tokens, with smart contracts as collateral management system.
    - Tokenized Assets: Gnosis allows users to create and trade tokens on its blockchain in a secure and transparent way.
    - Permissioned Governance Model: Gnosis employs an open governance structure which has been built from the ground up to ensure user franchise is protected whilst holding community members accountable for their actions on its network(s).

    """
    )
