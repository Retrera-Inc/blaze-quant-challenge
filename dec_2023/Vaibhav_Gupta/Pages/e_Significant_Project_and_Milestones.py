import streamlit as st
from PIL import Image

def e():
    st.markdown(
        """
    
    ## Significance Project Milestones     

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
    


    - Gnosis is a very promising and OG chain. Deploying there is an exciting next step for our ecosystem and further strengthens the ties between Gnosis and Balancer. Working alongside Karpatkey, our communities can more effectively collaborate and help shape the future of DeFi liquidity on L2s.
    [Fernando Martinelli, Balancer Labs CEO & Co-Founder]

    Gnosis Chain activates its own version of The Merge, transitions to proof-of-stake network .

    - Gnosis Chain has crossed its own Merge milestone, with the network transitioning to proof-of-stake.

    - The team says its Merge has made Gnosis Chain the third-most decentralized network behind Bitcoin and Ethereum.


    Gnosis Chain, a privacy-focused blockchain, has activated its own version of The Merge, and transactions on the network are now being processed under a proof-of-stake consensus in a process similar to what happened on Ethereum on Sept. 15.

    The Gnosis Chain underwent an upgrade that saw the network merge its previous execution layer with the Gnosis Beacon Chain launched last year. This process happened at the agreed-upon total terminal difficulty (TTD) on the Gnosis legacy chain at 01:47 PM EST on Thursday, and Gnosis paid homage to Ethereum by including Ethereum’s TTD in its own Merge TTD.

    Gnosis Chain now becomes the second network after Ethereum to transition to PoS from a different consensus architecture. The team says The Merge now makes the chain the third-most decentralized network in the crypto space after Bitcoin and Ethereum. Gnosis Chain’s validator count has subsequently increased from 20 to 100,000.

    Gnosis Chain's total value locked doubles to $150 million after MakerDAO's Spark Protocol expansion.

    - Gnosis Chain’s TVL doubled to $150 million since early October, fueled by stablecoin transfers.
    
    - Funds are being used on the network to earn yields from MakerDAO’s Spark lending protocol.

    
    # Gnosis Beacon Chain (GBC) 

    - In addition to providing stable, low-cost, and optimized transactions, the Gnosis Beacon Chain (GBC) infrastructure will be available to support important Ethereum updates, including EIP implementations. 
    - The GBC offers a new consensus opportunity for Gnosis Chain. Currently, Gnosis Chain uses a delegated Proof of Stake (DPOS) consensus mechanism called POSDAO. With the Gnosis Chain / GBC merge, a more diverse and distributed validator set will bring consensus to the chain. 
    
    # Gnosis Safe multisig wallets:
    
    These wallets are used by institutions and individuals to hold some of the largest quantities of funds on the Ethereum network. The free to use wallet includes multisignature functionality for enhanced security and control over digital assets.


    The main advantage of a Gnosis Safe multisig wallet is that it reduces the risk of unauthorized access or misuse of funds. Even if one of the signatories’ private keys is compromised, an attacker cannot access the wallet or perform transactions without the required number of signatures. This adds an extra layer of security compared to traditional single-signature wallets.
    Gnosis Safe multisig wallets are also used by individuals, organizations, or projects that require shared control over funds, such as cryptocurrency exchanges, investment funds, or decentralized autonomous organizations (DAOs). They provide a secure and flexible solution for managing and safeguarding digital assets in a collaborative manner.


    """
    )
    st.write("\n")
    image_path = "./assets/wallets.png"
    image = Image.open(image_path)
    st.image(image, caption="")
    
