import streamlit as st
from PIL import Image

def c():
    st.markdown(
        """
    ## On-chain Data Insights : 

    Gnosis includes 03 interinteroperable product lines (Gnosis Safe, Gnosis Protocol and GnosisDAO), allowing users to securely create, trade and hold digital assets on Ethereum.
    - Gnosis Chain is an EVM compatible, community owned network that prioritizes credible neutrality and resiliency, open to everyone without privilege or prejudice.This high-performance third-generation blockchain can handle advanced smart contracts and Dapps. The protocol was built to provide stability and scalability to the market. It’s faster and cheaper than Ethereum.Notably, The Gnosis chain uses a PoS (Proof-of-Stake) consensus mechanism to remain valid. 
    - The Gnosis Safe is the primary wallet for the network. Users can easily track their holdings and conduct international transactions using this dashboard. The wallet is completely EVM compatible, making it more usable for the average trader.

    """
    )
    image_path = "./assets/gnosis_levels.png"
    image = Image.open(image_path)
    st.image(image, caption="Layer-Wise-Demonstration-of-Gnosis-Chain")

    st.markdown(
        """

    ## Three Layers
    
    Three layers make Gnosis function. 
    - The first layer is called the Core Layer. This layer is where intelligent contracts live. It’s also responsible for handling settlements and market mechanisms. This structure helps to improve transaction times as it separates computation from validation processes.

    - The service layer is the next layer in the Gnosis ecosystem. This layer handles features such as chatbots, payment processor integrations, and stablecoins. The community can also set and debate trading fees and other costs in the service layer.

    - The application layer is where all the Dapps reside. This structure is ideal because it gives developers a specific network to build on that won't bog down the validation process. Notably, the application layer was built specifically to serve the needs of third-party developers.

    ## What consensus algorithm does Gnosis use?

    Gnosis, as a closely-related fork of Ethereum, underwent a “Merge” hardfork similar to that of Ethereum. The hardfork replaced Gnosis’ former “proof-of-authority” consensus with the “proof-of-stake” system as it merged with the Gnosis Beacon Chain. The Gnosis Merge replaced the Proof-of-Authority (PoA) consensus, which was secured by 20 validators, to a far more resilient 100,000 validators supporting the new PoS network. With nodes run by community members and teams around the world, the Gnosis Merge makes Gnosis the second most decentralized PoS network behind Ethereum.

    - Staking Means of GNO in GNOSIS Chain : 

    By staking your GNO tokens, you play a vital role in securing the Gnosis chain through the validation of blocks within the PoS consensus. As a reward for your participation, you will receive staking rewards. For a more comprehensive understanding of the validator deposit process, check the validator deposit process page.

    In order to establish a highly precise ETH-mirrored environment, it is required to stake a minimum of 32 tokens on the Gnosis Beacon Chain. To facilitate this, the mGNO token serves as a meta-token specifically designed for staking purposes. During the deposit process, an automatic conversion takes place where 1 GNO is transformed into 32 mGNO tokens behind the scenes.

    For those who prefer not to manage the infrastructure themselves, liquid staking providers offer the opportunity to stake without the need for personal infrastructure management. 
    """
    )
