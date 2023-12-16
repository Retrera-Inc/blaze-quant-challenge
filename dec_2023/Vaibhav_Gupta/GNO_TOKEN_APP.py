import streamlit as st
from PIL import Image

image_path = "./assets/Attlas_Blog_Phân-tích-token-45.jpg"
image = Image.open(image_path)
st.image(image, caption="")

st.markdown(
    """
## Overview : All about GNO token and GNOSIS-Chain .

 - Gnosis is a decentralized platform built on the Ethereum blockchain,which strives to create a global, open prediction market.
 - It operates as a decentralized autonomous organization (DAO),providing infrastructure for various types of decentralized applications (dApps).
 - Gnosis was founded in 2015 with a focus on building prediction markets to enable worldwide access to accurate information.
 - The platform's native cryptocurrency, GNO, is used to operate and govern the platform.
 - Gnosis has a maximum supply of 3,000,000 coins, with a circulating supply of 2,589,588 GNO at the time of writing.
 - Gnosis Chain is secured by over 100k validators around the world.


The core goal of Gnosis is to build a decentralized platform that allows anyone to participate in the prediction market, to customize information search and to become the standard for predictive assets.


## TimeLine  :

 - The protocol founders, Martin Koppelmann (CEO) and Stefan George (CTO), finally launched Gnosis in 2017
 - Published whitepaper 6/6/2018
 - ( GnosisDAO + Gnosis Chain ) In late 2020, Gnosis announced plans to fully decentralize into a DAO (Decentralized Autonomous Organization).
 - ( xDai + Gnosis ) In November 2021, the xDai and GnosisDAO communities voted to combine their vibrant ecosystems to create the Gnosis Chain.
 - ( On April 13th, 2023 the Safe team announced that all users on Gnosis Chain can execute sponsored transactions for the next 30 days.

## Table of Content :

 - Key Metrics and Market Comparisions
 - Tokenomics
 - On-chain Data Insights
 - Governance Mechanisms and Business Model
 - Significance Project Milestones
 - Social Activity
 - Why build on GNOSIS CHAIN ?
 - Evaluation of Potential Risks and Future Prospects
 - GNO Whitepaper

"""
)
# from streamlit_timeline import st_timeline

# st.set_page_config(layout="wide")

# items = [
#     {"id": 1, "content": "Development work begins", "start": "2015"},
#     {
#         "id": 2,
#         "content": "The protocol founders, Martin Koppelmann and Stefan George, finally launched Gnosis",
#         "start": "2017",
#     },
#     {"id": 3, "content": "Whitepaper Published", "start": "2018"},
# ]

# timeline = st_timeline(items, groups=[], options={}, height="300px")
# st.subheader("Selected item")
# st.write(timeline)


# ## Key Metrics and Market Comparisions :
# "''
# )

# image_path = "./assets/Revenue_ve_transaction_count.png"
# image = Image.open(image_path)
# st.image(image, caption=" # Revenue vs transaction_count (from July'23 onwards-)")

# st.markdown(
#     """

# """
# )

# image_path = "./assets/GN0_trading_Volume_vs_Revenue.png"
# image = Image.open(image_path)
# st.image(image, caption=" # GNO_Trading_Volume_vs_Revenue (from July'23 onwards-)")

# st.markdown(
#     """

# """
# )

# image_path = "./assets/Transaction_count_vs_Transaction_per_second.png"
# image = Image.open(image_path)
# st.image(
#     image,
#     caption=" # Transaction_count_vs_Transaction_per_second (from July'23 onwards-)",
# )

# st.markdown(
#     """
# | Key metrics    | :             |
# | -------------  | ------------- |
# | Ticket         | GNO           |
# | Blockchain     | Ethereum      |
# | Token standard | ERC-20        |
# | Token type     | governance    |
# | Token supply   | 10,000,000 GNO   |


# ## Tokenomics :

