import streamlit as st
from PIL import Image

import streamlit as st
from PIL import Image

st.markdown(
    """
       
## Evaluation of Potential Risks and Future Prospects :

During the two years of its existence, Gnosis development team has implemented a few important goals. The most outstanding milestones from the roadmap are connected with the implementation of DutchX Protocol:

 - Q4 2017: DutchX Protocol announced
 - July 2018: DutchX Smart Contracts Live on Mainnet
 - Dec 2018: slow.trade (app built on top of DutchX) live on Ethereum Mainnet
 - Feb 2019: DutchX 2.0 smart contracts deployed to Mainnet

"""
)
image_path = "./assets/Gnosis-milestones.jpg"
image = Image.open(image_path)
st.image(image, caption="")

st.markdown(
    """
 - The future projections include development of the dxDAO — a decentralized governance mechanism based on the Genesis protocol, and derived from the Holographic Consensus framework. 
This decentralized application will govern the trading protocol. Besides, the team is working on the mobile version of the Gnosis platform.

 - Gnosis Chain is currently secured by the POSDAO consensus, but this will be deprecated in the coming months as the Gnosis Chain incorporates a consensus-layer beacon chain. The Gnosis Beacon Chain mirrors the Ethereum Beacon Chain (with some important optimizations including faster blocks and epoch times). Close to 60,000 validators are already participating as the chain closes in on the merge between the Gnosis Chain EVM and the Gnosis Beacon Chain.

 - With the collaboration of GNO with the LI.FI and with xDAI chain , Gnosis Chain exists to facilitate high frequency and cost-efficient EVM-compatible transactions. Activity on Gnosis Chain is high, as the chain facilitated between 100,000–300,000 daily transactions for the month of February. As mentioned above, Gnosis Chain is home to a wide variety of crypto tooling that includes DEXs, NFT infrastructure, DAOs, gaming, and more. However, to fully unlock the potential of Gnosis Chain assets and protocols, users must be able to directly leverage tokens from other chains.

"""
)
image_path = "./assets/footer image.png"
image = Image.open(image_path)
st.image(image, caption="")
