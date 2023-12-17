import streamlit as st
from PIL import Image

def d():
    st.markdown(
        """

    ## Governance Mechanisms and Business Model: 

    """
    )
    image_path = "./assets/Business_model_not_to_scale.png"
    image = Image.open(image_path)
    st.image(
        image, caption="Exemplary relation between the users,validators and GNOSIS-chain"
    )

    st.markdown(
        """

    At the heart of this ecosystem lies the Gnosis chain, a cutting-edge third-generation blockchain designed for sophisticated smart contracts and Dapps. Engineered for stability and scalability, it outpaces Ethereum in speed and cost efficiency. Notably, the Gnosis chain maintains compatibility with the Ethereum Virtual Machine (EVM) and employs a Proof-of-Stake (PoS) consensus mechanism for validity.

    PoS networks, such as the Gnosis chain, offer enhanced energy efficiency.In this more democratic approach, users stake their tokens in the network's smart contracts to secure its operations, eliminating technical barriers to participation in the blockchain validation process.

    ### Staking: 
    Gnosis allows users to create OWL tokens by locking their tokens in a smart contract. These locked tokens can’t be traded and the lock period and amount of OWL awarded varies. This is the only way for users to create OWL tokens and they are used to pay fees on the Apollo network.

    ### Gas: 
    xDai tokens are transactional tokens on Gnosis and also used to pay for execution of smart contracts and gas fees.
    These fees are currently sent to the validator who seals the block in which the transactions take place (transaction fees are not split among pool participants, they are only received by the validator).

    ### Governance: 
    GNO is used to vote on governance proposals on the network.
    Users wishing to participate in guiding the products and development of the Gnosis ecosystem must first purchase and hold GNO tokens.
    A minimum of 1 GNO token is required to join.
    However, the process involves a weighted system whereby the more GNO tokens a user holds, the greater their voting power will be.
    Gnosis uses a community governance mechanism to ensure the community has a voice in future changes.
    The Gnosis DAO (decentralized autonomous organization) enables users to put forth votes using the GNO tokens. The system weights votes based on the number of GNO tokens staked.
    Those with more investment have more say in the network's developments.

    ## Different Working Modes of Gnosis Chain Making it a Right Choice 

    Gnosis Safe (multisig and programmable account), Cow Protocol (formerly CowSwap and Gnosis Protocol), Conditional Tokens (prediction markets), Gnosis Auction, and Zodiac (standard and tooling for composable DAOs) are all products incubated by Gnosis. 
    Their success is demonstrated by the recent spin-out of Cow Protocol and the current discussion around SafeDAO. By combining needs-driven development with deep technical expertise, Gnosis has built the decentralized infrastructure for the Ethereum ecosystem.


    3 platforms of Gnosis:

    - Apollo: a prediction market platform that helps users create their own tokens
    - DutchX: a decentralized exchange where users can trade and auction their tokens
    - Gnosis Safe: an e-wallet and browser that can interact with Ethereum applications

    ### More about Gnosis Chain Fees : 

    The Gnosis Chain has three types of fees associated with it. First, users are charged a transaction fee for calling contracts on the chain.This fee is not deducted from accounts, but rather paid to miners who process the transactions. 
    Second, deploying contracts onto the chain requires staking GNO tokens as collateral.
    Stakers must pay an additional charge in order to be rewarded for their services on the chain thirdly, developers can choose to use their GNO tokens to pay for gas when running computations on the Gnosis Chain. This allows them to escrow their funds while also lowering their costs and gaining scalability benefits over other networks.

    """
    )