# Ever pondered the significance of tokenomics, especially when dealing with GNO investments?
# What sets apart projects with astute incentives for prolonged GNO holding,
# ensuring they outshine counterparts lacking a robust token ecosystem?


# The max supply of GNO was initially capped at 10,000,000 to be fully vested in April 2021. However, on 4th May 2022, the Proposal to reduce Gnosis total supply was passed to cap supply at 3 million GNO.

# """
# )
# image_path = "./assets/content_GNO_Allocation_(1).png"
# image = Image.open(image_path)
# st.image(image, caption="Image Source: Token Terminal")

# st.markdown(
#     """

# The Initial token distribution of GNO is as follows:

#  - 95.80% is allocated to Gnosis Vault, Founders & Project
#  - 4.20% is allocated to ICO Investors


# The use of these proceeds are:
#  - 5% is allocated to marketing
#  - 15% is allocated to operations
#  - 20% is allocated to legal
#  - 60% is allocated to core development

# Funding Rounds

#  - 12.5M was raised in a Token Sale in April 2017 where the team raised 250,000 ETH.
# The sale was conducted as a Dutch auction which had a limit of $12.5 million raised or nine million GNO sold,
#  whichever came first.
#  The 12.5 million cap was reached selling 418,777 GNO.

# """
# )
# # import requests
# # import streamlit as st/

# # data = requests.get("'https://jsonplaceholder.typicode.com/todos/1'").json()

# # st.write(data)
# st.markdown(
#     """
# ## On-chain Data Insights :

#  Gnosis includes 03 interinteroperable product lines (Gnosis Safe, Gnosis Protocol and GnosisDAO), allowing users to securely create, trade and hold digital assets on Ethereum.
# """
# )
# image_path = "./assets/gnosis_levels.png"
# image = Image.open(image_path)
# st.image(image, caption="Layer-Wise-Demonstration-of-Gnosis-Chain")

# st.markdown(
#     """

#  ## Three Layers

# Three layers make Gnosis function.
#  - The first layer is called the Core Layer. This layer is where intelligent contracts live. It’s also responsible for handling settlements and market mechanisms. This structure helps to improve transaction times as it separates computation from validation processes.

#  - The service layer is the next layer in the Gnosis ecosystem. This layer handles features such as chatbots, payment processor integrations, and stablecoins. The community can also set and debate trading fees and other costs in the service layer.

#  - The application layer is where all the Dapps reside. This structure is ideal because it gives developers a specific network to build on that won't bog down the validation process. Notably, the application layer was built specifically to serve the needs of third-party developers.

# What consensus algorithm does Gnosis use?

# Gnosis, as a closely-related fork of Ethereum, underwent a “Merge” hardfork similar to that of Ethereum. The hardfork replaced Gnosis’ former “proof-of-authority” consensus with the “proof-of-stake” system as it merged with the Gnosis Beacon Chain. The Gnosis Merge replaced the Proof-of-Authority (PoA) consensus, which was secured by 20 validators, to a far more resilient 100,000 validators supporting the new PoS network. With nodes run by community members and teams around the world, the Gnosis Merge makes Gnosis the second most decentralized PoS network behind Ethereum.

# - Staking Means of GNO in GNOSIS Chain :

# By staking your GNO tokens, you play a vital role in securing the Gnosis chain through the validation of blocks within the PoS consensus. As a reward for your participation, you will receive staking rewards. For a more comprehensive understanding of the validator deposit process, check the validator deposit process page.

# In order to establish a highly precise ETH-mirrored environment, it is required to stake a minimum of 32 tokens on the Gnosis Beacon Chain. To facilitate this, the mGNO token serves as a meta-token specifically designed for staking purposes. During the deposit process, an automatic conversion takes place where 1 GNO is transformed into 32 mGNO tokens behind the scenes.

# For those who prefer not to manage the infrastructure themselves, liquid staking providers offer the opportunity to stake without the need for personal infrastructure management.

# ## Social Activity :

