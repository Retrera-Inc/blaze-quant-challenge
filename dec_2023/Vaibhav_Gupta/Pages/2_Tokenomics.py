import streamlit as st
from PIL import Image

st.markdown(
    """
            
## Tokenomics :

The max supply of GNO was initially capped at 10,000,000 to be fully vested in April 2021. However, on 4th May 2022, the Proposal to reduce Gnosis total supply was passed to cap supply at 3 million GNO.

"""
)
image_path = "./assets/content_GNO_Allocation_(1).png"
image = Image.open(image_path)
st.image(image, caption="Image Source: Token Terminal")

st.markdown(
    """

The Initial token distribution of GNO is as follows:

 - 95.80% is allocated to Gnosis Vault, Founders & Project
 - 4.20% is allocated to ICO Investors


The use of these proceeds are:
 - 5% is allocated to marketing
 - 15% is allocated to operations 
 - 20% is allocated to legal
 - 60% is allocated to core development

Funding Rounds

 - 12.5M was raised in a Token Sale in April 2017 where the team raised 250,000 ETH.
The sale was conducted as a Dutch auction which had a limit of $12.5 million raised or nine million GNO sold,
 whichever came first. 
 The 12.5 million cap was reached selling 418,777 GNO.

"""
)