# Popularity and Mention Ranking:

#  - Gnosis is discussed by 140 unique individuals.
#  - It is ranked #314 in terms of mentions and activity from collected posts.

# Sentiment Analysis Across Social Media:

#  - In the last 24 hours, Gnosis has an average sentiment score of 0.7 out of 5.
#  - On Twitter, 37.95% of tweets express bullish sentiment, while 23.08% express bearish sentiment.
#  - The majority (38.97%) of tweets are neutral about Gnosis.

#    Sentiment analysis is based on 195 tweets (taken into consideration so far).

# Gnosis is becoming more newsworthy, as evidenced by an increase in mentions and activity.


# ## Governance Mechanisms and Business Model:

# """
# )
# image_path = "./assets/Business_model_not_to_scale.png"
# image = Image.open(image_path)
# st.image(
#     image, caption="Exemplary relation between the users,validators and GNOSIS-chain"
# )

# st.markdown(
#     """

# At the heart of this ecosystem lies the Gnosis chain, a cutting-edge third-generation blockchain designed for sophisticated smart contracts and Dapps. Engineered for stability and scalability, it outpaces Ethereum in speed and cost efficiency. Notably, the Gnosis chain maintains compatibility with the Ethereum Virtual Machine (EVM) and employs a Proof-of-Stake (PoS) consensus mechanism for validity.

# PoS networks, such as the Gnosis chain, offer enhanced energy efficiency.In this more democratic approach, users stake their tokens in the network's smart contracts to secure its operations, eliminating technical barriers to participation in the blockchain validation process.

# Staking: Gnosis allows users to create OWL tokens by locking their tokens in a smart contract. These locked tokens can’t be traded and the lock period and amount of OWL awarded varies. This is the only way for users to create OWL tokens and they are used to pay fees on the Apollo network.

# Gas: xDai tokens are transactional tokens on Gnosis and also used to pay for execution of smart contracts and gas fees.
# These fees are currently sent to the validator who seals the block in which the transactions take place (transaction fees are not split among pool participants, they are only received by the validator).

# Governance: GNO is used to vote on governance proposals on the network.
# Users wishing to participate in guiding the products and development of the Gnosis ecosystem must first purchase and hold GNO tokens.
# A minimum of 1 GNO token is required to join.
# However, the process involves a weighted system whereby the more GNO tokens a user holds, the greater their voting power will be.
# Gnosis uses a community governance mechanism to ensure the community has a voice in future changes.
# The Gnosis DAO (decentralized autonomous organization) enables users to put forth votes using the GNO tokens. The system weights votes based on the number of GNO tokens staked.
# Those with more investment have more say in the network's developments.

# ## Significance Project Milestones

#  - Gnosis is a very promising and OG chain. Deploying there is an exciting next step for our ecosystem and further strengthens the ties between Gnosis and Balancer. Working alongside Karpatkey, our communities can more effectively collaborate and help shape the future of DeFi liquidity on L2s.
#  [Fernando Martinelli, Balancer Labs CEO & Co-Founder]

# Gnosis Chain activates its own version of The Merge, transitions to proof-of-stake network .

#  - Gnosis Chain has crossed its own Merge milestone, with the network transitioning to proof-of-stake.

#  - The team says its Merge has made Gnosis Chain the third-most decentralized network behind Bitcoin and Ethereum.


# Gnosis Chain, a privacy-focused blockchain, has activated its own version of The Merge, and transactions on the network are now being processed under a proof-of-stake consensus in a process similar to what happened on Ethereum on Sept. 15.

# The Gnosis Chain underwent an upgrade that saw the network merge its previous execution layer with the Gnosis Beacon Chain launched last year. This process happened at the agreed-upon total terminal difficulty (TTD) on the Gnosis legacy chain at 01:47 PM EST on Thursday, and Gnosis paid homage to Ethereum by including Ethereum’s TTD in its own Merge TTD.

# Gnosis Chain now becomes the second network after Ethereum to transition to PoS from a different consensus architecture. The team says The Merge now makes the chain the third-most decentralized network in the crypto space after Bitcoin and Ethereum. Gnosis Chain’s validator count has subsequently increased from 20 to 100,000.

# Gnosis Chain's total value locked doubles to $150 million after MakerDAO's Spark Protocol expansion.

#  - Gnosis Chain’s TVL doubled to $150 million since early October, fueled by stablecoin transfers.

#  - Funds are being used on the network to earn yields from MakerDAO’s Spark lending protocol.

# """
# )

# image_path = "./assets/Gnosis-Chain-Deep-Dive-Why-Build-on-Gnosis-Chain-1536x864.png"
# image = Image.open(image_path)
# st.image(image, caption="")


# st.markdown(
#     """

# ## Why build on GNOSIS CHAIN ?

# Gnosis Chain is kept secure by a geographically diverse network of 160,000+ validators.
# This diverse and international set of validators in combination with a focus on community-driven governance ensures that Gnosis Chain stays neutral in its operations and true to its original values.

# Gnosis Chain is governed by a DAO. Consequently, this means anyone can participate in the decision-making processes regarding the development and future of the network.

# Some of the main benefits and reasons why you should build on this network:

#  - Globally Secured: Gnosis Chain is fortified by 160,000+ validators worldwide.
#  - Cost-Efficient: Experience efficient operations at the low cost of just $0.000099 per 100K gas.
#  - 100% Uptime: Keep your dapps running without any issues thanks to Gnosis Chain’s 100% uptime.
#  - Swift Performance: With Gnosis Chain’s impressive five-second block time, you can experience rapid transaction confirmations to ensure your projects perform at the top level.
#  - EVM-Compatibility: Gnosis Chain is EVM-compatible. Consequently, when working with this network, you can use Ethereum tools, smart contracts, and wallets you’re familiar with.

# ## Evaluation of Potential Risks and Future Prospects :

# During the two years of its existence, Gnosis development team has implemented a few important goals. The most outstanding milestones from the roadmap are connected with the implementation of DutchX Protocol:

#  - Q4 2017: DutchX Protocol announced
#  - July 2018: DutchX Smart Contracts Live on Mainnet
#  - Dec 2018: slow.trade (app built on top of DutchX) live on Ethereum Mainnet
#  - Feb 2019: DutchX 2.0 smart contracts deployed to Mainnet

# """
# )
# image_path = "./assets/Gnosis-milestones.jpg"
# image = Image.open(image_path)
# st.image(image, caption="")

# st.markdown(
#     """
#  - The future projections include development of the dxDAO — a decentralized governance mechanism based on the Genesis protocol, and derived from the Holographic Consensus framework.
# This decentralized application will govern the trading protocol. Besides, the team is working on the mobile version of the Gnosis platform.

#  - Gnosis Chain is currently secured by the POSDAO consensus, but this will be deprecated in the coming months as the Gnosis Chain incorporates a consensus-layer beacon chain. The Gnosis Beacon Chain mirrors the Ethereum Beacon Chain (with some important optimizations including faster blocks and epoch times). Close to 60,000 validators are already participating as the chain closes in on the merge between the Gnosis Chain EVM and the Gnosis Beacon Chain.

#  - With the collaboration of GNO with the LI.FI and with xDAI chain , Gnosis Chain exists to facilitate high frequency and cost-efficient EVM-compatible transactions. Activity on Gnosis Chain is high, as the chain facilitated between 100,000–300,000 daily transactions for the month of February. As mentioned above, Gnosis Chain is home to a wide variety of crypto tooling that includes DEXs, NFT infrastructure, DAOs, gaming, and more. However, to fully unlock the potential of Gnosis Chain assets and protocols, users must be able to directly leverage tokens from other chains.

# """
# )
# image_path = "./assets/footer image.png"
# image = Image.open(image_path)
# st.image(image, caption="")
